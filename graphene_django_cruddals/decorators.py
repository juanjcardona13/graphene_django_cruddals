# -*- coding: utf-8 -*-
"""
Decoradores para optimización de resolvers y computed fields.
"""

from typing import List, Optional


def resolver_hints(
    select_related: Optional[List[str]] = None,
    prefetch_related: Optional[List[str]] = None,
    only: Optional[List[str]] = None,
):
    """
    Decorador para declarar hints de optimización en computed fields.

    Este decorador permite que los computed fields (campos calculados/virtuales)
    declaren qué campos del modelo necesitan para funcionar. El sistema de
    optimizaciones usará estos hints para aplicar select_related, prefetch_related
    y only automáticamente cuando el campo sea solicitado.

    Args:
        select_related: Lista de relaciones OneToOne/ForeignKey a optimizar con JOIN
        prefetch_related: Lista de relaciones ManyToMany/reverse FK a prefetch
        only: Lista de campos específicos del modelo a cargar

    Example:
        ```python
        class UserType(ModelObjectType):
            full_name = graphene.String()

            @resolver_hints(
                select_related=['profile', 'company'],
                only=['first_name', 'last_name', 'profile__avatar']
            )
            def resolve_full_name(self, info):
                return f"{self.first_name} {self.last_name}"
        ```

    Example con prefetch_related:
        ```python
        class PostType(ModelObjectType):
            comment_count = graphene.Int()

            @resolver_hints(
                prefetch_related=['comments']
            )
            def resolve_comment_count(self, info):
                return self.comments.count()
        ```

    Returns:
        Función decorada con atributos de hints para el sistema de optimizaciones
    """
    def wrapper(f):
        f.select_related = select_related or []
        f.prefetch_related = prefetch_related or []
        f.only = only or []
        f.have_resolver_hints = True
        return f

    return wrapper


__all__ = ["resolver_hints"]
