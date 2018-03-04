#!/bin/bash
export FC=$(which $FC)
export CC=$(which $CC)
export CXX=$(which $CXX)
mkdir -p build
rm -rf build/*
${PYTHON} setup.py install -v --single-version-externally-managed --record record.txt

