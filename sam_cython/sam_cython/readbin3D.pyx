"""
test doc
"""
# cython: c_string_type=str, c_string_encoding=ascii

from numpy cimport ndarray
from numpy import empty
import numpy as np

cdef extern:
    void c_reader(char *filename, int *len_filename,  int *N, double *the_array)

def readbin3D(str filename,  int N):
    """
    signature is readbin3D(str filename, int N)
    """
    py_byte_string = filename.encode('ascii')
    cdef char* c_string = py_byte_string
    cdef ndarray[double, mode="c"] the_array = empty(N, dtype=np.double)
    cdef int numchars= len(filename)
    c_reader(c_string,&numchars, &N, &the_array[0])
    return the_array
    

