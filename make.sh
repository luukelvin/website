#!/bin/sh

mkdir -p docs
cd app
python3 manage.py distill-local --force --collectstatic ../docs
cd ../docs
touch .nojekyll
cd ..
cp -r docs/* $DISTILL_DIR
rm -rf docs
