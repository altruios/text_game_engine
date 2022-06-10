from scene import SceneNode
_scene_list=[]

title_screen_lines=[
    "     ____      ____      ____      ____      ____ ",
    "    /xxxx\\    /xxxx\\    /xxxx\\    /xxxx\\    /xxxx\\",
    "    |xHxx|    |xHxx|    |xHxx|    |xHxx|    |xHxx|",
    "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm",
    "                TEXT ADVENTURE ENGINE             ",
]
t = ""
for line in title_screen_lines:
    t = t+line+"\n"




_scene_list.append(SceneNode("you find yourself in a dark place - nothing around you, you feel nothing", 0))
_scene_list.append(SceneNode("you walk across the road to a tree, a monster is there, it chases you: ", 1))
_scene_list.append(SceneNode("inside the victorian exterior is a poorly lit mansion,\n there's a staircase to your left, and a kitchen door in front of you", 2))
_scene_list.append(SceneNode("the monster is mauling you - there is a child running toward you", 3))
_scene_list.append(SceneNode("the monster lays dead on top of you, the child is crying", 4))
_scene_list.append(SceneNode("the floor creaks and the mold is everywhere.\nin front of you are two ivory marbles upon a small pedistal\n one is green, and one is orange",5))
_scene_list.append(SceneNode("the kitchen is dark - and the stove is still on - a pot is just starting to wistle", 6))
_scene_list.append(SceneNode("you have failed",-1))
_scene_list.append(SceneNode(t,"TITLE"))
