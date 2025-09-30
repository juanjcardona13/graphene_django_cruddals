# Optimización de queries GraphQL en Django

## 1. Análisis del AST de GraphQL (`_queryset_factory_analyze`)

### ¿Qué hace?
Esta función analiza la estructura de la query GraphQL antes de ejecutarla y determina qué relaciones es necesario cargar para evitar **N+1 queries**.

### Cambio principal (líneas 409-450):

```python
# ANTES: No extraía el orderBy
related_queryset = related_model.objects.all()

# AHORA: Extrae orderBy de los argumentos GraphQL
field_args = parse_arguments_ast(field.arguments, ...)
order_by = field_args.get('orderBy')
order_by_list = order_by_input_to_args(order_by)

# Aplica el ordenamiento al Prefetch
related_queryset = related_queryset.order_by(*order_by_list)
```

### ¿Por qué es importante?
- Cuando existe `paginatedManyToManyField(orderBy: {id: ASC})`, el **orderBy** se aplica dentro del `Prefetch`.  
- Los datos llegan ya ordenados, lo que evita tener que ordenarlos después.  
- Cuando los datos están en una **lista (prefetched)**, no es posible llamar `.order_by()` sobre ella.  

### Ejemplo visual:

```graphql
query {
  searchModelCs {
    objects {
      paginatedManyToManyField(orderBy: {id: ASC}) {  # ← orderBy se extrae aquí
        objects { id }
      }
    }
  }
}
```

Se convierte en:

```python
Prefetch(
    'many_to_many_field',
    queryset=ModelD.objects.all()
        .select_related('foreign_key_field')
        .order_by('id')  # ← orderBy aplicado aquí
)
```

---

## 2. Uso de datos prefetched (`default_search_field_resolver`)

### Cambio principal (líneas 499-512):

```python
# ANTES: Siempre obtenía datos frescos del manager
queryset = maybe_queryset(default_manager)

# AHORA: Verifica si ya están prefetched
if hasattr(root, '_prefetched_objects_cache') and field_name_for_prefetch in root._prefetched_objects_cache:
    # ✓ Usa datos ya cargados (sin query adicional)
    queryset = list(root._prefetched_objects_cache[field_name_for_prefetch])
else:
    # ✗ No están prefetched, los obtiene normalmente
    queryset = maybe_queryset(maybe_manager)
```

### ¿Qué es `_prefetched_objects_cache`?
Es un diccionario interno de Django que guarda los datos cargados por `prefetch_related()`:

```python
# Después de ejecutar:
ModelC.objects.prefetch_related('many_to_many_field')

# Cada objeto ModelC contiene:
model_c_instance._prefetched_objects_cache = {
    'many_to_many_field': <queryset con datos ya cargados>
}
```

### Flujo de ejecución
1. **Query GraphQL**
2. `searchModelCs` (query principal)  
3. `default_search_field_resolver` ejecuta:
   - `SELECT ModelC` (1 query)  
   - `Prefetch many_to_many_field` (1 query)  
4. Para cada `ModelC`:  
   - `paginatedManyToManyField` detecta datos en `_prefetched_objects_cache`  
   - Los usa directamente (**0 queries adicionales!**)  

---

## 3. Evitar operaciones sobre listas (líneas 524-566)

```python
# Detectar si los datos ya están cargados como lista
is_prefetched = isinstance(queryset, list) or (...)

# EVITAR llamar métodos de QuerySet sobre listas
if not isinstance(queryset, list):
    queryset = queryset.order_by(...)  # ✓ Solo si es QuerySet
    
if not is_prefetched and not isinstance(queryset, list):
    queryset = queryset.distinct()  # ✓ Solo si no está prefetched
```

### ¿Por qué?
Las listas no contienen métodos como `.order_by()` o `.distinct()`.  
Si se intenta llamarlos, ocurre el error:

```
AttributeError: 'list' object has no attribute 'order_by'
```

---

## 4. Optimización de paginación (`paginate_queryset`)

### Cambio principal (líneas 423-480):

```python
# ANTES: Usaba Django Paginator que ejecuta count() múltiples veces
p = Paginator(qs, items_per_page)
return paginated_type(
    total=p.count,        # ← COUNT ejecutado aquí
    pages=p.num_pages,    # ← COUNT ejecutado de nuevo
    ...
)

# AHORA: Cachea el count y calcula todo manualmente
total_count = qs.count()  # ← COUNT ejecutado SOLO UNA VEZ

num_pages = math.ceil(total_count / items_per_page)
start_index = (page - 1) * items_per_page
end_index = start_index + items_per_page

page_objects = qs[start_index:end_index]  # Slicing directo

return paginated_type(
    total=total_count,    # ← Usa el count cacheado
    pages=num_pages,      # ← Usa el count cacheado
    ...
)
```

