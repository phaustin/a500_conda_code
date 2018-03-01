#!/bin/bash

export FC=$(which $FC)
export CC=$(which $CC)
export CXX=$(which $CXX)
mkdir -p build
cd build
rm -rf *
cmake -D INSTALL_DIR=$PREFIX ..
make VERBOSE=1
make install VERBOSE=1
cd ..
echo "pha running ${PYTHON}"
${PYTHON} setup.py install -v --single-version-externally-managed --record record.txt

