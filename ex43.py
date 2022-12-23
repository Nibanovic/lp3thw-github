from sys import exit

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


# --------------

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
        enemy ship. There is an alien in front of you.
         
        Do you go left or right?
        """)

        action = input("> ")

        if action == "left":
            print("""
            The alien has caught and eaten you.
            """)
            return "death"
        elif action == "right":
            print("""
            You manage to reach the door on the right
            """)
            return "bridge"
        else:
            print("I don't know what that means")


class LaserWeaponArmory(Scene):

    def enter(self):
        print("""
        You find yourself in the laser weapon armory. 

        take bomb or not?
        """)

        action = input("> ")

        if action == 'take':
            print("""
            It is cold to the touch and rumbles faintly. You arm the
            pod and make it to the escape pod.
            """)
            return 'escape_pod'
        elif action == 'not':
            print("""
            The Alien catches up with you and you die.
            """)
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print("""
        You have reached the bridge of the ship. On the console you
        notice that one escape pod has left. Additionally, you
        see that there is a neutron bomb in the armory.
        
        Do you go to the escape pod or the armory?
        """)

        action = input("> ")

        if action == "pod":
            return "death"
        elif action == "armory":
            print("""
            You dash for the armory.
            """)
            return "laser_weapon_armory"
        else:
            print("I don't know what that means.")
            return "bridge"


class EscapePod(Scene):

    def enter(self):
        print("""
        You managed to reach the Escape Pod. There is a keypad next
        to it - a four letter password is required. The top-right 
        button seems to be worn out. What is the password?
        """)

        action = input("> ")

        if action == "1111" or "takemeaway":
            print("""
            The pod doors clock open and pressurize.
            You enter quickly and hit the eject button. The pod
            whizzes into space just as the alien ship explodes
            into a million pieces.
            """)
            return 'finished'
        else:
            print("""
            You've fumbled for too long - the Alien ate you.
            """)
            return 'death'


class Finished(Scene):

    def enter(self):
        print("\nYou've won! Good Job.")
        exit(1)



class Map(object):

    # all of the scenes are stored in a dictionary
    # ovaj se zove mapa jer su sve scene zakodirane ovdje
    scenes = {
        'finished': Finished(),
        'death': Death(),
        'central_corridor': CentralCorridor(),
        'bridge': TheBridge(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'escape_pod': EscapePod(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, next_scene):
        # preuzmi sljedeću scenu iz riječnika, vraća objekt te scene
        return self.scenes.get(next_scene)

    def opening_scene(self):
        # otvori sa input scenom
        return self.next_scene(self.start_scene)

class Engine(object):

    # otvori stvori si mapu
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        # otvori prvu scenu
        current_scene = self.scene_map.opening_scene()
        # i otvori zadnju scenu
        last_scene = self.scene_map.next_scene('finished')

        # sve dok prva nije jednaka zadnjoj,
        while current_scene != last_scene:
            #sljedeća scena je
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #last print out last scene
        current_scene.enter()


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()




