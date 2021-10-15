# Making a game called Gothons From Planet Percal #25

#Space Adventure game

# Write or Draw About the Problem

"""Aliens have invaded a space ship and ourhero has to go through a maze
of rooms defeating them so he can escape into an escape pod to the
planet below. The game will be more like a Zork or Adventure type
game with text outputs and funny ways to die. The game will involve an engine that runs
a map full of rooms or scenes. Each room will print its own description when the player 
enters it and then tell the engine what room to run next out of the map."""

# Different scenes
"""
DEATH: When a player dies
CENTRAL CORRIDOR: This is the starting point and has a Gothon already standing
                    there that the players have to defeat with a joke before continuing
LASER WEAPON ARMORY: This is wehre the hero gets a neutron bomb to blow up the ship before getting to
                    escape pod. It has a keypad with a guessing game.
THE BRIDGE: Another battle scene with a Gothon where a hero places a bomb.
ESCAPE POD: Where the hero escapes but only after guessing the right escape pod.
"""

# Key Concepts
"""
NOUNS

Alien
Player
Ship
Maze
Room
Scene
Gothon
Escape Pod
Planet
Map
Engine
Death
Central Corridor
Laser Weapon Armory
The Bridge

VERBS
(Next time:D)
"""

"""
NOTES:

ROOM = SCENE

Lets go with scene.

because, DEATH is a scene, CENTRAL CORRIDOR is a scene, PLANET is a scene.

MAP = MAZE

no battles, so we can ignore alien and player, save it for later.


HIERARCHY:

MAP
Engine
SCENE
    DEATH
    CENTRAL CORRIDOR
    LASER WEAPON ARMORY
    THE BRIDGE
    ESCAPE POD

ACTIONS NEEDED:

MAP
    next_scene
    opening_Scene
Engine
    play
SCENE
    enter
    CENTRAL CORRIDOR
    LASER WEAPON ARMORY
    THE BRIDGE
    ESCAPE POD
"""