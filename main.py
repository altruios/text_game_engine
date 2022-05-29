import os
clear = lambda: os.system("clear")
from player import Player
from world_state import Sg
clear()
name = input("what is your name?   :")
P = Player(name)
Sg.play(P)