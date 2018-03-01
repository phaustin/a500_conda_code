from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy
import os
from pathlib import Path

try:
    recipe_dir = os.environ['RECIPE_DIR']
except KeyError:
    recipe_dir="."

try:
    lib_prefix = os.environ['PREFIX']
except KeyError:
    lib_prefix = os.environ['CONDA_PREFIX']
    
readbin3D_pyx = Path(recipe_dir).parent / Path('sam_cython/readbin3D.pyx')
lib_dir = str(Path(lib_prefix) / Path('lib'))

extensions = [
    Extension(
        "sam_cython.readbin3D",
        [str(readbin3D_pyx)],
        include_dirs = [numpy.get_include()],
        libraries=['read3D','gfortran'],
        library_dirs=[lib_dir]
    ),
]

setup(
    name = "sam_cython",
    packages = find_packages(),
    ext_modules = cythonize(extensions)
)
