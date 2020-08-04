from fury import primitive, window, actor
import numpy as np

scene = window.Scene()
verts, faces = primitive.prim_torus_vertices(roundness=(1, 1))
torus_actor = actor.surface(verts, faces)
torus_actor.GetProperty().BackfaceCullingOff()
dots = actor.dots(verts)
scene.add(dots)
scene.add(torus_actor)

window.show(scene, size=(600, 600))
