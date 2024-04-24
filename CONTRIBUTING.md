
# ❤️ Contributing

We appreciate your interest in improving Graphene-Django-CRUDDALS!

Any contribution you can offer will be valued and beneficial to the community. Some ways you can contribute include:

- Proposing new ideas to improve the project.
- Promoting the project among your peers and relevant communities.
- Refactoring and organizing existing code to improve its readability and maintainability.
- Improving documentation to make it clearer and more comprehensive.
- Fixing errors reported by the community or discovered during code review.
- Contributing resources, whether financial, time, or knowledge-based.

## Getting Started

If you already have a contribution in mind, we recommend that you first review the open issues and project progress to ensure that your idea is not already in development or has been proposed by other contributors.

## Setting up the Project

After cloning this repository, make sure you have all the dependencies installed. You can do this by running the following command:
  

```sh
make dev-setup
```

Set up a virtual environment using the following command:

```sh
python -m venv venv
source venv/bin/activate
```

## Development



## Testing

Once the setup process is complete, we invite you to test the project's functionality. You can do this by running:

```sh
make tests
```

## Opening Pull Requests

Ready to go? Fork the project and open a pull request from the 'main' branch. This will initiate a review process that includes code comparisons and automated tests.

We recommend that before opening the pull request, you restart and run lint tests locally to avoid unnecessary errors and save time.

```sh
make format
make lint
```

## Documentation

Our documentation is done with MkDocs and uses ReadTheDocs theme. Documentation dependencies can be installed with:

```sh
pip install -r docs/requirements.txt
```

To generate an HTML version of the documentation, run:

```sh
mkdocs build
```








