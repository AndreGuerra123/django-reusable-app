import os, pytest, subprocess, datetime


full_context = {
        "full_name": "John Doe",
        "email": "jd@host.com",
        "github_username": "JDoe",
        "project_name": "Django Reusable App",
        "repo_name": "dj-reusable",
        "app_name": "dj_reusable",
        "app_config_name": "DjangoReusableAppConfig",
        "project_short_description": "My Django Reusable App",
        "version": "0.1.0",
        "create_example_project": "Yes",
        "open_source_license": "MIT"
        }

def test_bake(cookies):
    """
    Test to check if package project can be created (without providing extra context)
    """
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'dj-package'
    assert result.project.isdir()

def test_bake_full_context(cookies):
    """
    Test to check if package project can be created (with full context)
    """
    result = cookies.bake(extra_context=full_context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == full_context['repo_name']
    assert result.project.isdir()

def test_structure(cookies):
    """
    Test to check if package project structure is correct
    """
    result = cookies.bake(extra_context=full_context)
    root = result.project

    #test root files
    assert root.join('.gitignore').isfile()
    assert root.join('AUTHORS.rst').isfile()
    assert root.join('CONTRIBUTING.rst').isfile()
    assert root.join('HISTORY.rst').isfile()
    assert root.join('manage.py').isfile()
    assert root.join('pyproject.toml').isfile()
    assert root.join('README.rst').isfile()
    assert root.join('runtests.py').isfile()
    assert root.join('tox.ini').isfile()

    #test root dirs files (and implicitly dirs)
    # .circleci
    circle_root = root.join('.circleci')
    assert circle_root.join('config.yml').isfile()
    # .github
    github_root = root.join('.github')
    assert github_root.join('ISSUE_TEMPLATE.md').isfile()
    # dj_package
    app_root = root.join(full_context['app_name'])
    assert app_root.join('static').join('css').join('{}.css'.format(full_context['app_name'])).isfile()
    assert app_root.join('static').join('img').join('.gitignore').isfile()
    assert app_root.join('static').join('js').join('{}.js'.format(full_context['app_name'])).isfile()
    assert app_root.join('templates').join(full_context['app_name']).join('base.html').isfile()
    assert app_root.join('__init__.py').isfile()
    assert app_root.join('apps.py').isfile()
    assert app_root.join('models.py').isfile()
    assert app_root.join('urls.py').isfile()
    assert app_root.join('views.py').isfile()
    #docs
    docs_root = root.join('docs')
    assert docs_root.join('conf.py').isfile()
    assert docs_root.join('contributing.rst').isfile()
    assert docs_root.join('history.rst').isfile()
    assert docs_root.join('index.rst').isfile()
    assert docs_root.join('installation.rst').isfile()
    assert docs_root.join('make.bat').isfile()
    assert docs_root.join('Makefile').isfile()
    assert docs_root.join('readme.rst').isfile()
    assert docs_root.join('usage.rst').isfile()
    #example
    ex_root = root.join('example')
    assert ex_root.join('example').join('__init__.py').isfile()
    assert ex_root.join('example').join('settings.py').isfile()
    assert ex_root.join('example').join('urls.py').isfile()
    assert ex_root.join('example').join('wsgi.py').isfile()
    assert ex_root.join('templates').join(full_context['app_name']).join('base.html').isfile()
    assert ex_root.join('manage.py').isfile()
    assert ex_root.join('README.md').isfile()
    assert ex_root.join('pyproject.toml').isfile()
    #tests
    t_root = root.join('tests')
    assert t_root.join('__init__.py').isfile()
    assert t_root.join('settings.py').isfile()
    assert t_root.join('test_models.py').isfile()
    assert t_root.join('urls.py').isfile()

def test_structure_no_example_project(cookies):
    """
    Test to check if package project structure is correct without examples project creation
    """
    no_example_context = full_context.copy()
    no_example_context['create_example_project'] = "No"
    result = cookies.bake(extra_context=no_example_context)
    root = result.project
    assert not root.join('example').isdir()

# Test old manifest files

def test_readme(cookies):
    """
    Test the generation of a correct readme file.
    """
    result = cookies.bake(extra_context=full_context)
    readme_file = result.project.join('README.rst')
    readme_lines = [x.strip() for x in readme_file.readlines(cr=False)]
    assert 'pip install {}'.format(full_context['repo_name']) in readme_lines
    assert "'{}',".format(full_context['app_name']) in readme_lines
    assert 'import {}'.format(full_context['app_name']) in readme_lines
    assert "path('/{}', include({}.urls)),".format(full_context['app_name'],full_context['app_name']) in readme_lines

def test_authors(cookies):
    result = cookies.bake(extra_context=full_context)
    authors_text = result.project.join('AUTHORS.rst').read()
    assert '* {} <{}>'.format(full_context['full_name'],full_context['email']) in authors_text
        
def test_contributing(cookies):
    result = cookies.bake(extra_context=full_context)
    contributing_txt = result.project.join('CONTRIBUTING.rst').read()
    assert 'Report bugs at https://github.com/{}/{}/issues.'.format(full_context['github_username'],full_context['repo_name']) in contributing_txt
    assert '{} could always use more documentation'.format(full_context['project_name']) in contributing_txt
    assert 'The best way to send feedback is to file an issue at https://github.com/{}/{}/issues.'.format(full_context['github_username'],full_context['repo_name']) in contributing_txt
    assert "Ready to contribute? Here's how to set up `{}` for local development.".format(full_context['repo_name']) in contributing_txt
    assert "1. Fork the `{}` repo on GitHub.".format(full_context['repo_name']) in contributing_txt
    assert "$ git clone git@github.com:your_name_here/{}.git".format(full_context['repo_name']) in contributing_txt
    assert "$ cd {}/".format(full_context['repo_name']) in contributing_txt
    assert "$ poetry run flake8 {}".format(full_context['app_name']) in contributing_txt
    assert "$ poetry run sphinx-apidoc -o docs/ {} --force".format(full_context['app_name']) in contributing_txt
    assert "https://travis-ci.org/{}/{}/pull_requests".format(full_context['github_username'],full_context['repo_name']) in contributing_txt

def test_history(cookies):
        result = cookies.bake(extra_context=full_context)
        history_text = result.project.join('HISTORY.rst').read()
        assert full_context['version'] in history_text

# Test tools files

def test_circleci(cookies):
    """
    Test case to assert that the circleci configuration file has the basic template
    """
    result = cookies.bake(extra_context=full_context)
    circleci_config_file = result.project.join('.circleci').join('config.yml')
    circleci_lines = [x.strip() for x in circleci_config_file.readlines(cr=False)]
    assert 'poetry install' in circleci_lines
    assert 'poetry run flake8 {}'.format(full_context['app_name']) in circleci_lines
    assert 'poetry run tox' in circleci_lines
    assert 'poetry run sphinx-apidoc -o docs/ {} --force'.format(full_context['app_name']) in circleci_lines
    assert 'poetry publish --build --username "${PYPI_USERNAME}" --password "${PYPI_PASSWORD}" --no-interaction' in circleci_lines
    assert 'poetry run codecov' in circleci_lines

def test_tox(cookies):
    """
    Test case to assert that the tox configuration file has the basic template
    """
    result = cookies.bake(extra_context={'repo_name': 'dj-pack','app_name':'dj_app'})
    tox_config_file = result.project.join('tox.ini')
    tox_config_lines = [x.strip() for x in tox_config_file.readlines(cr=False)]
    required = ["skipsdist = True",
       "{py27}-django{109,110,111}",
       "{py340,py35,py36,py370}-django{111,20,21}",
       "whitelist_externals = poetry, django",
       "skip_install = true",
       "poetry run coverage run --branch runtests.py",
       "django109: Django<=1.9",
       "django110: Django>=1.10,<1.11",
       "django111: Django>=1.11,<2.0",
       "django20: Django>=2.0,<2.1",
       "django21: Django>=2.1"]
    for req in required:
            assert req in tox_config_lines
    
def test_poetry(cookies):
    result = cookies.bake(extra_context=full_context)
    poetry_file = result.project.join('pyproject.toml')
    poetry_text = poetry_file.read()
    #TODO:

# Test app files

def test_app_url(cookies):
    """
    Test case to assert that the urls.py file has the basic template
    """
    result = cookies.bake(extra_context=full_context)
    urls_file_txt = result.project.join(full_context['app_name'], 'urls.py').read()
    assert "app_name = \'{}\'".format(full_context['app_name']) in urls_file_txt
    assert "url(r'', TemplateView.as_view(template_name='base.html'))" in urls_file_txt

def test_app_config(cookies):
    """
    Test case to assert that the app.py file has the basic template
    """
    result = cookies.bake(extra_context=full_context)
    app_config_file_txt = result.project.join(full_context['app_name'], 'apps.py').read()
    assert "class {}(AppConfig):".format(full_context['app_config_name']) in app_config_file_txt
    assert "name = '{}'".format(full_context['app_name']) in app_config_file_txt

def test_version_in_init(cookies):
    """
    Test case to assert that the init.py file has the versioning
    """
    result = cookies.bake(extra_context=full_context)
    init_file_txt = result.project.join(full_context['app_name'], '__init__.py').read()
    assert "__version__ = '{}'".format(full_context['version']) in init_file_txt
    
# Test docs files
def test_docs_conf(cookies):
    """
    Test case to assert that the docs/conf.py file has the correct template
    """
    result = cookies.bake(extra_context=full_context)
    conf_file_txt = result.project.join('docs', 'conf.py').read()
    assert "import {}".format(full_context['app_name']) in conf_file_txt
    assert "project = u'{}'".format(full_context['project_name']) in conf_file_txt
    assert "copyright = u'{}, {}'".format(datetime.datetime.now().year,full_context['full_name']) in conf_file_txt
    assert "version = {}.__version__".format(full_context['app_name']) in conf_file_txt
    assert "release = {}.__version__".format(full_context['app_name']) in conf_file_txt
    assert "htmlhelp_basename = '{}doc'".format(full_context['repo_name']) in conf_file_txt
    assert "('index', '{}.tex', u'{} Documentation',".format(full_context['repo_name'],full_context['project_name']) in conf_file_txt
    assert "u'{}', 'manual'),".format(full_context['full_name']) in conf_file_txt
    assert "('index', '{}', u'{} Documentation',".format(full_context['repo_name'],full_context['project_name']) in conf_file_txt
    assert "u'{}', '{}', 'One line description of project.',".format(full_context['full_name'],full_context['repo_name']) in conf_file_txt

def test_docs_usage(cookies):
    """
    Test case to assert that the docs/usage.rst file has the correct template
    """
    result = cookies.bake(extra_context=full_context)
    usage_file_txt = result.project.join('docs', 'usage.rst').read()
    assert "To use {} in a project, add it to your `INSTALLED_APPS`:".format(full_context['project_name']) in usage_file_txt
    assert "'{}',".format(full_context['app_name']) in usage_file_txt
    assert "Add {}'s URL patterns:".format(full_context['project_name']) in usage_file_txt
    assert "import {}".format(full_context['app_name']) in usage_file_txt
    assert "url(r'^', include({}.urls)),".format(full_context['app_name']) in usage_file_txt

# Test example files

def test_example_poetry(cookies):
    """
    Test case to assert that the example/pyproject.toml file has the correct template
    """
    result = cookies.bake(extra_context=full_context)
    poetry_file_txt = result.project.join('example', 'pyproject.toml').read()
    assert 'description = "An example project with your {} app.'.format(full_context['project_name']) in poetry_file_txt
    assert 'authors = ["{} <{}>"]'.format(full_context['full_name'],full_context['email']) in poetry_file_txt
    assert 'python = "*"' in poetry_file_txt
    assert 'django = "*"' in poetry_file_txt

def test_example_template(cookies):
    """
    Test case to assert that the example/templates/{{cookiecutter.app_name}}/base.html file has the correct template
    """
    result = cookies.bake(extra_context=full_context)
    template_file_txt = result.project.join('example','templates',full_context['app_name'],'base.html').read()
    assert full_context['app_name'] in template_file_txt
    assert full_context['repo_name'] in template_file_txt

def test_example_settings(cookies):
    """
    Test case to assert that the example/example/settings.py file has the correct template
    """
    result = cookies.bake(extra_context=full_context)
    settings_file_txt = result.project.join('example','example','settings.py').read()
    assert "'{}',".format(full_context['app_name']) in settings_file_txt

def test_example_urls(cookies):
    """
    Test case to assert that the example/example/urls.py file has the correct template
    """
    result = cookies.bake(extra_context=full_context)
    urls_file_txt = result.project.join('example','example','urls.py').read()
    assert "url(r'', include('{}.urls', namespace='{}')),".format(full_context['app_name'],full_context['app_name']) in urls_file_txt

def test_docs_usage(cookies):
    """
    Test case to assert that the docs/usage.rst file has the correct template
    """
    result = cookies.bake(extra_context=full_context)
    usage_file_txt = result.project.join('docs', 'usage.rst').read()
    assert "To use {} in a project, add it to your `INSTALLED_APPS`:".format(full_context['project_name']) in usage_file_txt
    assert "'{}',".format(full_context['app_name']) in usage_file_txt
    assert "Add {}'s URL patterns:".format(full_context['project_name']) in usage_file_txt
    assert "import {}".format(full_context['app_name']) in usage_file_txt
    assert "url(r'^', include({}.urls)),".format(full_context['app_name']) in usage_file_txt

# Test test files
def test_test_settings(cookies):
   """check if test project should have correct test settings"""
   result = cookies.bake(extra_context=full_context)
   test_settings_txt = result.project.join('tests', 'settings.py').read()
   assert "\"{}\",".format(full_context['app_name']) in test_settings_txt
    
def test_test_urls(cookies):
   """check if test project should have correct test url.py"""
   result = cookies.bake(extra_context=full_context)
   test_urls_txt = result.project.join('tests', 'urls.py').read()
   assert "url(r'^', include('{}.urls', namespace='{}')),".format(full_context['app_name'],full_context['app_name']) in test_urls_txt

def test_test_models(cookies):
   """check if test project should have correct test test_models.py"""
   result = cookies.bake(extra_context=full_context)
   test_models_txt = result.project.join('tests', 'test_models.py').read()
   assert "from {} import models".format(full_context['app_name']) in test_models_txt
   assert "class Test{}(TestCase):".format(full_context['app_name'].capitalize()) in test_models_txt

# Test project testing and migrations

def test_run_tests(cookies):
    """generated project should be able to generate migrations"""
    result = cookies.bake(extra_context=full_context)
    with result.project.as_cwd():
        args = ["python","runtests.py"]
        subprocess.check_call(args)

def test_make_migrations(cookies):
    """generated project should be able to generate migrations"""
    result = cookies.bake(extra_context=full_context)
    with result.project.as_cwd():
        args = ["python","manage.py","makemigrations",full_context['app_name']]
        subprocess.check_call(args)
        args = ["python","manage.py","migrate"]
        subprocess.check_call(args)

      

