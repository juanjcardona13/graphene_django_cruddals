Para mantener sincronizado este proyecto se debe de tener en cuenta varios factores:

1. Repositorio en si mismo, es el que contiene el código fuente, el proyecto como tal, aca es donde esta la version que usa PyPi para mostrar.
2. PyPi, es el repositorio de paquetes de Python, aca se sube el proyecto para que sea accesible a todos, se debe de publicar, actualmente se esta usando GitHub Actions para automatizar este proceso.
3. Documentación, se debe de mantener actualizada, se esta usando MkDocs para generar la documentación, y se esta usando ReadTheDocs para publicarla, esto es como si fuera un proyecto mas, pero de documentación, tiene su propio requirements.txt.
4. Pruebas, se debe de mantener actualizado el proyecto de pruebas, se esta usando PyTest para las pruebas, junto con tox para que se ejecute en diferentes versiones de Python, se esta usando GitHub Actions para automatizar este proceso, adicional esto se conecta con CodeCov para tener un reporte de cobertura de pruebas, para conectar con CodeCov se debe de tener un token, este token se debe de guardar en GitHub Secrets.
5. GitHub Actions, se esta usando para automatizar los procesos de publicación en PyPi, pruebas, y documentación, se debe de tener en cuenta que se deben de guardar las credenciales de PyPi en GitHub Secrets.
6. ReadTheDocs, se esta usando para publicar la documentación
7. CodeCov, se esta usando para tener un reporte de cobertura de pruebas, se debe de tener en cuenta que se deben de guardar las credenciales de CodeCov en GitHub Secrets.
8. MkDocs, se esta usando para generar la documentación
9. Tox, se esta usando para ejecutar las pruebas en diferentes versiones de Python
10. PyTest, se esta usando para las pruebas
11. PyPi, se esta usando para publicar el proyecto
12. CodeCov, se esta usando para tener un reporte de cobertura de pruebas
13. MkDocs Material, se esta usando para el tema de la documentación


Adicional, por ahora se esta usando Makefile para configurar el ambiente de desarrollo se usa con los siguientes comandos:

1. `make dev-setup` se usa para instalar las dependencias de desarrollo, no se usa requirements.txt en la raíz del proyecto, si no que va al archivo de setup.py y toma las dependencias de desarrollo, adicional con la bandera -e se instala el proyecto en modo editable.
2. `make tests` se usa para ejecutar las pruebas, se esta usando PyTest para las pruebas, y se esta usando Tox para ejecutar las pruebas en diferentes versiones de Python.
3. `make format` se usa para formatear el código, se esta usando ruff para formatear el código.
4. `make lint` se usa para revisar el código, se esta usando ruff para revisar el código.



Para publicar en PyPi manualmente se debe de hacer lo siguiente:

1. Instalar

pip install wheel => para generar el archivo .whl
pip install twine => para subir el archivo .whl a PyPi

2. Generar los archivos necesarios

python setup.py sdist bdist_wheel => para generar los archivos necesarios para subir a PyPi

3. Revisar los archivos generados

twine check dist/* => para verificar que los archivos generados esten correctos

4. Subir a PyPi

twine upload dist/* => para subir los archivos a PyPi

Release version 0.1.4


Por ultimo, para actualizar el proyecto Graphene Django Cruddals correctamente se debe de hacer lo siguiente:

Estaría bien estos pasos, para publicar mi proyecto:

1. Asegurarse de tener el virtualenv activado
2. Correr los comandos de make
  `make dev-setup`
  `make tests`
  `make format`
  `make lint`
3. Actualizar el archivo `__init__.py` con la nueva versión
4. Hacer todos los pasos necesarios de git
  `git add .`
  `git commit -m "UPDATE MESSAGE HERE"`
  `git tag v0.1.4`
  `git push origin main --tags`
  `git add . && git commit -m "Release version 0.1.4" && git tag v0.1.4 && git push origin main --tags`
5. Esperar a que GitHub Actions haga su trabajo
  - Correr los test
  - Correr el lint
  - Actualizar codecov
  - Actualizar la documentación
  - Publicar en PyPi
6. Verificar que todo este correcto
  - Verificar que la documentación este correcta
  - Verificar que la cobertura de pruebas este correcta
  - Verificar que el proyecto este publicado en PyPi


