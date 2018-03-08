import subprocess
from pathlib import Path
import site
import sys
import shutil
import os


def clean_build(modulename):
    """
    do a clean build of the module in folder .tmpdir

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
        shutil.rmtree('./.tmpdir')
    except FileNotFoundError:
         pass
    try: 
        shutil.rmtree(f'./{modulename}.egg-info')
    except FileNotFoundError:
        pass
    major, minor, *rest = sys.version_info
    command="python setup.py clean --all".split()
    out=subprocess.check_output(command,stderr=subprocess.STDOUT,universal_newlines=True)
    command="python setup.py install --prefix=./.tmpdir --single-version-externally-managed --record=record.txt".split()
    out=subprocess.check_output(command,stderr=subprocess.STDOUT,universal_newlines=True)
    the_path= Path(f'./.tmpdir/lib/python{major}.{minor}/site-packages').resolve()
    sys.path.insert(0, str(the_path))
    site.removeduppaths()
    print(out)
    #print(sys.path)


if __name__ == "__main__":
    clean_build('make_unique')
    import make_unique
    print(f'instaled make_unique at {make_unique.__file__}')
    from make_unique.tests import test_pha
    

    
