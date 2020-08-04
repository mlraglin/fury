import numpy as np
from fury import actor, window, ui, utils, pick, primitive

vertices, triangles = primitive.prim_sphere(name='symmetric362',
                                            gen_faces=False)
colors = np.array([0.5, 0.0, 0.0])
centers = np.array([0.0, 0.0, 0.0])

selected = np.zeros(1, dtype=np.bool)

scene = window.Scene()
sphere_actor = actor.get_actor_from_primitive(vertices, triangles, colors)

vertices = utils.vertices_from_actor(sphere_actor)
num_vertices = vertices.shape[0]
num_objects = centers.shape[0]

vcolors = utils.colors_from_actor(sphere_actor, 'colors')
scene.add(sphere_actor)

pickm = pick.PickingManager()

def left_click_callback(obj, event):
    event_pos = pickm.event_position(showm.iren)
    picked_info = pickm.pick(event_pos, showm.scene)

    vertex_index = picked_info['vertex']

    object_index = np.int(np.floor((vertex_index / num_vertices) *
                          num_objects))
    sec = np.int(num_vertices / num_objects)

    if not selected[object_index]:
        color_add = np.array([0.5, 0.0, 0.0])
        selected[object_index] = True
    else:
        color_add = np.array([-0.5, 0.0, 0.75])
        selected[object_index] = False

    vcolors[object_index * sec: object_index * sec + sec] += color_add
    utils.update_actor(sphere_actor)

    showm.render()

sphere_actor.AddObserver('LeftButtonPressEvent', left_click_callback, 1)


showm = window.ShowManager(scene,
                           size=(900, 768), reset_camera=False,
                           order_transparent=True)
showm.initialize()

interactive = True
if interactive:
    showm.start