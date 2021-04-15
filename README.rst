=============================
Django SVG Image Field
=============================

.. image:: https://badge.fury.io/py/django-svg-image-form-field.svg
    :target: https://badge.fury.io/py/django-svg-image-form-field

.. image:: https://travis-ci.org/artrey/django-svg-image-form-field.svg?branch=master
    :target: https://travis-ci.org/artrey/django-svg-image-form-field

.. image:: https://codecov.io/gh/artrey/django-svg-image-form-field/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/artrey/django-svg-image-form-field

A form field to handle validation of image + svg

Documentation
-------------

The full documentation is at https://django-svg-image-form-field.readthedocs.io.

Quickstart
----------

Install Django SVG Image Field::

    pip install django-svg-image-form-field

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_svg_image_form_field.apps.DjangoSvgImageFieldConfig',
        ...
    )

Add Django SVG Image Field's URL patterns:

.. code-block:: python

    from django_svg_image_form_field import urls as django_svg_image_field_urls


    urlpatterns = [
        ...
        url(r'^', include(django_svg_image_field_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements-dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
