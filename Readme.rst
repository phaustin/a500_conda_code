Building pybind11 extensions using pip or conda
+++++++++++++++++++++++++++++++++++++++++++++++

Create an environment named test using miniconda3 (working with 4.10)
=====================================================================

* For osx::

    wget https://raw.githubusercontent.com/phaustin/pybind11_test/master/environment_osx.yml
    conda env create -f environment_osx.yml

* For linux::

    wget https://raw.githubusercontent.com/phaustin/pybind11_test/master/environment_linux.yml
    conda env create -f environment_linux.yml

* Activate it::

    conda activate test

Using pip
=========
    
* Do::
    
    conda activate test

    CXX=$(which $CXX);pip install git+https://github.com/phaustin/pybind11_test.git#egg=pybind_test

    mkdir test
    cd test
    python -c 'from hello_pybind.do_add import add_them;print(add_them(1,2))'

  prints::

    inside hello_pybind __init__.py
    3


Using conda
===========

* Clone the repo::

    git clone https://github.com/phaustin/pybind11_test.git
    pip uninstall hello-pybind  #(if necessary from above install)
    cd pyind11_test
    conda build .

* This should print out::

    running run_test.py
    inside hello_pybind __init__.py
    sum of 1 and 2: 3








