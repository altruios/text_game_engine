import os
clear = lambda: os.system("clear")
from player import Player
from world_state import Ws
clear()
Ws.title_screen();
name = input("what is your name?   :")
P = Player(name)
Ws.add_player(P)
Ws.play()