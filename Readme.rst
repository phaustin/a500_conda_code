Building cython and pybind11 extensions using pip or conda
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Create an environment named test using miniconda3 (working with 4.10)
=====================================================================

* clone the repo::

   git clone https://github.com/phaustin/a500_conda_code.git

* For osx::

    conda env create -f environment_osx.yml

* For linux::

    conda env create -f environment_linux.yml

* Activate it::

    conda activate test

Building pybind11_basic
=======================

::

   cd a500_conda_code/pybind11_basic


Using pip
---------
    
* Do::
    
    CXX=$(which $CXX);pip install .

    mkdir test
    cd test
    python -c 'from hello_pybind.do_add import add_them;print(add_them(1,2))'

  prints::

    inside hello_pybind __init__.py
    3


Using conda
-----------

build it::

    pip uninstall hello-pybind  #(if necessary from above install)
    conda build .

* This should print out::

    running run_test.py
    inside hello_pybind __init__.py
    sum of 1 and 2: 3

Building sam_cython
===================

::

   cd a500_conda_code/sam_cython


Using pip
---------
    
* Compile and install the fortran library::

    mkdir build
    cd build
    cmake ..
    make install

* Install the package::    

    cd ..
    CC=$(which $CC) FC=$(which $FC) pip install .

    cd build
    python -c 'from sam_cython.tests import testit'

  prints::

    inside  __init__.py
    ------ test started ---------
    here is a long filename the end
    [-9.990e+02 -9.999e+03  3.000e+00  4.000e+00  5.000e+00]
    --------- test completed ---------



Using conda
-----------

build it::

    pip uninstall sam-cython  #(if necessary from above install)
    conda build .

* This should print out::

    ===== testing package: sam_cython-0.0.1-py36hdc02c5d_2 =====
    running run_test.py
    inside  __init__.py
    ------ test started ---------
    here is a long filename the end
    [-9.990e+02 -9.999e+03  3.000e+00  4.000e+00  5.000e+00]
    --------- test completed ---------
    finished test
    ===== sam_cython-0.0.1-py36hdc02c5d_2 OK =====
  

Building pybind11_unique
========================

::

   cd a500_conda_code/pybind11_unique


Using pip
---------
    
* Do::
    
    CXX=$(which $CXX) pip install .

    mkdir build
    cd build
    python -c 'from make_unique.tests import testit'

  prints::

    inside make_unique __init__.py
    init file triggered
    testing double
    original vector: [0. 5. 5. 1. 2. 2. 2. 3. 4. 4. 4. 4. 4. 5.]
    after call:  [0. 1. 2. 3. 4. 5. 5.]
    testing float
    original vector: [0. 5. 5. 1. 2. 2. 2. 3. 4. 4. 4. 4. 4. 5.]
    after call:  [0. 1. 2. 3. 4. 5. 5.]
    testing int64_t
    original vector: [0 5 5 1 2 2 2 3 4 4 4 4 4 5]
    after call:  [0 1 2 3 4 5 5]
    testing int32_t
    original vector: [0 5 5 1 2 2 2 3 4 4 4 4 4 5]
    after call:  [0 1 2 3 4 5 5]


Using conda
-----------

build it::

    pip uninstall make-unique  #(if necessary from above install)
    conda build .

* This should print out::

    ===== testing package: cpp_make_unique-0.1-py36h0a44026_0 =====
    running run_test.py
    inside make_unique __init__.py
    init file triggered
    testing double
    original vector: [0. 5. 5. 1. 2. 2. 2. 3. 4. 4. 4. 4. 4. 5.]
    after call:  [0. 1. 2. 3. 4. 5. 5.]
    testing float
    original vector: [0. 5. 5. 1. 2. 2. 2. 3. 4. 4. 4. 4. 4. 5.]
    after call:  [0. 1. 2. 3. 4. 5. 5.]
    testing int64_t
    original vector: [0 5 5 1 2 2 2 3 4 4 4 4 4 5]
    after call:  [0 1 2 3 4 5 5]
    testing int32_t
    original vector: [0 5 5 1 2 2 2 3 4 4 4 4 4 5]
    after call:  [0 1 2 3 4 5 5]
    ===== cpp_make_unique-0.1-py36h0a44026_0 OK =====
    
    
    running run_test.py
    inside hello_pybind __init__.py
    sum of 1 and 2: 3
    






