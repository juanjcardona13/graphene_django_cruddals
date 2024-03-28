from setuptools import find_packages, setup
import ast
import re

_version_re = re.compile(r"__version__\s+=\s+(.*)")

with open("graphene_django_cruddals/__init__.py", "rb") as f:
    VERSION = str(
        ast.literal_eval(_version_re.search(f.read().decode("utf-8")).group(1))
    )

tests_require = [
    "pytest>=3.6.3"
]

setup(
    name="graphene_django_cruddals",
    version=VERSION,
    description="Framework for trivial code, Easy and Fast for learn, Easy and Fast for use",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/juanjcardona13",
    author="Juan J Cardona",
    author_email="juanjcardona13@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
    ],
    keywords="api graphql crud graphene graphene-django",
    packages=find_packages(exclude=["tests", "examples", "examples.*"]),
    install_requires=[
        "graphene-django>=3.0.0",
        "mypy==1.9.0"
    ],
    setup_requires=["pytest-runner"],
    tests_require=tests_require,
    extras_require={
        "test": tests_require
    },
    include_package_data=True,
    zip_safe=False,
    platforms="any",
)
