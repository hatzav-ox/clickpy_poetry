#!/bin/sh

pipenv run coverage html

if command -v open &> /dev/null
then
    open htmlcov/index.html
elif command -v start &> /dev/null
then
    start htmlcov/index.html
fi
