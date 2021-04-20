#!/bin/sh

set -e

pip install --no-cache-dir -r requirements_dev.txt

py.test -l --tb=short -r fE /opt/resource/lib
py.test -l --tb=short -r fE /opt/resource-tests

rm -fr /tmp/*
pip uninstall -y -r requirements_dev.txt
