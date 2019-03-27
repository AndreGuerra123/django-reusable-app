
[![CircleCI](https://circleci.com/gh/AndreGuerra123/django-reusable-app/tree/master.svg?style=svg)](https://circleci.com/gh/AndreGuerra123/django-reusable-app/tree/master)

# Django Reusable App

A cookiecutter template to package Django Reusable Apps.

## Goals

Creating reusable Django packages has always been annoying. There are no defined/maintained
best practices (especially for ``setup.py``), so you end up cutting and pasting hacky, poorly understood,
often legacy code from one project to the other. This template, inspired by [cookiecutter-pypackage](https://),
is designed to allow Django developers the ability to break free from cargo-cult configuration and follow
a common pattern dictated by the experts and maintained here.

## Features

* [Poetry](https://github.com/sdispater/poetry) as package manager
* [CircleCI](https://circleci.com/) as automated continuous integration pipeline
* [Coverage.py](https://github.com/nedbat/coveragepy) as coverage measurement tool.
* [Codecov](https://codecov.io/) as coverage reporter tool.
* [Flake8](https://gitlab.com/pycqa/flake8) as Python code linter.
* [Tox](https://tox.readthedocs.io/en/latest/) as automated Python multiversioning testing platform.
* [Sphinx](http://www.sphinx-doc.org/en/master/) as documentation builder
* [MIT](https://opensource.org/licenses/MIT) licensed by default


## Getting Started

These instructions will let you to build a fully documented, tested and integrated [Django](https://www.djangoproject.com/) reusable app in seconds.

### Prerequisites

First install [Cookiecutter](https://github.com/audreyr/cookiecutter):

```
pip install cookiecutter
```

### Installing

Only one step is required to create a Django reusable app:

```
cookiecutter gh:AndreGuerra123/django-reusable-app
```

You'll be prompted for some questions, answer them, then it will create a directory that is your new package.
Enter the created reusable app project and take a look around:

```
cd YOUR_PACKAGE_NAME/
ls
```

Django reusable app require the use of [Poetry](https://github.com/sdispater/poetry) as the package manager. 

```
pip install poetry
```

Then install your app development dependencies and create a virtualenv using:

```
poetry install
poetry shell
```

Create a GitHub repo and push it there:

```
git init
git add .
git commit -m "first awesome commit"
git remote add origin git@github.com:YOUR_GIT_USERNAME/YOUR_GIT_REPO.git
git push -u origin master
```

You're set up. It's time to write the code!!!

### Linting

In order to lint using [Flake8](https://gitlab.com/pycqa/flake8) your project in your local development environment, just run the following:

```
poetry run flake8 YOUR_PACKAGE_NAME
```

### Documentation

In order to automatically build your project documentation using [Sphinx](http://www.sphinx-doc.org/en/master/), just run the following command:

```
poetry run sphinx-apidoc -o /docs YOUR_APP_NAME
```

### Testing

In order to test your project in your local development environment, just run the following:

```
poetry run tox
```

### Deployment

Deployment is perfomed automatically by [CircleCI](https://circleci.com/) and [Poetry](https://github.com/sdispater/poetry), if all tests are passed.
Your order to do so, your Pypi credentials must be added to CircleCI environment.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. 

For the versions available, see the [tags on this repository](https://github.com/AndreGuerra123/django-reusable-app/tags). 

For the modifications made in each version, read the [CHANGELOG.md](CHANGELOG.md).

## Authors

See also the list of [contributors](CONTRIBUTORS.md) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Future Perspectives

Please refer to [ROADMAP.md](ROADMAP.md) for future features to be developed.
