=============================
{{ cookiecutter.project_name }}
=============================

.. image:: https://circleci.com/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?style=svg
    :target: https://circleci.com/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?version=latest
    :target: https://{{ cookiecutter.repo_name }}.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/pypi/pyversions/envision.svg

.. image:: https://img.shields.org//pypi/pyversions//{{cookiecutter.repo_name}}.svg

.. image:: https://img.shields.io/pypi/djversions/{{cookiecutter.repo_name}}.svg

.. image:: https://img.shields.io/pypi/djversions/{{cookiecutter.repo_name}}.svg

.. image:: https://img.shields.io//pypi/wheel/{{cookiecutter.repo_name}}.svg

{{ cookiecutter.project_short_description}}

Documentation
-------------

The full documentation is at https://{{ cookiecutter.repo_name }}.readthedocs.io.

Quickstart
----------

Install {{ cookiecutter.project_name }}::

    pip install {{ cookiecutter.repo_name }}

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        '{{ cookiecutter.app_name }}',
        ...
    )

Add {{ cookiecutter.project_name }}'s URL patterns:

.. code-block:: python

    import {{ cookiecutter.app_name }}

    urlpatterns = [
        ...
        url(r'^', include({{ cookiecutter.app_name }}.urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?::
    $ cd {{ cookiecutter.repo_name }}
    $ poetry install
    $ poetry run runtests.py

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`django-reusable-app`: https://github.com/AndreGuerra123/django-reusable-app
