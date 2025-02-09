import ast
import re

from setuptools import find_packages, setup

_version_re = re.compile(r"__version__\s+=\s+(.*)")

VERSION = "0.0.0"

with open("graphene_django_cruddals/__init__.py", "rb") as f:
    _version_re_search = _version_re.search(f.read().decode("utf-8"))
    if _version_re_search is not None:
        VERSION = str(ast.literal_eval(_version_re_search.group(1)))

tests_require = [
    "pytest>=7.3.1",
    "pytest-cov",
    "pytest-random-order",
    "coveralls",
    "mock",
    "pytz",
    "django-filter>=22.1",
    "pytest-django>=4.5.2",
]

dev_requires = [
    "ruff==0.1.2",
    "pre-commit",
] + tests_require

setup(
    name="graphene_django_cruddals",
    version=VERSION,
    description="Framework for trivial code, Easy and Fast for learn, Easy and Fast for use",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/juanjcardona13/graphene_django_cruddals",
    author="Juan J Cardona",
    author_email="juanjcardona13@gmail.com",
    license="Apache 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
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
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.2",
    ],
    keywords="api graphql crud graphene graphene-django cruddals",
    packages=find_packages(exclude=["tests", "examples", "examples.*"]),
    install_requires=["graphene-django>=3.0.0", "graphene-cruddals>=0.2.11"],
    setup_requires=["pytest-runner"],
    tests_require=tests_require,
    extras_require={
        "test": tests_require,
        "dev": dev_requires,
    },
    include_package_data=True,
    zip_safe=False,
    platforms="any",
)
