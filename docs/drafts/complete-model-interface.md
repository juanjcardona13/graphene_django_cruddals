```python
class ExampleModelInterface:
    
    class ObjectType: # This is the class that will be used to modify the ObjectType of the model
        
        class Meta: # This is the class that will be used to modify the Meta class of the ObjectType
            only_fields = "__all__" # Tuple of str or "__all__"
            exclude_fields = () # Tuple of str

        new_field = graphene.String() # Graphene => Scalar, String, ID, Int, Float, Boolean, Date, DateTime, Time, Decimal, JSONString, UUID, List, NonNull, Enum, Argument, Dynamic

        def resolve_new_field(self, info): # Resolver for new_field should be a function with the same name as the field prefixed by "resolve_" and receive 2 arguments (self, info), return the value of the field same type as the field
            return "new_field"

        # another fields with their resolvers

        @classmethod
        def get_queryset(cls, queryset, info): # This method is special and is used to modify the queryset before it is returned, receives 3 arguments (cls, queryset:QuerySet de Django, info), return queryset
            return queryset

    class InputObjectType:
        class Meta:
            only_fields = "__all__"
            exclude_fields = ()
            #(deprecated)hold_required_in_fields = False  # Podría ser también reemplazar esto por required_fields = "__all__" y not_required_fields = ()

        new_field = graphene.String()
        # exist_field = CruddalsRelationField() => For relations

        # Implícitamente si pone un campo que ya estaba en el ModelInputObjectType, sera sobrescrito por el que ponga de ultimo
        # y ya todos los otros nuevos serán nuevos campos como tal

    class CreateInputObjectType:
        class Meta:
            only_fields = "__all__"
            exclude_fields = ()
            #(deprecated)hold_required_in_fields = False  # Podría ser también reemplazar esto por required_fields = "__all__" y not_required_fields = ()

        new_field = graphene.String()
        # exist_field = CruddalsRelationField() => For relations

        # Implícitamente si pone un campo que ya estaba en el ModelInputObjectType, sera sobrescrito por el que ponga de ultimo
        # y ya todos los otros nuevos serán nuevos campos como tal

    class UpdateInputObjectType:
        class Meta:
            only_fields = "__all__"
            exclude_fields = ()
            #(deprecated)hold_required_in_fields = False  # Podría ser también reemplazar esto por required_fields = "__all__" y not_required_fields = ()

        new_field = graphene.String()
        # exist_field = CruddalsRelationField() => For relations

        # Implícitamente si pone un campo que ya estaba en el ModelInputObjectType, sera sobrescrito por el que ponga de ultimo
        # y ya todos los otros nuevos serán nuevos campos como tal

    class FilterInputObjectType:
        class Meta:
            only_fields = "__all__"
            exclude_fields = ()

        new_field = graphene.String()

        # Implícitamente si pone un campo que ya estaba en el ModelInputObjectType, sera sobrescrito por el que ponga de ultimo
        # y ya todos los otros nuevos serán nuevos campos como tal

    class OrderByInputObjectType:
        class Meta:
            only_fields = "__all__"
            exclude_fields = ()

        new_field = graphene.String()

        # Implícitamente si pone un campo que ya estaba en el ModelInputObjectType, sera sobrescrito por el que ponga de ultimo
        # y ya todos los otros nuevos serán nuevos campos como tal

    class CreateField:
        class Meta:
            modify_input_argument = {
                "name": "input",
                "required": True,
                "description": "",
                "hidden": False,
            }
            extra_arguments = {}

        def pre_mutate(*args, **kwargs):
            return (*args, kwargs)

        def mutate(*args, **kwargs):
            return "object_create"

        def override_total_mutate(*args, **kwargs):
            return "object_create"

        def post_mutate(*args, **kwargs):
            return "object_create"

    class ReadField:
        class Meta:
            modify_where_argument = {
                "name": "where",
                "required": True,
                "description": "",
                "hidden": False,
            }
            extra_arguments = {}

        def pre_resolve(*args, **kwargs):
            return (*args, kwargs)

        def resolve(*args, **kwargs):
            return "object_read"

        def override_total_resolve(*args, **kwargs):
            return "object_read"

        def post_resolve(*args, **kwargs):
            return "object_read"

    class UpdateField:
        class Meta:
            modify_input_argument = {
                "name": "input",
                "required": True,
                "description": "",
                "hidden": False,
            }
            extra_arguments = {}

        def pre_mutate(*args, **kwargs):
            return (*args, kwargs)

        def mutate(*args, **kwargs):
            return "object_update"

        def override_total_mutate(*args, **kwargs):
            return "object_update"

        def post_mutate(*args, **kwargs):
            return "object_update"

    class DeleteField:
        class Meta:
            modify_where_argument = {
                "name": "where",
                "required": True,
                "description": "",
                "hidden": False,
            }
            extra_arguments = {}

        def pre_mutate(*args, **kwargs):
            return (*args, kwargs)

        def mutate(*args, **kwargs):
            return "object_read"

        def override_total_mutate(*args, **kwargs):
            return "object_read"

        def post_mutate(*args, **kwargs):
            return "object_read"

    class DeactivateField:
        class Meta:
            modify_where_argument = {
                "name": "where",
                "required": True,
                "description": "",
                "hidden": False,
            }
            extra_arguments = {}

        def pre_mutate(*args, **kwargs):
            return (*args, kwargs)

        def mutate(*args, **kwargs):
            return "list_objects_deactivates"

        def override_total_mutate(*args, **kwargs):
            return "list_objects_deactivates"

        def post_mutate(*args, **kwargs):
            return "list_objects_deactivates"

    class ActivateField:
        class Meta:
            modify_where_argument = {
                "name": "where",
                "required": True,
                "description": "",
                "hidden": False,
            }
            extra_arguments = {}

        def pre_mutate(*args, **kwargs):
            return (*args, kwargs)

        def mutate(*args, **kwargs):
            return "list_objects_actives"

        def override_total_mutate(*args, **kwargs):
            return "list_objects_actives"

        def post_mutate(*args, **kwargs):
            return "list_objects_actives"

    class ListField:
        class Meta:
            modify_order_by_argument = {
                "name": "orderBy",
                "required": False,
                "description": "",
                "hidden": False,
            }
            modify_pagination_config_argument = {
                "name": "paginated",
                "required": False,
                "description": "",
                "hidden": False,
            }
            extra_arguments = {}

        def pre_resolve(*args, **kwargs):
            return (*args, kwargs)

        def resolve(*args, **kwargs):
            return "paginated_objects"

        def override_total_resolve(*args, **kwargs):
            return "paginated_objects"

        def post_resolve(*args, **kwargs):
            return "paginated_objects"

    class SearchField:
        class Meta:
            modify_where_argument = {
                "name": "where",
                "required": False,
                "description": "",
                "hidden": False,
            }
            modify_order_by_argument = {
                "name": "orderBy",
                "required": False,
                "description": "",
                "hidden": False,
            }
            modify_pagination_config_argument = {
                "name": "paginated",
                "required": False,
                "description": "",
                "hidden": False,
            }
            extra_arguments = {}

        def pre_resolve(*args, **kwargs):
            return (*args, kwargs)

        def resolve(*args, **kwargs):
            return "paginated_objects"

        def override_total_resolve(*args, **kwargs):
            return "paginated_objects"

        def post_resolve(*args, **kwargs):
            return "paginated_objects"

```