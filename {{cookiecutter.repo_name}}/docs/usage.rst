=====
Usage
=====

To use {{ cookiecutter.project_name }} in a project, add it to your `INSTALLED_APPS`:

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
