#!/bin/bash -xe

cd $(dirname $0)
mkdir -p build
rst2html5.py README.rst > build/README.html
dashing build -s build/
