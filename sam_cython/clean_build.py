import subprocess
from pathlib import Path
import site
import sys
import shutil
import os

def clean_build(tmpdir='.tmpdir'):
    """
    do a clean build of the module in folder tmpdir

    Parameters
    ----------

    tmpdir: str
       name of directory for the install target
    
    Returns:
       None -- builds module as side effect
    """
    #
    #
    #
    try:
        shutil.rmtree(tmpdir)
    except FileNotFoundError:
         pass
    command=f"python -m pip -v install --target={tmpdir} --no-deps --ignore-installed .".split()
    out=subprocess.check_output(command,stderr=subprocess.STDOUT,universal_newlines=True)
    the_path= Path(f'{tmpdir}').resolve()
    sys.path.insert(0, str(the_path))
    site.removeduppaths()
    print(out)

from contextlib import contextmanager
@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(newdir)
    try:
        yield
    finally:
        os.chdir(prevdir)

    
if __name__ == "__main__":

    cmakedir='./.cmakebuild'

    teardown=True

    if teardown:
        try:
            shutil.rmtree(cmakedir)
        except FileNotFoundError:
             pass
        os.makedirs(cmakedir)
    #
    # build the fotran library
    #
    with cd(cmakedir):
        command="cmake ..".split()
        out=subprocess.check_output(command,stderr=subprocess.STDOUT,universal_newlines=True)
        command="make install".split()
        out=subprocess.check_output(command,stderr=subprocess.STDOUT,universal_newlines=True)
        print(out)

    #
    # now build the pybind11 extension and call it
    #
    clean_build()
    import sam_cython
    print(f'installed sam_cython at {sam_cython.__file__}')
    from sam_cython.tests import testit
    
    

    
