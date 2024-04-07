

<h1 align="center">Graphene-Django-CRUDDALS</h1>
<div align="center">

👩🏽‍💻 🚀 👨🏽‍💻  
**Framework for trivial code, easy and fast to learn and use.**  
Turn your Django-models into a complete GraphQL API with all CRUD operations  

[![PyPI](https://img.shields.io/pypi/v/graphene-django-cruddals?style=flat-&color=00559c&label=pypi&logo=python&logoColor=white)](https://pypi.org/project/graphene-django-cruddals/)
[![GitHub License](https://img.shields.io/github/license/juanjcardona13/graphene_django_cruddals?style=flat&color=4c1)](https://github.com/juanjcardona13/graphene_django_cruddals/blob/main/LICENSE)


[Docs](https://graphene-django-cruddals.readthedocs.io/en/latest/) |...|...|

<small>Built with ❤︎ by [Juan J Cardona](https:github.com/juanjcardona13) and [contributors](https://github.com/juanjcardona13/graphene_django_cruddals/graphs/contributors) 
</small>
</div>

## 📋 Table of Contents

1. 🚀 [Getting started](#getting-started)
2. 👩‍💻 [Usage](#basic-usage)
3. 📚 [Documentation](#documentation)
4. 📜 [License](#license)
5. ❤️ [Contributing](#contributing)
6. 📞 [Contact](#contact)
7. 🙏 [Acknowledgements](#acknowledgements)
8.  🎁 [Features](#features)
9. 🗺️ [Roadmap](#roadmap)


## 🚀 Getting started

### Prerequisites

To install this project you need to have a Django project already set up. If you don't have one, you can follow the [official Django tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/).

### Installation

You can install this package using pip:

```bash
pip install graphene-django-cruddals
```

## 👩‍💻 Usage

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
type Query {
  readQuestion(where: QuestionFilterInput!): QuestionType
  searchQuestions(where: QuestionFilterInput, orderBy: QuestionOrderByInput, paginated: PaginationConfigInput): QuestionPaginatedType
  listQuestions: [QuestionType!]
}

type Mutation {
  createQuestions(input: [CreateQuestionInput!]): CreateQuestionsPayload
  updateQuestions(input: [UpdateQuestionInput!]): UpdateQuestionsPayload
  activateQuestions(where: QuestionFilterInput!): ActivateQuestionsPayload
  deactivateQuestions(where: QuestionFilterInput!): DeactivateQuestionsPayload
  deleteQuestions(where: QuestionFilterInput!): DeleteQuestionsPayload
}

# Input types
input QuestionInput {
  id: ID
  questionText: String
  pubDate: DateTime
}
input CreateQuestionInput {
  questionText: String!
  pubDate: DateTime!
}
input UpdateQuestionInput {
  id: ID!
  questionText: String
  pubDate: DateTime
}
input QuestionFilterInput {
  id: IDFilter
  questionText: StringFilter
  pubDate: DateTimeFilter
  AND: [QuestionFilterInput!]
  OR: [QuestionFilterInput!]
  NOT: QuestionFilterInput
}
input QuestionOrderByInput {
  id: OrderEnum
  questionText: OrderStringEnum
  pubDate: OrderEnum
}

# Output types
type QuestionType {
  id: ID!
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
# ... and more
```

</details>  

🎉🥳 Now you can use and test in Graphiql 🚀🚀🚀


## 📚 Documentation

You can find the full documentation [here](https://graphene-django-cruddals.readthedocs.io/en/latest/), please keep in mind that this is a work in progress.

## 📜 License

Distributed under the MIT License. See [LICENSE](https://github.com/juanjcardona13/graphene_django_cruddals/blob/main/LICENSE) for more information.

## ❤️ Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. For more information, please read the [CONTRIBUTING.md]()

## 📞 Contact

- [Email](mailto:juanjcardona13@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/juanjcardona13/)
- [GitHub](https://github.com/juanjcardona13)

## 🙏 Acknowledgements

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Graphene Django](https://docs.graphene-python.org/projects/django/en/latest/)
- [Graphene Django CRUD](https://github.com/djipidi/graphene_django_crud)
- [Readme Template 1](https://www.makeareadme.com)
- [Readme Template 2](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)


## 🎁 Features

|                            |     Status        |     Comments     |
| -------------------------- | :-----------------: | :---------------: |
| Generate a complete GraphQL schema from a Django model           |         ✅         |        〰️        |
| Generate the necessary ObjectTypes, InputObjectTypes, Fields, InputFields, Arguments, Mutations, Queries, and resolvers to interact with a Django model           |         ✅         |        〰️        |
| Generate 8 CRUD (Create, Read, Update, Delete) + DALS (Deactivate, Activate, List, Search) operations for a Django model in seconds           |         ✅         |        〰️        |
| Generate each of the Create, Update, Delete, Deactivate, Activate, List, and Search operations, all to be performed massively           |         ✅         |        〰️        |
| Handle required and non-required fields of Django models based on the blank and null attributes           |         ✅         |        〰️        |
| Handle editable and non-editable fields of Django models based on the editable attribute           |         ✅         |        〰️        |
| Generate documentation for the fields of Django models based on the help_text attribute           |         ✅         |        〰️        |
| Generate default values for Django model fields based on the default attribute           |         ✅         |        〰️        |
| Generate enums for Django model fields based on the choices attribute           |         ✅         |        〰️        |
| Handle one-to-many, many-to-one, one-to-one, and many-to-many relationships, both directly and inversely           |         ✅         |        〰️        |
| Handle nested model relationships for mutations, allowing nested mutations           |         ✅         |        〰️        |
| Handle nested model relationships for queries, allowing nested queries at any depth level, with all pagination, sorting, and advanced search features           |         ✅         |        〰️        |
| Handle pagination of query results, both at the top level and for nested levels           |         ✅         |        〰️        |
| Handle sorting of query results           |         ✅         |        〰️        |
| Handle advanced search to perform complex and nested queries with model fields, related fields, and logical operators AND, OR, NOT           |         ✅         |        〰️        |
| Handle (thanks to graphene-file-upload) File and ImageField types of Django           |         ✅         |        〰️        |
| Handle JSONField types of Django to deliver them as a JSON string or as a JSON object           |         ✅         |        〰️        |
| Have excellent data validation in mutations (thanks to DjangoForm), providing a friendly and comprehensive list of errors           |         ✅         |        〰️        |
| Expose a function to use the ObjectTypes generated from the models           |         ✅         |        〰️        |
| Handle polymorphic relationships, both one-to-many and many-to-one           |         ✅         |        〰️        |
| Extend and/or customize each part of the GraphQL schema generated by Graphene Django CRUDDALS, such as ObjectTypes, InputObjectTypes, Fields, InputFields, Arguments, Mutations, Queries, and even resolvers           |         ✅         |        〰️        |
| Generate CRUD+DALS operations at the model, app, or project level           |         ✅         |        〰️        |
| Generate a folder with the necessary files for consuming the GraphQL API with any JavaScript client, following the best practices of DRY (Don't Repeat Yourself) and saving hours of work, messy code, and errors. Don't think about how to consume your GraphQL API, Graphene Django CRUDDALS does it for you. (Just consume it)           |         ✅         |        〰️        |
| Generate a file with the queries and mutations created so that you can test your GraphQL API with GraphiQL           |         ✅         |        〰️        |
| Generate a .gql and .json file with the entire GraphQL schema generated so that you can share it with your team or anyone interested, or you can also use it with other GraphQL tools for the frontend like those in the ecosystem https://the-guild.dev/#platform, Apollo, etc., or so you can migrate to another language or backend framework. The possibilities are endless           |         ✅         |        〰️        |
| Handle transactions in mutations           |         ❌         |        〰️        |
| Handle directives in queries and mutations           |         ❌         |        〰️        |
| Handle subscriptions           |         ❌         |        〰️        |
| Optimized queries and mutations           |         ❌         |        〰️        |
| Generate Types for TypeScript           |         ❌         |        〰️        |
| Generate validators in Zod, Yup, others           |         ❌         |        〰️        |

## 🗺️ Roadmap

- [x] Create a complete CRUD+DALS
- [x] Add support for custom fields
- [ ] Add support for custom queries
- [ ] Add support for custom mutations
- [ ] Add support for custom resolvers