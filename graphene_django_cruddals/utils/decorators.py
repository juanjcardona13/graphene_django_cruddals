from typing import List, Optional


def resolver_hints(
    select_related: Optional[List[str]] = None,
    prefetch_related: Optional[List[str]] = None,
    only: Optional[List[str]] = None,
):
    """
    Decorator to declare optimization hints in computed fields.

    This decorator allows computed fields (calculated/virtual fields)
    to declare which model fields they need to function. The optimization
    system will use these hints to apply select_related, prefetch_related
    and only automatically when the field is requested.

    Args:
        select_related: List of OneToOne/ForeignKey relationships to optimize with JOIN
        prefetch_related: List of ManyToMany/reverse FK relationships to prefetch
        only: List of specific model fields to load

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

    Example with prefetch_related:
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
        Decorated function with hint attributes for the optimization system
    """

    def wrapper(f):
        f.select_related = select_related or []
        f.prefetch_related = prefetch_related or []
        f.only = only or []
        f.have_resolver_hints = True
        return f

    return wrapper


__all__ = ["resolver_hints"]
