#!/usr/bin/env python

from setuptools import setup, find_packages

# setup the project
setup(
    name="django-shop-richcatalog",
    version="1.1.0",
    author="Nimbis Services, Inc.",
    author_email="devops@nimbisservices.com",
    description="Rich catalog functionality for django shop.",
    license="BSD",
    packages=find_packages(exclude=["tests", ]),
    install_requires=[
        'Django',
        'django-shop >= 0.2.0',
        'django-cms',
        'django-shop-richproduct',
        'django-mptt',
        'image',
    ],
    zip_safe=False,
    include_package_data=True,
)
