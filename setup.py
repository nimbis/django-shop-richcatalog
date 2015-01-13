from setuptools import setup, find_packages
from pip.req import parse_requirements
from uuid import uuid1


# parse requirements
reqs = parse_requirements("requirements/common.txt", session=uuid1())

# setup the project
setup(
    name="django-shop-richcatalog",
    version="0.4.1",
    author="Nimbis Services, Inc.",
    author_email="devops@nimbisservices.com",
    description="Rich catalog functionality for django shop.",
    license="BSD",
    packages=find_packages(exclude=["tests", ]),
    install_requires=[str(x).split(' ')[0] for x in reqs],
    zip_safe=False,
    include_package_data=True,
    test_suite="tests.main",
)