### Resultado
- De **2 COUNTs duplicados** → **1 COUNT** por nivel de paginación.  
- Reducción inmediata de queries duplicadas.  

---

## 5. Resumen del flujo completo

### Ejemplo con la query:

```graphql
query {
  searchModelCs {  # ← Nivel 1
    objects {
      id
      paginatedManyToManyField(orderBy: {id: ASC}) {  # ← Nivel 2
        objects {
          id
          foreignKeyField { id }
        }
      }
    }
  }
}
```

### Ejecución optimizada:

1. **ANÁLISIS (antes de ejecutar queries)**  
   `_queryset_factory_analyze()` analiza el AST:
   - Detecta: `searchModelCs` necesita `many_to_many_field`  
   - Detecta: `orderBy {id: ASC}`  
   - Crea:  
     ```python
     Prefetch('many_to_many_field', queryset=ModelD.objects.order_by('id'))
     ```

2. **EJECUCIÓN (queries SQL)**  
   - Query 1: `SELECT COUNT(*) FROM ModelC`  
   - Query 2: `SELECT * FROM ModelC ... (13 objetos)`  
   - Query 3: `SELECT * FROM ModelD WHERE modelc_id IN (1,2,...,13) ORDER BY id ASC`  

3. **RESOLUCIÓN de campos anidados**  
   - Para cada `ModelC`:  
     - `paginatedManyToManyField` usa `_prefetched_objects_cache`  
     - **No ejecuta queries adicionales**  
     - Pagina sobre la lista prefetched  

✅ **Total: 3 queries en lugar de 99!**

---

## 6. Comparación: Antes vs Después

### ANTES (99 queries):

```python
# Por cada ModelC (13 objetos):
for model_c in model_cs:
    model_c.many_to_many_field.all()      # 1 query
    model_c.many_to_many_field.count()    # 1 query (duplicada)
    model_c.many_to_many_field.count()    # 1 query (duplicada otra vez)
    
    for model_d in model_c.many_to_many_field.all():
        model_d.foreign_key_field         # 1 query (N+1)
```

➡️ Total: `13 * (1 + 2 + N) = ~99 queries`

---

### DESPUÉS (27 queries):

```python
# Una sola vez:
Prefetch(
  'many_to_many_field', 
  queryset=ModelD.objects
           .select_related('foreign_key_field')
           .order_by('id')
)  # ← 1 query para todos

# Por cada ModelC:
for model_c in model_cs:
    # Usa datos prefetched (0 queries)
    # COUNT una sola vez (1 query)
    # Pagina sobre lista (0 queries)
```

➡️ Total: `6 queries principales + 21 lazy loading = 27 queries`

---

## 7. Puntos clave para recordar

- `Prefetch` carga relaciones en una sola query para todos los objetos.  
- `_prefetched_objects_cache` guarda esos datos para reutilizarlos.  
- `_queryset_factory_analyze` analiza el AST GraphQL para crear los `Prefetch` correctos.  
- `default_search_field_resolver` detecta y usa datos prefetched cuando están disponibles.  
- `paginate_queryset` cachea el `count` para evitar queries duplicadas.  


## 8. Queries necesarias y optimizadas

### Queries necesarias y optimizadas (primeras 6):
- **Query 1:** COUNT principal de ModelC ✓
- **Query 2:** SELECT principal con `select_related (oneToOneField)` ✓
- **Query 3:** Prefetch para `oneToOneField.paginatedForeignKeyERelated` ✓
- **Query 4:** Prefetch para `many_to_many_field` ✓
- **Query 5:** Prefetch para `many_to_many_field.paginatedForeignKeyERelated` ✓
- **Query 6:** Prefetch para `foreign_key_D_related` ✓

### Queries que aún es posible eliminar (queries 7-27):
- **Queries 7-10:** 4 SELECTs individuales de ModelD (IDs 1-4)
- **Queries 11-27:** 17 SELECTs individuales de ModelC y ModelD para resolver campos anidados

Estas queries individuales ocurren porque GraphQL resuelve campos dentro de objetos ya paginados, y esos resolvers no usan los datos del prefetch. El problema está en que cuando el resolver accede a campos como `foreignKeyField` dentro de los objetos paginados, se produce **lazy loading** en lugar de usar los datos cargados previamente.

### Resumen de la optimización:
- ✅ 73% de reducción en queries (**99 → 27**)
- ✅ Eliminados todos los COUNTs duplicados
- ✅ Prefetch funcionando correctamente para las relaciones principales
- ⚠️ Aún hay 21 queries individuales que provienen del lazy loading de campos dentro de objetos paginados

Las **27 queries restantes** son muy buenas considerando la complejidad de la query con múltiples niveles de anidación. Para eliminar las últimas 21 queries individuales, es necesario agregar más **prefetches anidados** dentro de los Prefetch existentes, pero eso implica modificaciones más profundas en cómo `_queryset_factory_analyze` construye los Prefetch anidados.