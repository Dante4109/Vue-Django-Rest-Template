## PHONY tells make not to look for a file definition and use commands defined within this file
.PHONY: help test flake8 coverage test-all pull commit push print docs install dev
.DEFAULT_GOAL := help

WHITE 	= [0m
RED 	= [91m
GREEN 	= [92m
YELLOW 	= [93m
BLUE 	= [94m
MAGENTA = [95m
CYAN 	= [96m

ifeq ($(OS),Windows_NT)
    #Windows stuff
    REMOVE = rmdir
	REMOVE_FLAGS = /s /Q
else
    #Linux stuff
    REMOVE = rm
	REMOVE_FLAGS = -f
endif

branch := $(shell git rev-parse --abbrev-ref HEAD)

ifeq ($(branch),master)
$(error Work must be completed on a feature branch but the repo is currently looking at master)
endif

help:
	@echo ${CYAN}"DEV:-----------------------------------------------------------------"
	@echo "   flake8   --> run current linting process on source code and tests"
	@echo "   coverage --> build the testing coverage report"
	@echo "   test-all --> run both linting and unit tests"
	@echo "   test     --> run unit tests"
	@echo "   docs     --> build the source code documentation"
	@echo "GIT:-----------------------------------------------------------------"
	@echo "   pull            --> pull master into current branch"
	@echo "   commit msg=''   --> commit your changes (auto-staged)"
	@echo "   push            --> push your changes"
	@echo "MISC:----------------------------------------------------------------"
	@echo "   install  --> install the package (non-editable)"
	@echo "   dev      --> install the package (editable)"
	@echo "---------------------------------------------------------------------"${WHITE}

## run tests quickly with the default Python
test:
	python setup.py test
	@echo ${GREEN}Unit Tests Passed${WHITE}

## check style with flake8
flake8:
	flake8 VDRF
	@echo ${GREEN}Source Code Linting Passed${WHITE}
	flake8 tests
	@echo ${GREEN}Test Code Linting Passed${WHITE}

## check code coverage quickly with the default Python
coverage:
	coverage run --omit=*__init__.py --source VDRF setup.py test
	@echo ${GREEN}Unit Tests Passed${WHITE}
	coverage xml
	coverage html
	coverage report -m --fail-under=95 --omit=*__init__.py
	@echo ${GREEN}Coverage Percentage Passed${WHITE}

## run our tests including coverage
test-all:
	flake8 VDRF
	@echo ${GREEN}Source Code Linting Passed${WHITE}
	flake8 tests
	@echo ${GREEN}Test Code Linting Passed${WHITE}
	coverage run --omit=*__init__.py --source VDRF setup.py test
	@echo ${GREEN}Unit Tests Passed${WHITE}
	coverage xml
	coverage html
	coverage report -m --fail-under=95 --omit=*__init__.py
	@echo ${GREEN}Coverage Percentage Passed${WHITE}
	@echo ${GREEN}Congrats :) ${WHITE}

## Pull main from server and merge into feature branch
update:
	git switch main
	@echo ${GREEN}Switched Back to Main Branch${WHITE}
	git pull --commit
	@echo ${GREEN}Pulled Main Branch from Server${WHITE}
	git switch $(branch)
	@echo ${GREEN}Switched Back to Feature Branch: $(branch)${WHITE}
	git merge --commit Main
	@echo ${GREEN}Merged Main Branch into Feature Branch: $(branch)${WHITE}

## Stage and commit current changes to feature branch
commit:
	git add -A
	@echo ${GREEN}Staged All Changes for Feature Branch: $(branch)${WHITE}
	git commit -m "$(msg)"
	@echo ${GREEN}Committed All Changes for Feature Branch: $(branch)${WHITE}

## Runs flake8, unit tests, coverage report before publish/pushing feature branch to the server
push:
	flake8 VDRF
	@echo ${GREEN}Source Code Linting Passed${WHITE}
	flake8 tests
	@echo ${GREEN}Test Code Linting Passed${WHITE}
	coverage run --omit=*__init__.py --source VDRF setup.py test
	@echo ${GREEN}Unit Tests Passed${WHITE}
	coverage xml
	coverage html
	coverage report -m --fail-under=95 --omit=*__init__.py
	@echo ${GREEN}Coverage Percentage Passed${WHITE}
	git push -u origin $(branch)
	@echo ${GREEN}Pushed Feature Branch: $(branch)${WHITE}

print:
	@echo $(msg)

## generate Sphinx HTML documentation, including API docs
docs:
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

install:
	pip install pipenv
	pipenv install -e .
	python setup.py install
	@echo ${GREEN}Installation Completed :) ${WHITE}

dev:
	pip install pipenv
	pipenv install -e .
	python setup.py install
	@echo ${GREEN}Installation Completed :) ${WHITE}
	python setup.py develop
	@echo ${GREEN}Now in Development Mode ${WHITE}

dev_live:
	@echo ${YELLOW}Running in Development Mode...${WHITE}
	@echo "Starting both npm and Python servers concurrently..."
	npm run dev  & # Runs npm server in the foreground
	python manage.py runserver # Runs Python server in the foreground
	@echo ${GREEN}Development Servers Started${WHITE}

# Example Makefile
PROJECT_ROOT := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

all:
		@echo "Current directory: $(PWD)"
		@echo "Project root: $(PROJECT_ROOT)"
		$(MAKE) -C $(PROJECT_ROOT) actual_target

actual_target:
		@echo "Now in the project root for actual_target"
		# Commands that rely on being in the project root
		# e.g., compile source files, run tests