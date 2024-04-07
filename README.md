

<h1 align="center">Graphene-Django-CRUDDALS</h1>
<div align="center">

👩🏽‍💻 🚀 👨🏽‍💻  
**Framework for trivial code, easy and fast to learn and use.**  
Turn your Django-models into a complete GraphQL API with all CRUD operations  

[![PyPI](https://img.shields.io/pypi/v/graphene-django-cruddals?style=flat-&color=00559c&label=pypi&logo=python&logoColor=white)](https://pypi.org/project/graphene-django-cruddals/)
[![GitHub License](https://img.shields.io/github/license/juanjcardona13/graphene_django_cruddals?style=flat&color=4c1)](https://github.com/juanjcardona13/graphene_django_cruddals/blob/main/LICENSE)


**[Docs](https://graphene-django-cruddals.readthedocs.io/en/latest/) |...|...|**

<sub>Built with ❤︎ by [Juan J Cardona](https://github.com/juanjcardona13) and [contributors](https://github.com/juanjcardona13/graphene_django_cruddals/graphs/contributors) 
</sub>
</div>

## 📋 Table of Contents

1. 🚀 [Getting started](#getting-started)
2. 👩‍💻 [Usage](#usage)
3. 🎁 [Features](#features)
4. 📚 [Documentation](#documentation)
5. 📜 [License](#license)
6. ❤️ [Contributing](#contributing)
7. 📞 [Contact](#contact)
8. 🙏 [Acknowledgements](#acknowledgements)
9. 🗺️ [Roadmap](#roadmap)


## <a name="getting-started">🚀 Getting started</a>

### Prerequisites

To install this project you need to have a Django project already set up. If you don't have one, you can follow the [official Django tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/).

### Installation

You can install this package using pip:

```bash
pip install graphene-django-cruddals
```

## <a name="usage">👩‍💻 Usage</a> 

To use it, simply create a new class that inherits "`CruddalsModel`"
Suppose we have the following models.

```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

Then we can create a complete CRUD+DALS for the models `Question` with the following code

```python
class CruddalsQuestion(CruddalsModel):
    class Meta:
        model = Question
```

Now you can use the `schema` that was generated for you,

```python
schema = CruddalsQuestion.Schema
```

or use in your existing schema root `Query` and `Mutation`

```python
class Query(
    # ... your others queries
    CruddalsQuestion.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    # ... your others mutations
    CruddalsQuestion.Mutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema( query=Query, mutation=Mutation, )
```

your schema will have the following queries and mutations

<details>
<summary>Click to see the generated schema</summary>

```graphql
# Queries
type Query {
  readQuestion(where: FilterQuestionInput!): QuestionType
  searchQuestions(where: FilterQuestionInput, orderBy: OrderByQuestionInput, paginated: PaginationConfigInput): QuestionPaginatedType
  listQuestions: [QuestionType!]
}

# Mutations
type Mutation {
  createQuestions(input: [CreateQuestionInput!]): CreateQuestionsPayload
  updateQuestions(input: [UpdateQuestionInput!]): UpdateQuestionsPayload
  activateQuestions(where: FilterQuestionInput!): ActivateQuestionsPayload
  deactivateQuestions(where: FilterQuestionInput!): DeactivateQuestionsPayload
  deleteQuestions(where: FilterQuestionInput!): DeleteQuestionsPayload
}


# Inputs
# - From the model: Question
input CreateQuestionInput {
  questionText: String!
  pubDate: DateTime!
}
input UpdateQuestionInput {
  id: ID!
  questionText: String
  pubDate: DateTime
}
input FilterQuestionInput {
  id: IDFilter
  questionText: StringFilter
  pubDate: DateTimeFilter
  AND: [FilterQuestionInput]
  OR: [FilterQuestionInput]
  NOT: FilterQuestionInput
}
input OrderByQuestionInput {
  id: OrderEnum
  questionText: OrderStringEnum
  pubDate: OrderEnum
}
# - Filters
input IDFilter {
  exact: ID
  iexact: ID
  gt: ID
  gte: ID
  lt: ID
  lte: ID
  in: [ID]
  contains: ID
  icontains: ID
  startswith: ID
  istartswith: ID
  endswith: ID
  iendswith: ID
  range: [ID]
  isnull: Boolean
  regex: String
  iregex: String
  containedBy: ID
}
input StringFilter {
  exact: String
  iexact: String
  gt: String
  gte: String
  lt: String
  lte: String
  in: [String]
  contains: String
  icontains: String
  startswith: String
  istartswith: String
  endswith: String
  iendswith: String
  range: [String]
  isnull: Boolean
  regex: String
  iregex: String
}
input DateTimeFilter {
  exact: DateTime
  iexact: DateTime
  gt: DateTime
  gte: DateTime
  lt: DateTime
  lte: DateTime
  in: [DateTime]
  contains: DateTime
  icontains: DateTime
  startswith: DateTime
  istartswith: DateTime
  endswith: DateTime
  iendswith: DateTime
  range: [DateTime]
  isnull: Boolean
  regex: String
  iregex: String
  year: DateTime
  month: DateTime
  day: DateTime
  weekDay: DateTime
  isoWeekDay: DateTime
  week: DateTime
  isoYear: DateTime
  quarter: DateTime
  containedBy: DateTime
  hour: DateTime
  minute: DateTime
  second: DateTime
  date: DateTime
  time: DateTime
}
# - Pagination
input PaginationConfigInput {
  page: Int = 1
  itemsPerPage: IntOrAll = "All"
}



# Types
# - From the model: Question
type QuestionType {
  id: ID
  questionText: String!
  pubDate: DateTime!
}
type QuestionPaginatedType implements PaginationInterface {
  total: Int
  page: Int
  pages: Int
  hasNext: Boolean
  hasPrev: Boolean
  indexStartObj: Int
  indexEndObj: Int
  objects: [QuestionType!]
}
# - Payload the mutations
type CreateQuestionsPayload {
  objects: [QuestionType]
  errorsReport: [ErrorCollectionType]
}
type UpdateQuestionsPayload {
  objects: [QuestionType]
  errorsReport: [ErrorCollectionType]
}
type ActivateQuestionsPayload {
  objects: [QuestionType]
  errorsReport: [ErrorCollectionType]
}
type DeactivateQuestionsPayload {
  objects: [QuestionType]
  errorsReport: [ErrorCollectionType]
}
type DeleteQuestionsPayload {
  objects: [QuestionType]
  errorsReport: [ErrorCollectionType]
  success: Boolean
}
# - Error
type ErrorCollectionType {
  objectPosition: String
  errors: [ErrorType]
}
type ErrorType {
  field: String!
  messages: [String!]!
}



# Interfaces

interface PaginationInterface {
  total: Int
  page: Int
  pages: Int
  hasNext: Boolean
  hasPrev: Boolean
  indexStartObj: Int
  indexEndObj: Int
}


# Scalars

"""
The `DateTime` scalar type represents a DateTime
value as specified by
[iso8601](https://en.wikipedia.org/wiki/ISO_8601).
"""
scalar DateTime
"""The page size can be int or 'All'"""
scalar IntOrAll


# Enums
enum OrderEnum {
  ASC
  DESC
}

enum OrderStringEnum {
  ASC
  DESC
  IASC
  IDESC
}

```

</details>  

🎉🥳 Now you can use and test in Graphiql 🚀🚀🚀  

## <a name="features">🎁 Features</a>

| Status | Description |
| :----: | ----------- |
| ✅     | Done        |
| 〰️     | In progress |
| ❌     | Not started |



|                        Feature                                         |     Status          |                 Comments              |
| -----------------------------------------------------------------------| :-----------------: | :-----------------------------------: |
| Generate `ObjectType` from Django model                                |         ✅          |        Pending for documentation      |
| Generate `InputObjectType` from Django model                           |         ✅          |        Pending for documentation      |
| Generate `Fields` from Django model                                    |         ✅          |        Pending for documentation      |
| Generate `InputFields` from Django model                               |         ✅          |        Pending for documentation      |
| Generate `Arguments` from Django model                                 |         ✅          |        Pending for documentation      |
| Generate `Mutations` from Django model                                 |         ✅          |        Pending for documentation      |
| Generate `Queries` from Django model                                   |         ✅          |        Pending for documentation      |
| Generate `resolvers` from Django model                                 |         ✅          |        Pending for documentation      |
| Generate `Create` operation for a Django model                         |         ✅          |        Pending for documentation      |
| Generate `Read` operation for a Django model                           |         ✅          |        Pending for documentation      |
| Generate `Update` operation for a Django model                         |         ✅          |        Pending for documentation      |
| Generate `Delete` operation for a Django model                         |         ✅          |        Pending for documentation      |
| Generate `Deactivate` operation for a Django model                     |         ✅          |        Pending for documentation      |
| Generate `Activate` operation for a Django model                       |         ✅          |        Pending for documentation      |
| Generate `List` operation for a Django model                           |         ✅          |        Pending for documentation      |
| Generate `Search` operation for a Django model                         |         〰️          |        Pending for documentation      |
| Generate each operation, all to be performed `massively`               |         〰️          |        Pending for documentation      |
| Handle `null` and `blank` attribute of Django model                    |         〰️          |        Pending for documentation      |
| Handle `editable` attribute of Django model                            |         〰️          |        Pending for documentation      |
| Handle `help_text` attribute of Django model                           |         〰️          |        Pending for documentation      |
| Handle `default` attribute of Django model                             |         〰️          |        Pending for documentation      |
| Handle `choices` attribute of Django model                             |         〰️          |        Pending for documentation      |
| Handle `OneToOneField` field of Django model                           |         〰️          |        Pending for documentation      |
| Handle `OneToOneRel` field of Django model                             |         〰️          |        Pending for documentation      |
| Handle `ManyToManyField` field of Django model                         |         〰️          |        Pending for documentation      |
| Handle `ManyToManyRel` field of Django model                           |         〰️          |        Pending for documentation      |
| Handle `ForeignKey` field of Django model                              |         〰️          |        Pending for documentation      |
| Handle `ManyToOneRel` field of Django model                            |         〰️          |        Pending for documentation      |
| Handle `GenericForeignKey` field of Django model                       |         〰️          |        Pending for documentation      |
| Handle `GenericRel` field of Django model                              |         〰️          |        Pending for documentation      |
| Handle `FileField` and `ImageField` fields of Django Model             |         〰️          |        Pending for documentation      |
| Handle `JSONField` field of Django model                               |         〰️          |        Pending for documentation      |
| Allowing nested mutations at any depth level                           |         〰️          |        Pending for documentation      |
| Allowing nested queries at any depth level                             |         〰️          |        Pending for documentation      |
| Handle pagination of query results                                     |         〰️          |        Pending for documentation      |
| Handle sorting of query results                                        |         〰️          |        Pending for documentation      |
| Handle advanced search                                                 |         〰️          |        Pending for documentation      |
| Handle advanced search with `AND` operator                             |         〰️          |        Pending for documentation      |
| Handle advanced search with `OR` operator                              |         〰️          |        Pending for documentation      |
| Handle advanced search with `NOT` operator                             |         〰️          |        Pending for documentation      |
| Handle advanced search with `relational fields` operator               |         〰️          |        Pending for documentation      |
| Providing a friendly and comprehensive list of errors                  |         〰️          |        Pending for documentation      |
| Allow use the ObjectTypes generated from the models                    |         〰️          |        Pending for documentation      |
| Allow customizing the `ObjectType` generated by CRUDDALS               |         〰️          |        Pending for documentation      |
| Allow customizing the `InputObjectType` generated by CRUDDALS          |         〰️          |        Pending for documentation      |
| Allow customizing the `Fields` generated by CRUDDALS                   |         〰️          |        Pending for documentation      |
| Allow customizing the `InputFields` generated by CRUDDALS              |         〰️          |        Pending for documentation      |
| Allow customizing the `Arguments` generated by CRUDDALS                |         〰️          |        Pending for documentation      |
| Allow customizing the `Mutations` generated by CRUDDALS                |         〰️          |        Pending for documentation      |
| Allow customizing the `Queries` generated by CRUDDALS                  |         〰️          |        Pending for documentation      |
| Allow customizing the `resolvers` generated by CRUDDALS                |         〰️          |        Pending for documentation      |
| Generate all operations at the `model`, `app`, or `project` **level**  |         〰️          |        Pending for documentation      |
| Files for consuming the GraphQL API with any JavaScript client         |         〰️          |        Pending for documentation      |
| File with the queries and mutations for with GraphiQL                  |         〰️          |        Pending for documentation      |
| File with the entire GraphQL schema generated                          |         〰️          |        Pending for documentation      |
| Handle transactions in mutations                                       |         ❌          |        Pending for documentation      |
| Handle directives in queries and mutations                             |         ❌          |        Pending for documentation      |
| Handle subscriptions                                                   |         ❌          |        Pending for documentation      |
| Optimized queries and mutations                                        |         ❌          |        Pending for documentation      |
| Generate Types for TypeScript                                          |         ❌          |        Pending for documentation      |
| Generate validators for Zod, Yup, others                               |         ❌          |        Pending for documentation      |



## <a name="documentation">📚 Documentation</a>

You can find the full documentation [here](https://graphene-django-cruddals.readthedocs.io/en/latest/), please keep in mind that this is a work in progress.

## <a name="license">📜 License</a>

Distributed under the MIT License. See [LICENSE](https://github.com/juanjcardona13/graphene_django_cruddals/blob/main/LICENSE) for more information.

## <a name="contributing">❤️ Contributing</a>

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. For more information, please read the [CONTRIBUTING.md]()

## <a name="contact">📞 Contact</a>

- [Email](mailto:juanjcardona13@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/juanjcardona13/)
- [GitHub](https://github.com/juanjcardona13)

## <a name="acknowledgements">🙏 Acknowledgements</a>

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Graphene Django](https://docs.graphene-python.org/projects/django/en/latest/)
- [Graphene Django CRUD](https://github.com/djipidi/graphene_django_crud)
- [Readme Template 1](https://www.makeareadme.com)
- [Readme Template 2](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)

## <a name="roadmap">🗺️ Roadmap</a>

- [ ] Finish documentation
- [ ] Add more examples
- [ ] Add more features
- [ ] Add tests
- [ ] Add localization
- [ ] Add SEO
- [ ] Add analytics
- [ ] Make social marketing
- [ ] Add monitoring
- [ ] Add logging
- [ ] Add CI/CD
- [ ] Add collaboration
- [ ] Add communication
- [ ] Add networking

