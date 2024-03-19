# regular package import
import lidar
# subpackage import with aliasing
import lidar.math as lm
# importing part + aliasing
from lidar.math import cartesian_length as cl


point_list = [(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 3, 3)]
point_cloud = lidar.PointCloud(point_list, (4, 4, 4))

# explicit generator
for point in point_cloud.point_cloud():
    print(point)

# PointCloud as iterable
for point in point_cloud:
    print(point)

print(lm.cartesian_length(0, 1, 0))
print(cl(0, 1, 0))
