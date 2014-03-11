from setuptools import setup, find_packages
from pip.req import parse_requirements

# parse requirements
reqs = parse_requirements("requirements/common.txt")

# setup the project
setup(
    name="django-shop-richcatalog",
    version="0.3.0",
    author="Nimbis Services, Inc.",
    author_email="info@nimbisservices.com",
    description="Rich catalog functionality for django shop.",
    license="BSD",
    packages=find_packages(exclude=["tests", ]),
    install_requires=[str(x).split(' ')[0] for x in reqs],
    zip_safe=False,
    include_package_data=True,
    test_suite="tests.main",
)
