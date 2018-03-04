#!/bin/bash -v
#export PATH="/Users/phil/ana36/bin:$PATH"
export FC=$(which $FC)
export CC=$(which $CC)
export CXX=$(which $CXX)
pip install . -v
