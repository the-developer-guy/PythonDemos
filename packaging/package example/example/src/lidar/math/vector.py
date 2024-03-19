import math

# azimuth: θ - theta
# polar: φ - phi

def print_global_x():
    print(x)

def cartesian_length(x, y, z):
    return (x ** 2 + y ** 2 + z ** 2) ** 0.5


def cartesian_to_spherical(distance, azimuth, polar):
    x = distance * math.sin(polar) * math.cos(azimuth)
    y = distance * math.sin(polar) * math.sin(azimuth)
    z = distance * math.cos(polar)
    return (x, y, z)


def spherical_to_cartesian(x, y, z):
    distance = cartesian_length(x, y, z)
    azimuth = math.atan(y / x)
    polar = math.atan(((x ** 2 + y ** 2) ** 0.5) / z)
    return (distance, azimuth, polar)
