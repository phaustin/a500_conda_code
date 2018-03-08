import subprocess
from pathlib import Path
import site
import sys
import shutil
import os


def clean_build(modulename,tmpdir='.tmpdir'):
    """
    do a clean build of the module in folder tmpdir

    Parameters
    ----------

    modulename: str
       name of module to build
    
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
    try: 
        shutil.rmtree(f'./{modulename}.egg-info')
    except FileNotFoundError:
        pass
    major, minor, *rest = sys.version_info
    command="python setup.py clean --all".split()
    out=subprocess.check_output(command,stderr=subprocess.STDOUT,universal_newlines=True)
    command=f"python setup.py install --prefix={tmpdir} --single-version-externally-managed --record=record.txt".split()
    out=subprocess.check_output(command,stderr=subprocess.STDOUT,universal_newlines=True)
    the_path= Path(f'{tmpdir}/lib/python{major}.{minor}/site-packages').resolve()
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
    
    with cd(cmakedir):
        command="cmake ..".split()
        out=subprocess.check_output(command,stderr=subprocess.STDOUT,universal_newlines=True)
        command="make install".split()
        out=subprocess.check_output(command,stderr=subprocess.STDOUT,universal_newlines=True)
        print(out)

    clean_build('sam_cython')
    import sam_cython
    print(f'installed sam_cython at {sam_cython.__file__}')
    from sam_cython.tests import testit
    
    

    
