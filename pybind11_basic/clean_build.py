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
    command=f"python -m pip install --target={tmpdir} --no-deps --ignore-installed .".split()
    out=subprocess.check_output(command,stderr=subprocess.STDOUT,universal_newlines=True)
    the_path= Path(f'{tmpdir}').resolve()
    sys.path.insert(0, str(the_path))
    site.removeduppaths()
    print(out)

if __name__ == "__main__":
    clean_build('hello_pybind')
    import hello_pybind
    print(f'installed hello_pybind at {hello_pybind.__file__}')
    from hello_pybind.do_add import add_them
    print(f'testing: 1 + 2 = {add_them(1,2)}')

    

    
