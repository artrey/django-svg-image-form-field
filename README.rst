=============================
Django SVG Image Field
=============================

.. image:: https://badge.fury.io/py/django-svg-image-form-field.svg
    :target: https://badge.fury.io/py/django-svg-image-form-field

A form field to handle validation of image + svg

Quickstart
----------

Install Django SVG Image Field::

    pip install django-svg-image-form-field

Models:

.. code-block:: python

    from django.db import models


    class Article(models.Model):
        title = models.CharField(max_length=100)
        image = models.ImageField(upload_to='images/articles')
        text = models.TextField()

Forms:

.. code-block:: python

    from django import forms

    from .models import Article
    from django_svg_image_form_field import SvgAndImageFormField


    class ArticleForm(forms.ModelForm):
        class Meta:
            model = Article
            exclude = []
            field_classes = {
                'image': SvgAndImageFormField,
            }

Example usage:

.. code-block:: python

    from django.contrib import admin

    from .forms import ArticleForm
    from .models import Article


    @admin.register(Article)
    class SectionAdmin(admin.ModelAdmin):
        list_display = 'id', 'title'
        search_fields = 'title',
        form = ArticleForm

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
