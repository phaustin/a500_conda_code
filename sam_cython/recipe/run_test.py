#!/usr/bin/env python
import site, os
from pathlib import Path
recipe_dir=Path(os.environ['RECIPE_DIR'])
site.addsitedir(recipe_dir)
import tests.testit
print('finished test')




