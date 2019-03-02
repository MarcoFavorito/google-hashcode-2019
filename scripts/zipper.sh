#!/usr/bin/env bash
rm solution.zip
zip -r solution.zip hashcode19/* README.md requirements.txt .gitignore LICENSE zipper.sh scripts/* SUBMISSION setup.py\
     data/.gitkeep out/.gitkeep -x *__pycache__* *.pyc