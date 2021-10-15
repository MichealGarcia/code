# Create class scene, it has-a function enter
class Scene(object):

    def enter(self):
        pass

# create class Engine, it has-a init with param self, scene_map. and has-a function
# play
class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

# Create a class Death that is-a scene, and has-a function enter with param self
class Death(Scene):

    def enter(self):
        pass

# create class CentralCorridor that is-a Scene, that has-a function enter with param self
class CentralCorridor(Scene):

    def enter(self):
        pass

# crate class LaserWeaponArmory that is-a Scene, that has-a function enter param self
class LaserWeaponArmory(Scene):

    def enter(self):
        pass

#Create a class TheBridge that is-a Scene, and has-a function enter param self
class TheBridge(Scene):

    def enter(self):
        pass

# class EscapePod is-a Scene, that has-a enter function param self
class EscapePod(Scene):

    def enter(self):
        pass

# Create a class Map that has-a init param self and start_scene
# and has-a function next_scene with param self, scene_name
# and has-a fucntion opening_scene param self
class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass
    def opening_scene(self):
        pass

#Create an instance called a_map in the 'central corridor'
a_map = Map('central_corridor')
#Create an instance of Engine eith param a_map
a_game = Engine(a_map)
#with a_game, call function play
a_game.play()
