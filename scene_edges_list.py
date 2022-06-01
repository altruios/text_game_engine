from scene import SceneEdge
from item_list import get_item
# hidden checks
def sword_check(player=None):
    return not player.search_inventory("sword")



# walk functions - what happens when you walk a path
def edge0fn(player=None,display=None):
    display(1,"you wake up - only remembering the things you learned before\n")
    player.health=100;
    player.respawn=player.respawn+1;


def edge1fn(player=None,swung_sword=False,display=None):
    if not swung_sword:
        display(1,"you run and stumble on the ground, the monster chases you\n")
        player.health=player.health-50;

def edge2fn(player=None,display=None):
    display(1,"you walk down the street and the monster loses interest in you\n")
    if(sword_check(player)):
        display(1,"you stumble on the ground\n",add=True)
        player.health=player.health-10
        display(0,"-10 health",add=True)
        display(1,"you find a sword: do you take it?\n",add=True)
        opt = input("yes / no ? : ")
        if(opt == "y" or opt=="yes"):
            sword = get_item("sword")
            player.add_to_inventory(sword)
    display(1,"you get up and get to your front door\n",add=True)
    
def e2hifn(player=None,display=None):
    if player:
        return player.respawn==0;
    return True
def edge3fn(player=None,display=None):
    if player:
        player.use("sword")
        display(0,"the monster was killed\n")

_scene_edges = []
_scene_edges.append(SceneEdge("try again", edge0fn, False, 0, 1))
_scene_edges.append(SceneEdge("run",edge1fn, False, 1, 3))
_scene_edges.append(SceneEdge("walk",edge2fn, e2hifn, 1, 2))
_scene_edges.append(SceneEdge("nothing",edge0fn, False, 3, 0))
_scene_edges.append(SceneEdge("swing sword",edge3fn, sword_check, 3, 4))
_scene_edges.append(SceneEdge("nothing",edge0fn, False, 2, 0))