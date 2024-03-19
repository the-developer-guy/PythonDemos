from lidar.everything import *
import lidar.everything
import lidar.everything as et

# import * works for f(), because it was set in __all__
f()

# lidar.everything.g can be accessed: imported in __init__.py
lidar.everything.g()

# aliasing also works fine
et.g()

# g was NOT included in __all__, this must fail
g()
