from sys import exit
from random import randint
from textwrap import dedent

class Map(object):

    def __init__(self, start_scene):
        pass
    def next_scene(self):
        pass
    def opening_scene(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

#--------------

class Death(Scene):

    def enter(self):
        print("""
        You have died.
        """)
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print("""
        You've found yourself in a dark, damp corridor of the
        enemy ship.
        """)

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass



a_map = Map('death')
a_game = Engine(a_map)
a_game.play()




