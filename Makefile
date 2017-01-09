
.PHONY: db test pep8 clean doc check-venv check-reqs

# clean out potentially stale pyc files
clean:
	@find . -name "*.pyc" -exec rm {} \;

# check that virtualenv is enabled
check-venv:
ifndef VIRTUAL_ENV
	$(error VIRTUAL_ENV is undefined, try "workon" command)
endif

# Install pip requirements.txt file
reqs: check-venv
	pip install -r requirements.txt

# Show all occurence of same error
# Exclude the static directory, since it's auto-generated
PEP8_OPTS=--repeat --exclude=static,migrations,south_migrations,js,doc --show-source

pep8: check-venv
	python setup.py pep8 $(PEP8_OPTS)

test: check-venv clean
	python manage.py test --keepdb

# flake8
#

FLAKE8_OPTS = --max-complexity 10 --exclude='doc,dist,build,htmlcov,migrations,south_migrations'
flake8: check-venv
	flake8 $(FLAKE8_OPTS) . | tee flake8.log

#
# doc
#

doc: check-venv
	cd doc; make html
	@echo "See ./doc/_build/index.html for html documentation."

#
# code coverage
#

COVERAGE_INCLUDE='shop_richcatalog/*'

coverage: check-venv
	coverage erase
	-coverage run --include=$(COVERAGE_INCLUDE) ./manage.py test --keepdb
	coverage report
	coverage html
	@echo "See ./htmlcov/index.html for coverage report"
