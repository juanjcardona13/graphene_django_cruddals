```python
""" GraphQL Field
  Describes one discrete piece of information available to request within a selection set.
  All Graphql Field have:

    - type (ObjectType, ScalarType, Enum, Interface, Union): The graphql type of the field
    - arguments (Dict[str, Argument]): Arguments that can be input to the field.
    - resolver (Callable): A function to get the value for a Field from the parent value object. If not set, the default resolver method for the schema is used.

    - deprecation_reason (str): The reason why the field is deprecated
    - required (bool): If the field is required
    - name (str): The name of the GraphQL field (must be unique in a type)
    - description (str): The description of the field
    - default_value (Any): The default value of the field
"""

""" GraphQL Input Field
  A special type of field, it is special because is only found in InputObjectType.
  All Graphql Input Field have:

    - type (InputObjectType, ScalarType, Enum): The graphql type of the input field
    - name (str): The name of the GraphQL input field (must be unique in a type)
    - default_value (Any): Default value to use as input if none set in user operation ( query, mutation, etc.).
    - deprecation_reason (str): The reason why the input field is deprecated
    - description (str): The description of the input field
    - required (bool): If the input field is required
"""

""" GraphQL Argument
  An additional piece of information used to customize the resolution of a field. Arguments are passed to resolvers to modify or specify the data to be returned.
  All Graphql Argument have:

    - type (InputObjectType, ScalarType, Enum): The graphql type of the argument
    - name (str): The name of the GraphQL argument (must be unique in a type)
    - default_value (Any): Default value to use if none set in user operation ( query, mutation, etc.).
    - deprecation_reason (str): The reason why the argument is deprecated
    - description (str): The description of the argument
    - required (bool): If the argument is required
"""

""" Graphql InputObjectType
  A special type in GraphQL that groups multiple input fields to send them as a single argument.
  All Graphql InputObjectType have:

    - name (str): The name of the InputObjectType
    - description (str): The description of the InputObjectType
    - input_fields (Dict[str, InputField]): The input fields of the InputObjectType
"""

""" GraphQL ObjectType
  Is a type in the GraphQL schema that groups multiple fields to represent a single object.
  ObjectTypes have a name, but most importantly describe their fields.

  All Graphql ObjectType have:

    - name (str): The name of the ObjectType
    - fields (Dict[str, Field]): The fields of the ObjectType
    - interfaces (List[Interface]): The interfaces that the ObjectType implements
    - description (str): The description of the ObjectType
"""

""" GraphQL Scalar
  Is a primitive type that can represent a leaf value.
  All Graphql Scalar have:

    - name (str): The name of the Scalar
    - description (str): The description of the Scalar
"""

""" GraphQL Schema
  Is at the core of any GraphQL server implementation. It represents the data model that a client can query.
  All Graphql Schema have:

    - query (ObjectType): The root query ObjectType of the schema
    - mutation (ObjectType): The root mutation ObjectType of the schema
    - subscription (ObjectType): The root subscription ObjectType of the schema
    - types (List[Union, Interface, ObjectType, Scalar, Enum]): The types of the schema
    - directives (List[Directive]): The directives of the schema
    - description (str): The description of the schema
"""




class ExampleModelInterface:

    class ObjectType:
      """
        This is the class that will be used to modify the ObjectType of the model.
        Like all graphql ObjectType, this is a objectType with all options that a ObjectType can have
        The special thing about this ObjectType is that it is created automatically by CRUDDALS, and it will have the fields of the model

        - Name: The name of the ObjectType will be `{ModelName}Type`
        - Fields: The fields of the ObjectType will be the fields of the model
          The fields build for default to the ObjectType can be modified of 3 ways:
            - `only_fields` attribute in the `Meta` class of the `ObjectType` class, where you can put a tuple of str or "__all__" to include only the fields that you want
            - `exclude_fields` attribute in the `Meta` class of the `ObjectType` class, where you can put a tuple of str to exclude the fields that you want
            - Modify the fields directly in the `ObjectType` class, where you can add new fields, modify the resolvers, or modify the type of the fields
          For add new custom fields, you can add a new field with the name of the field and the type of the field (any attribute of the class that is of type GRAPHENE TYPE will be a field), and you can add a resolver for the field with the name `resolve_{field_name}` (any method of the class that starts with `resolve_` and match with the name of the field will be a resolver for the field)
        - Interfaces: Not used and for the moment cannot be overwritten - TODO
        - Description: Not used and for the moment cannot be overwritten - TODO

        Exist a special method that can be used to modify the objects returned before it is returned, this method is `get_objects` and is a class method that have 3 arguments (root, objects, info), where `root` is the root object that contains the ObjectType, `objects` is the objects that will be returned, and `info` is the info object that contains the context of the request
        You can intercept the exact moment when the ObjectType is resolved by using the `get_objects` method, this method always will be called before the ObjectType is resolved, and you can modify the response before it is returned
      """

        class Meta: # This is the class that will be used to modify the Meta class of the ObjectType
            only_fields = "__all__" # Tuple of str or "__all__"
            exclude_fields = () # Tuple of str

        new_field = graphene.String() # Graphene => Scalar, String, ID, Int, Float, Boolean, Date, DateTime, Time, Decimal, JSONString, UUID, List, NonNull, Enum, Argument, Dynamic

        def resolve_new_field(self, info): # Resolver for new_field should be a function with the same name as the field prefixed by "resolve_" and receive 2 arguments (self, info), return the value of the field same type as the field
            return "new_field"

        # another fields with their resolvers

        @classmethod
        def get_objects(cls, objects, info):
            return objects

    class InputObjectType:
      """
        This is the class that will be used to modify the InputObjectType of the model.
        Like all graphql InputObjectType, this is a InputObjectType with all options that a InputObjectType can have
        The special thing about this InputObjectType is that it is created automatically by CRUDDALS, and it will have the fields editables of the model
        This inputObjectType will have the `id` field optional

        - Name: The name of the InputObjectType will be `{ModelName}Input`
        - InputFields: The input fields of the InputObjectType will be the fields editables of the model
          The InputFields build for default to the InputObjectType can be modified of 3 ways:
            - `only_fields` attribute in the `Meta` class of the `InputObjectType` class, where you can put a tuple of str or "__all__" to include only the fields that you want
            - `exclude_fields` attribute in the `Meta` class of the `InputObjectType` class, where you can put a tuple of str to exclude the fields that you want
            - Modify the fields directly in the `InputObjectType` class, where you can add new fields, modify the resolvers, or modify the type of the fields
          For add new custom fields, you can add a new field with the name of the field and the type of the field (any attribute of the class that is of type GRAPHENE TYPE will be a field), and you can add a resolver for the field with the name `resolve_{field_name}` (any method of the class that starts
      """
        class Meta:
            only_fields = "__all__"
            exclude_fields = ()
            #(deprecated)hold_required_in_fields = False  # Podría ser también reemplazar esto por required_fields = "__all__" y not_required_fields = ()

        new_field = graphene.String()
        # exist_field = CruddalsRelationField() => For relations

        # Implícitamente si pone un campo que ya estaba en el ModelInputObjectType, sera sobrescrito por el que ponga de ultimo
        # y ya todos los otros nuevos serán nuevos campos como tal

    class CreateInputObjectType:
      """
        This is the class that will be used to modify the CreateInputObjectType of the model.
        Like all graphql InputObjectType, this is a InputObjectType with all options that a InputObjectType can have
        The special thing about this CreateInputObjectType is that it is created automatically by CRUDDALS, and it will have the fields editables of the model
        This inputObjectType never will have the `id` field

        - Name: The name of the InputObjectType will be `Create{ModelName}Input`
        - InputFields: The input fields of the InputObjectType will be the fields editables of the model
          The InputFields build for default to the InputObjectType can be modified of 3 ways:
            - `only_fields` attribute in the `Meta` class of the `InputObjectType` class, where you can put a tuple of str or "__all__" to include only the fields that you want
            - `exclude_fields` attribute in the `Meta` class of the `InputObjectType` class, where you can put a tuple of str to exclude the fields that you want
            - Modify the fields directly in the `InputObjectType` class, where you can add new fields, modify the resolvers, or modify the type of the fields
          For add new custom fields, you can add a new field with the name of the field and the type of the field (any attribute of the class that is of type GRAPHENE TYPE will be a field), and you can add a resolver for the field with the name `resolve_{field_name}` (any method of the class that starts with `resolve_` and match with the name of the field will be a resolver for the field)
      """

        class Meta:
            only_fields = "__all__"
            exclude_fields = ()
            #(deprecated)hold_required_in_fields = False  # Podría ser también reemplazar esto por required_fields = "__all__" y not_required_fields = ()

        new_field = graphene.String()
        # exist_field = CruddalsRelationField() => For relations

        # Implícitamente si pone un campo que ya estaba en el ModelInputObjectType, sera sobrescrito por el que ponga de ultimo
        # y ya todos los otros nuevos serán nuevos campos como tal

    class UpdateInputObjectType:
      """
        This is the class that will be used to modify the UpdateInputObjectType of the model.
        Like all graphql InputObjectType, this is a InputObjectType with all options that a InputObjectType can have
        The special thing about this UpdateInputObjectType is that it is created automatically by CRUDDALS, and it will have the fields editables of the model
        This inputObjectType will have the `id` field required

        - Name: The name of the InputObjectType will be `Update{ModelName}Input`
        - InputFields: The input fields of the InputObjectType will be the fields editables of the model
          The InputFields build for default to the InputObjectType can be modified of 3 ways:
            - `only_fields` attribute in the `Meta` class of the `InputObjectType` class, where you can put a tuple of str or "__all__" to include only the fields that you want
            - `exclude_fields` attribute in the `Meta` class of the `InputObjectType` class, where you can put a tuple of str to exclude the fields that you want
            - Modify the fields directly in the `InputObjectType` class, where you can add new fields, modify the resolvers, or modify the type of the fields
          For add new custom fields, you can add a new field with the name of the field and the type of the field (any attribute of the class that is of type GRAPHENE TYPE will be a field), and you can add a resolver for the field with the name `resolve_{field_name}` (any method of the class that starts with `resolve_` and match with the name of the field will be a resolver for the field)
      """
        class Meta:
            only_fields = "__all__"
            exclude_fields = ()
            #(deprecated)hold_required_in_fields = False  # Podría ser también reemplazar esto por required_fields = "__all__" y not_required_fields = ()

        new_field = graphene.String()
        # exist_field = CruddalsRelationField() => For relations

        # Implícitamente si pone un campo que ya estaba en el ModelInputObjectType, sera sobrescrito por el que ponga de ultimo
        # y ya todos los otros nuevos serán nuevos campos como tal

    class FilterInputObjectType:
      """
        This is the class that will be used to modify the FilterInputObjectType of the model.
        Like all graphql InputObjectType, this is a InputObjectType with all options that a InputObjectType can have
        The special thing about this FilterInputObjectType is that it is created automatically by CRUDDALS, and it will have the fields of the model converted to filters

        - Name: The name of the InputObjectType will be `Filter{ModelName}Input`
        - InputFields: The input fields of the InputObjectType will be the fields of the model converted to filters
          The InputFields build for default to the InputObjectType can be modified of 3 ways:
            - `only_fields` attribute in the `Meta` class of the `InputObjectType` class, where you can put a tuple of str or "__all__" to include only the fields that you want
            - `exclude_fields` attribute in the `Meta` class of the `InputObjectType` class, where you can put a tuple of str to exclude the fields that you want
            - Modify the fields directly in the `InputObjectType` class, where you can add new fields, modify the resolvers, or modify the type of the fields
          For add new custom fields, you can add a new field with the name of the field and the type of the field (any attribute of the class that is of type GRAPHENE TYPE will be a field), and you can add a resolver for the field with the name `resolve_{field_name}` (any method of the class that starts with `resolve_` and match with the name of the field will be a resolver for the field)
      """
        class Meta:
            only_fields = "__all__"
            exclude_fields = ()

        new_field = graphene.String()

        # Implícitamente si pone un campo que ya estaba en el ModelInputObjectType, sera sobrescrito por el que ponga de ultimo
        # y ya todos los otros nuevos serán nuevos campos como tal

    class OrderByInputObjectType:
      """
        This is the class that will be used to modify the OrderByInputObjectType of the model.
        Like all graphql InputObjectType, this is a InputObjectType with all options that a InputObjectType can have
        The special thing about this OrderByInputObjectType is that it is created automatically by CRUDDALS, and it will have the fields of the model converted to order by

        - Name: The name of the InputObjectType will be `OrderBy{ModelName}Input`
        - InputFields: The input fields of the InputObjectType will be the fields of the model converted to order by
          The InputFields build for default to the InputObjectType can be modified of 3 ways:
            - `only_fields` attribute in the `Meta` class of the `InputObjectType` class, where you can put a tuple of str or "__all__" to include only the fields that you want
            - `exclude_fields` attribute in the `Meta` class of the `InputObjectType` class, where you can put a tuple of str to exclude the fields that you want
            - Modify the fields directly in the `InputObjectType` class, where you can add new fields, modify the resolvers, or modify the type of the fields
          For add new custom fields, you can add a new field with the name of the field and the type of the field (any attribute of the class that is of type GRAPHENE TYPE will be a field), and you can add a resolver for the field with the name `resolve_{field_name}` (any method of the class that starts with `resolve_` and match with the name of the field will be a resolver for the field)
      """
        class Meta:
            only_fields = "__all__"
            exclude_fields = ()

        new_field = graphene.String()

        # Implícitamente si pone un campo que ya estaba en el ModelInputObjectType, sera sobrescrito por el que ponga de ultimo
        # y ya todos los otros nuevos serán nuevos campos como tal


    class ModelCreateField:
      """
        Like all graphql fields, this is a field with all options that a field can have
        The only difference is that this field is used to create objects

        - Name: The name of the field will be `create{ModelNamePluralized}`
        - Type: It will always be `Create{ModelNamePluralized}Payload`
          `Create{ModelNamePluralized}Payload` is a ObjectType that will be created automatically by CRUDDALS, and it will have the following fields:
            - `objects`: Graphene.List of the ObjectType of the model
            - `errorsReport`: Graphene.List of the ErrorCollectionType
          This type cannot be modified, but the type for List the `objects` can be modified through the `ObjectType` class

        - Arguments: Automatically have 1 argument called `input` that is a List of InputObjectType with the name `Create{ModelName}Input`
          `Create{ModelName}Input` is a InputObjectType that will be created automatically by CRUDDALS, where the input fields are the fields of the model
          The `input` argument cannot be modified, but the type for the `Create{ModelName}Input` can be modified through the `CreateInputObjectType` class
          additional arguments can be added through the `extra_arguments` attribute of the `Meta` class in the `ModelCreateField` class

        - Resolver: The resolver will be created automatically by CRUDDALS, and it will receive 3 arguments (root, info, input), and it will return a dict with the keys `objects` and `errorsReport`
          The `default_resolver` can be modified totally add a new resolver with the name `override_total_mutate` how class method in the `ModelCreateField` class,
          or modify the resolver before or after the mutation with the names `pre_mutate` and `post_mutate` how classes methods in the `ModelCreateField` class
          or additionally, allow enter to CRUDDALS but control for the user with the name `mutate`, (This is special because allow override the mutation but also call the pre and post mutate, or other mutations in other interfaces) how class method in the `ModelCreateField` class

        - Deprecation Reason: Not used and for the moment cannot be overwritten - TODO
        - Required: Not used and for the moment cannot be overwritten - TODO
        - Description: Not used and for the moment cannot be overwritten - TODO
        - Default Value: Not used and for the moment cannot be overwritten - TODO
      """

        class Meta:
            # For modify the input argument, only can modify the InputObjectType through the CreateInputObjectType
            extra_arguments = {
              # "key": str (used how name), "value": graphene.Argument
            } # This dict add new arguments to the mutation

        def pre_mutate(*args, **kwargs):
            return (*args, kwargs)

        def mutate(*args, **kwargs):
            return "object_create"

        def override_total_mutate(*args, **kwargs):
            return "object_create"

        def post_mutate(*args, **kwargs):
            return "object_create"

    class ModelReadField:
      """
        Like all graphql fields, this is a field with all options that a field can have
        The only difference is that this field is used to get only one object (read object)

        - Name: The name of the field will be `read{ModelName}`
        - Type: It will always be `{ModelName}Type`
          `{ModelName}Type` is a ObjectType that will be created automatically by CRUDDALS, and it will have the fields of the model
          This type cannot be modified here directly, but the type can be modified through the `ObjectType` class

        - Arguments: Automatically have 1 argument called `where` that is a InputObjectType with the name `Filter{ModelName}Input`
          `Filter{ModelName}Input` is a InputObjectType that will be created automatically by CRUDDALS, where the input fields are the fields of the model converted to filters
          The `where` argument cannot be modified, but the type for the `Filter{ModelName}Input` can be modified through the `FilterInputObjectType` class
          additional arguments can be added through the `extra_arguments` attribute of the `Meta` class in the `ModelReadField` class

        - Resolver: The resolver will be created automatically by CRUDDALS, and it will receive 3 arguments (root, info, where), and it will return the object
          The `default_resolver` can be modified totally add a new resolver with the name `override_total_resolve` how class method in the `ModelReadField` class,
          or modify the resolver before or after the mutation with the names `pre_resolve` and `post_resolve` how classes methods in the `ModelReadField` class
          or additionally, allow enter to CRUDDALS but control for the user with the name `resolve`, (This is special because allow override the mutation but also call the pre and post resolve, or other mutations in other interfaces) how class method in the `ModelReadField` class

        - Deprecation Reason: Not used and for the moment cannot be overwritten - TODO
        - Required: Not used and for the moment cannot be overwritten - TODO
        - Description: Not used and for the moment cannot be overwritten - TODO
        - Default Value: Not used and for the moment cannot be overwritten - TODO
      """

        class Meta:
            extra_arguments = {}

        def pre_resolve(*args, **kwargs):
            return (*args, kwargs)

        def resolve(*args, **kwargs):
            return "object_read"

        def override_total_resolve(*args, **kwargs):
            return "object_read"

        def post_resolve(*args, **kwargs):
            return "object_read"

    class ModelUpdateField:
      """
        Like all graphql fields, this is a field with all options that a field can have
        The only difference is that this field is used to update objects

        - Name: The name of the field will be `update{ModelNamePluralized}`
        - Type: It will always be `Update{ModelNamePluralized}Payload`
          `Update{ModelNamePluralized}Payload` is a ObjectType that will be created automatically by CRUDDALS, and it will have the following fields:
            - `objects`: Graphene.List of the ObjectType of the model
            - `errorsReport`: Graphene.List of the ErrorCollectionType
          This type cannot be modified, but the type for List the `objects` can be modified through the `ObjectType` class

        - Arguments: Automatically have 1 argument called `input` that is a List of InputObjectType with the name `Update{ModelName}Input`
          `Update{ModelName}Input` is a InputObjectType that will be created automatically by CRUDDALS, where the input fields are the fields of the model
          The `input` argument cannot be modified, but the type for the `Update{ModelName}Input` can be modified through the `CreateInputObjectType` class
          additional arguments can be added through the `extra_arguments` attribute of the `Meta` class in the `ModelCreateField` class

        - Resolver: The resolver will be created automatically by CRUDDALS, and it will receive 3 arguments (root, info, input), and it will return a dict with the keys `objects` and `errorsReport`
          The `default_resolver` can be modified totally add a new resolver with the name `override_total_mutate` how class method in the `ModelCreateField` class,
          or modify the resolver before or after the mutation with the names `pre_mutate` and `post_mutate` how classes methods in the `ModelCreateField` class
          or additionally, allow enter to CRUDDALS but control for the user with the name `mutate`, (This is special because allow override the mutation but also call the pre and post mutate, or other mutations in other interfaces) how class method in the `ModelCreateField` class

        - Deprecation Reason: Not used and for the moment cannot be overwritten - TODO
        - Required: Not used and for the moment cannot be overwritten - TODO
        - Description: Not used and for the moment cannot be overwritten - TODO
        - Default Value: Not used and for the moment cannot be overwritten - TODO
      """

        class Meta:
            # For modify the input argument, only can modify the InputObjectType through the CreateInputObjectType
            extra_arguments = {
              # "key": str (used how name), "value": graphene.Argument
            } # This dict add new arguments to the mutation

        def pre_mutate(*args, **kwargs):
            return (*args, kwargs)

        def mutate(*args, **kwargs):
            return "object_update"

        def override_total_mutate(*args, **kwargs):
            return "object_update"

        def post_mutate(*args, **kwargs):
            return "object_update"

    class ModelDeleteField:
      """
        Like all graphql fields, this is a field with all options that a field can have
        The only difference is that this field is used to delete objects

        - Name: The name of the field will be `delete{ModelNamePluralized}`
        - Type: It will always be `Delete{ModelNamePluralized}Payload`
          `Delete{ModelNamePluralized}Payload` is a ObjectType that will be created automatically by CRUDDALS, and it will have the following fields:
            - `objects`: Graphene.List of the ObjectType of the model
            - `errorsReport`: Graphene.List of the ErrorCollectionType
            - `success`: Graphene.Boolean
          This type cannot be modified, but the type for List the `objects` can be modified through the `ObjectType` class

        - Arguments: Automatically have 1 argument called `where` that is a InputObjectType with the name `Filter{ModelName}Input`
          `Filter{ModelName}Input` is a InputObjectType that will be created automatically by CRUDDALS, where the input fields are the fields of the model converted to filters
          The `where` argument cannot be modified, but the type for the `Filter{ModelName}Input` can be modified through the `FilterInputObjectType` class
          additional arguments can be added through the `extra_arguments` attribute of the `Meta` class in the `ModelDeleteField` class

        - Resolver: The resolver will be created automatically by CRUDDALS, and it will receive 3 arguments (root, info, where), and it will return a dict with the keys `objects`, `errorsReport` and `success`
          The `default_resolver` can be modified totally add a new resolver with the name `override_total_mutate` how class method in the `ModelDeleteField` class,
          or modify the resolver before or after the mutation with the names `pre_mutate` and `post_mutate` how classes methods in the `ModelDeleteField` class
          or additionally, allow enter to CRUDDALS but control for the user with the name `mutate`, (This is special because allow override the mutation but also call the pre and post mutate, or other mutations in other interfaces) how class method in the `ModelDeleteField` class

        - Deprecation Reason: Not used and for the moment cannot be overwritten - TODO
        - Required: Not used and for the moment cannot be overwritten - TODO
        - Description: Not used and for the moment cannot be overwritten - TODO
        - Default Value: Not used and for the moment cannot be overwritten - TODO
      """

        class Meta:
            extra_arguments = {}

        def pre_mutate(*args, **kwargs):
            return (*args, kwargs)

        def mutate(*args, **kwargs):
            return "object_read"

        def override_total_mutate(*args, **kwargs):
            return "object_read"

        def post_mutate(*args, **kwargs):
            return "object_read"

    class ModelDeactivateField:
      """
        Like all graphql fields, this is a field with all options that a field can have
        The only difference is that this field is used to deactivate objects

        - Name: The name of the field will be `deactivate{ModelNamePluralized}`
        - Type: It will always be `Deactivate{ModelNamePluralized}Payload`
          `Deactivate{ModelNamePluralized}Payload` is a ObjectType that will be created automatically by CRUDDALS, and it will have the following fields:
            - `objects`: Graphene.List of the ObjectType of the model
            - `errorsReport`: Graphene.List of the ErrorCollectionType
            - `success`: Graphene.Boolean
          This type cannot be modified, but the type for List the `objects` can be modified through the `ObjectType` class

        - Arguments: Automatically have 1 argument called `where` that is a InputObjectType with the name `Filter{ModelName}Input`
          `Filter{ModelName}Input` is a InputObjectType that will be created automatically by CRUDDALS, where the input fields are the fields of the model converted to filters
          The `where` argument cannot be modified, but the type for the `Filter{ModelName}Input` can be modified through the `FilterInputObjectType` class
          additional arguments can be added through the `extra_arguments` attribute of the `Meta` class in the `ModelDeactivateField` class

        - Resolver: The resolver will be created automatically by CRUDDALS, and it will receive 3 arguments (root, info, where), and it will return a dict with the keys `objects`, `errorsReport` and `success`
          The `default_resolver` can be modified totally add a new resolver with the name `override_total_mutate` how class method in the `ModelDeactivateField` class,
          or modify the resolver before or after the mutation with the names `pre_mutate` and `post_mutate` how classes methods in the `ModelDeactivateField` class
          or additionally, allow enter to CRUDDALS but control for the user with the name `mutate`, (This is special because allow override the mutation but also call the pre and post mutate, or other mutations in other interfaces) how class method in the `ModelDeactivateField` class

        - Deprecation Reason: Not used and for the moment cannot be overwritten - TODO
        - Required: Not used and for the moment cannot be overwritten - TODO
        - Description: Not used and for the moment cannot be overwritten - TODO
        - Default Value: Not used and for the moment cannot be overwritten - TODO
      """

        class Meta:
            extra_arguments = {}

        def pre_mutate(*args, **kwargs):
            return (*args, kwargs)

        def mutate(*args, **kwargs):
            return "list_objects_deactivates"

        def override_total_mutate(*args, **kwargs):
            return "list_objects_deactivates"

        def post_mutate(*args, **kwargs):
            return "list_objects_deactivates"

    class ModelActivateField:
      """
        Like all graphql fields, this is a field with all options that a field can have
        The only difference is that this field is used to activate objects

        - Name: The name of the field will be `activate{ModelNamePluralized}`
        - Type: It will always be `Activate{ModelNamePluralized}Payload`
          `Activate{ModelNamePluralized}Payload` is a ObjectType that will be created automatically by CRUDDALS, and it will have the following fields:
            - `objects`: Graphene.List of the ObjectType of the model
            - `errorsReport`: Graphene.List of the ErrorCollectionType
            - `success`: Graphene.Boolean
          This type cannot be modified, but the type for List the `objects` can be modified through the `ObjectType` class

        - Arguments: Automatically have 1 argument called `where` that is a InputObjectType with the name `Filter{ModelName}Input`
          `Filter{ModelName}Input` is a InputObjectType that will be created automatically by CRUDDALS, where the input fields are the fields of the model converted to filters
          The `where` argument cannot be modified, but the type for the `Filter{ModelName}Input` can be modified through the `FilterInputObjectType` class
          additional arguments can be added through the `extra_arguments` attribute of the `Meta` class in the `ModelActivateField` class

        - Resolver: The resolver will be created automatically by CRUDDALS, and it will receive 3 arguments (root, info, where), and it will return a dict with the keys `objects`, `errorsReport` and `success`
          The `default_resolver` can be modified totally add a new resolver with the name `override_total_mutate` how class method in the `ModelActivateField` class,
          or modify the resolver before or after the mutation with the names `pre_mutate` and `post_mutate` how classes methods in the `ModelActivateField` class
          or additionally, allow enter to CRUDDALS but control for the user with the name `mutate`, (This is special because allow override the mutation but also call the pre and post mutate, or other mutations in other interfaces) how class method in the `ModelActivateField` class

        - Deprecation Reason: Not used and for the moment cannot be overwritten - TODO
        - Required: Not used and for the moment cannot be overwritten - TODO
        - Description: Not used and for the moment cannot be overwritten - TODO
        - Default Value: Not used and for the moment cannot be overwritten - TODO
      """
        class Meta:
            extra_arguments = {}

        def pre_mutate(*args, **kwargs):
            return (*args, kwargs)

        def mutate(*args, **kwargs):
            return "list_objects_actives"

        def override_total_mutate(*args, **kwargs):
            return "list_objects_actives"

        def post_mutate(*args, **kwargs):
            return "list_objects_actives"

    class ModelListField:
      """
        Like all graphql fields, this is a field with all options that a field can have
        The only difference is that this field is used to list objects

        - Name: The name of the field will be `list{ModelNamePluralized}`
        - Type: It will always be a List of the ObjectType of the model
          This type cannot be modified, but the type for List the `objects` can be modified through the `ObjectType` class

        - Arguments: This field not have arguments for default, but additional arguments can be added through the `extra_arguments` attribute of the `Meta` class in the `ModelListField` class

        - Resolver: The resolver will be created automatically by CRUDDALS, and it will receive 3 arguments (root, info), and it will return a list of objects
          The `default_resolver` can be modified totally add a new resolver with the name `override_total_resolve` how class method in the `ModelListField` class,
          or modify the resolver before or after the mutation with the names `pre_resolve` and `post_resolve` how classes methods in the `ModelListField` class
          or additionally, allow enter to CRUDDALS but control for the user with the name `resolve`, (This is special because allow override the mutation but also call the pre and post resolve, or other mutations in other interfaces) how class method in the `ModelListField` class

        - Deprecation Reason: Not used and for the moment cannot be overwritten - TODO
        - Required: Not used and for the moment cannot be overwritten - TODO
        - Description: Not used and for the moment cannot be overwritten - TODO
        - Default Value: Not used and for the moment cannot be overwritten - TODO
      """
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

    class ModelSearchField:
      """
        Like all graphql fields, this is a field with all options that a field can have
        The only difference is that this field is used to search objects

        - Name: The name of the field will be `search{ModelNamePluralized}`
        - Type: It will always be a `{ModelName}PaginatedType`
          `{ModelName}PaginatedType` is a ObjectType that will be created automatically by CRUDDALS, and it will have the following fields:
            - `objects`: Graphene.List of the ObjectType of the model
            - `total`: Graphene.Int
            - `page`: Graphene.Int
            - `pages`: Graphene.Int
            - `hasNext`: Graphene.Boolean
            - `hasPrev`: Graphene.Boolean
            - `indexStart`: Graphene.Int
            - `indexEnd`: Graphene.Int
          This type cannot be modified, but the type for List the `objects` can be modified through the `ObjectType` class

        - Arguments: Automatically have 3 arguments called `where`, `orderBy` and `paginationConfig` that are InputObjectType with the names `Filter{ModelName}Input`, `OrderBy{ModelName}Input` and `PaginationConfigInput`
          `Filter{ModelName}Input` is a InputObjectType that will be created automatically by CRUDDALS, where the input fields are the fields of the model converted to filters
          `OrderBy{ModelName}Input` is a InputObjectType that will be created automatically by CRUDDALS, where the input fields are the fields of the model converted to order by
          `PaginationConfigInput` is a InputObjectType that will be created automatically by CRUDDALS, where have 2 input fields `page` and `itemsPerPage`
          The `where`, `orderBy` and `paginated` arguments cannot be modified, but the type for the `Filter{ModelName}Input`, `OrderBy{ModelName}Input` can be modified through the `FilterInputObjectType` and `OrderByInputObjectType` classes
          additional arguments can be added through the `extra_arguments` attribute of the `Meta` class in the `ModelSearchField` class

        - Resolver: The resolver will be created automatically by CRUDDALS, and it will receive 3 arguments (root, info, where, orderBy, paginationConfig), and it will return a dict with the keys `objects`, `total`, `page`, `pages`, `hasNext`, `hasPrev`, `indexStart` and `indexEnd`
          The `default_resolver` can be modified totally add a new resolver with the name `override_total_resolve` how class method in the `ModelSearchField` class,
          or modify the resolver before or after the mutation with the names `pre_resolve` and `post_resolve` how classes methods in the `ModelSearchField` class
          or additionally, allow enter to CRUDDALS but control for the user with the name `resolve`, (This is special because allow override the mutation but also call the pre and post resolve, or other mutations in other interfaces) how class method in the `ModelSearchField` class

        - Deprecation Reason: Not used and for the moment cannot be overwritten - TODO
        - Required: Not used and for the moment cannot be overwritten - TODO
        - Description: Not used and for the moment cannot be overwritten - TODO
        - Default Value: Not used and for the moment cannot be overwritten - TODO
      """

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

```
