Show how to use pybind11 to wrap c++ standard library calls in src/main.cpp and tests/test_pha.py

1) source activate root

conda install numpy
condat install cmake
conda install -c conda-forge xtensor-python
conda install gcc_linux-64 gxx_linux-64 gfortran_linux-64

to build with pip:

pip install . -v

to test:

python pybind11_unique/tests/test_pha.py

should print:

testing double
original vector: [0. 5. 5. 1. 2. 2. 2. 3. 4. 4. 4. 4. 4. 5.]
after call:  [0. 1. 2. 3. 4. 5.]
testing float
original vector: [0. 5. 5. 1. 2. 2. 2. 3. 4. 4. 4. 4. 4. 5.]
after call:  [0. 1. 2. 3. 4. 5.]
testing int64_t
original vector: [0 5 5 1 2 2 2 3 4 4 4 4 4 5]
after call:  [0 1 2 3 4 5]
testing int32_t
original vector: [0 5 5 1 2 2 2 3 4 4 4 4 4 5]
after call:  [0 1 2 3 4 5]


