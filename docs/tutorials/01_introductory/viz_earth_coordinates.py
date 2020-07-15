
"""
============================
Earth Coordinate Conversion
============================

In this tutorial, we will show how to place actors on specific locations
on the surface of the Earth using a new function.
"""

from fury import window, actor, utils, io
from fury.data import read_viz_textures, fetch_viz_textures
import math
import numpy as np

###############################################################################
# Create a new scene, and load in the image of the Earth using
# ``fetch_viz_textures`` and ``read_viz_textures``. We will use a 16k
# resolution texture for maximum detail.

scene = window.Scene()

fetch_viz_textures()
earth_file = read_viz_textures("1_earth_16k.jpg")
earth_image = io.load_image(earth_file)
earth_actor = actor.texture_on_sphere(earth_image)
scene.add(earth_actor)

###############################################################################
# Rotate the Earth to make sure the texture is correctly oriented. Change it's
# scale using ``actor.SetScale()``.

utils.rotate(earth_actor, (-90, 1, 0, 0))
utils.rotate(earth_actor, (180, 0, 1, 0))
earth_actor.SetScale(2, 2, 2)

###############################################################################
# Define the function to convert geographical coordinates of a location in
# latitude and longitude degrees to coordinates on the ``earth_actor`` surface.
# In this function, convert to radians, then to spherical coordinates, and
# lastly, to cartesian coordinates.

def latlong_coordinates(lat, lon):
    #Convert latitude and longitude to spherical coordinates
    degrees_to_radians = math.pi/180.0
    #phi = 90 - latitude
    phi = (90-lat)*degrees_to_radians
    #theta = longitude
    theta = lon*degrees_to_radians*-1
    #r is radius 1
    #now convert to cartesian
    x = np.sin(phi)*np.cos(theta)
    y = np.sin(phi)*np.sin(theta)
    z = np.cos(phi)
    # flipping z to y for FURY coordinates
    return (x, z, y)


###############################################################################
# Let's use this function to place some sphere actors on several locations
# around the Earth.

locationone = latlong_coordinates(39.1636505, -86.525757) #bloomington
locationtwo = latlong_coordinates()
locationthree = latlong_coordinates()

centers = np.array([[*locationone, *locationtwo, *locationthree]])
radius = 0.005
colors = np.random.rand(1, 3)
sphere_actor = actor.sphere(centers, colors, radius)
scene.add(sphere_actor)

window.show(scene, size=(900, 768))