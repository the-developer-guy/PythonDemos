from lidar.everything import *
import lidar.everything
import lidar.everything as et

from lidar.everything.demo import *
# or: from lidar.everything.demo import h

# import * works for f(), because it was set in __all__
f()

# lidar.everything.g can be accessed: imported in __init__.py
lidar.everything.g()

# aliasing also works fine
et.g()

h()

# _i is hidden from "import *"
_i()

# g was NOT included in __all__, this must fail
g()
