#!/bin/sh

set -e

pip install --no-cache-dir -r requirements_dev.txt

py.test -l --tb=short -vv -r fEP /opt/resource/lib
py.test -l --tb=short -vv -r fEP /opt/resource-tests

rm -fr /tmp/*
pip uninstall -y -r requirements_dev.txt
