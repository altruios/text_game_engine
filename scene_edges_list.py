from scene import SceneEdge
from item_list import get_item
# hidden checks
def sword_check(player=None):
    return not player.search_inventory("sword")



# walk functions - what happens when you walk a path
def edge0fn(player=None,display=None):
    display=display+"you wake up - only remembering the things you learned before\n"
    player.health=100;
    player.respawn=player.respawn+1;


def edge1fn(player=None,swung_sword=False,display=None):
    if not swung_sword:
        display=display+"you run and stumble on the ground, the dog chases you"
        player.health=player.health-50;

def edge2fn(player=None,display=None):
    display=display+"you walk down the street and the dog loses interest in you"
    if(sword_check(player)):
        print("you stumble on the ground")
        player.health=player.health-10
        print("you find a sword: do you take it?")
        opt = input("yes / no ? : ")
        if(opt == "y" or opt=="yes"):
            sword = get_item("sword")
            player.add_to_inventory(sword)
        display=display+"you get up and get to your front door\n"
    else:
        display=display+"you get up and get to your front door\n"

def e2hifn(player=None,display=None):
    if player:
        return player.respawn==0;
    return True
def edge3fn(player=None,display=None):
    if player:
        player.use("sword")
        print("the dog was killed")

_scene_edges = []
_scene_edges.append(SceneEdge("try again", edge0fn, False, 0, 1))
_scene_edges.append(SceneEdge("run",edge1fn, False, 1, 3))
_scene_edges.append(SceneEdge("walk",edge2fn, e2hifn, 1, 2))
_scene_edges.append(SceneEdge("nothing",edge0fn, False, 3, 0))
_scene_edges.append(SceneEdge("swing sword",edge3fn, sword_check, 3, 4))
_scene_edges.append(SceneEdge("nothing",edge0fn, False, 2, 0))