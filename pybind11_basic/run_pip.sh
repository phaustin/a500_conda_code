#!/bin/bash -v
export FC=$(which $FC)
export CC=$(which $CC)
export CXX=$(which $CXX)
pip install . -v
