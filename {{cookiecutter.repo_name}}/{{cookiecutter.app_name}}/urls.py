# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

app_name = '{{ cookiecutter.app_name }}'
urlpatterns = [
    url(r'', TemplateView.as_view(template_name='base.html')),
]
