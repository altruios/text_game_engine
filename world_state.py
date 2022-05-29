from scene import *
import item
from scene_edges_list import _scene_edges
from scene_list import _scene_list
print("worldstate");
Sg = SceneGraph()
for x in _scene_list:
    Sg.add(x)
for x in _scene_edges:
    Sg.add(edge=x)

Sg.set_visible_node(1)
Sg.set_visible_edges()



