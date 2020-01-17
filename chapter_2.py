import arcade
import settings
import os

sprite_scale = 0.5
wall_scaling = 0.1
wall_size = 10

movement_speed = 5
'''
class Dialogue:
    def __init__(self, center_x, center_y, width, height, text, font_size=18,
                 font_face="Arial", face_color=arcade.color.LIGHT_GRAY):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
'''
class Level:
    def __init__(self):
        self.wall_list = arcade.SpriteList()
        self.character_list = arcade.SpriteList()
        self.item_list = arcade.SpriteList()
        #self.dialogue_list = []
        #self.background = None


def setup_level_1():
    level = Level()

    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", wall_scaling)
    wall.left = 7 * wall_size
    wall.bottom = 5 * wall_size
    level.wall_list.append(wall)

    create_and_add_vertical_walls_to_list(3, 13, 24, level.wall_list)
    create_and_add_horiontal_walls_to_list(5, 200, 50, level.wall_list)

    prison_guard = arcade.Sprite("pics\prison_guard.png", sprite_scale)
    prison_guard.center_x = 200
    prison_guard.center_y = 300
    level.character_list.append(prison_guard)

    money = Item("pics\gold_1.png", 0.5)
    money.center_x = 400
    money.center_y = 25
    level.item_list.append(money)

    #conversation = Dialogue(200, 300, 10, 5, "Hi.")
    #level.dialogue_list.append(conversation)


    return level

def setup_level_2():
    level = Level()

    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",wall_scaling)
    wall.left = 15 * wall_size
    wall.bottom = 20 * wall_size
    level.wall_list.append(wall)

    create_and_add_vertical_walls_to_list(3, 13, 24, level.wall_list)
    create_and_add_horiontal_walls_to_list(5, 200, 50, level.wall_list)

    return level

def setup_level_3():
    level = Level()

    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", wall_scaling)
    wall.left = 7 * wall_size
    wall.bottom = 5 * wall_size
    level.wall_list.append(wall)

    return level


def create_and_add_vertical_walls_to_list(column_start: int, column_end: int, x: int, wall_list: arcade.SpriteList):
    for y in range(column_start * wall_size, column_end * wall_size, wall_size):
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", wall_scaling)
        wall.left = x * wall_size
        wall.bottom = y
        wall_list.append(wall)

def create_and_add_horiontal_walls_to_list(row_start: int, row_end: int, y: int, wall_list: arcade.SpriteList):
    for x in range(row_start * wall_size, row_end * wall_size, wall_size):
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", wall_scaling)
        wall.left = x
        wall.bottom = y * wall_size
        wall_list.append(wall)


class Item(arcade.Sprite):
    pass

class Chapter2View(arcade.View):

    def __init__(self):
        super().__init__()

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.current_level = 0
        self.inventory = 0
        

        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        self.levels = [
            setup_level_1(),
            setup_level_2(),
            setup_level_3()
        ]

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.levels[self.current_level].wall_list)

        arcade.set_background_color(arcade.color.AMAZON)
        

    def on_draw(self):
        arcade.start_render()
        self.levels[self.current_level].wall_list.draw()
        self.levels[self.current_level].character_list.draw()
        self.levels[self.current_level].item_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = movement_speed
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -movement_speed
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -movement_speed
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = movement_speed

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.levels[self.current_level].item_list)
        for item in hit_list:
            item.remove_from_sprite_lists()
            self.inventory += 1

        self.physics_engine.update()

        #go up
        if self.player_sprite.center_y > settings.HEIGHT and self.current_level == 0 and self.inventory == 1:  
            self.current_level = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.levels[self.current_level].wall_list)
            self.player_sprite.center_y = 0
        elif self.player_sprite.center_y > settings.HEIGHT and self.current_level == 0 and self.inventory == 0:  
            self.player_sprite.center_y = settings.HEIGHT

        elif self.player_sprite.center_y > settings.HEIGHT and self.current_level == 1:
            self.current_level = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.levels[self.current_level].wall_list)
            self.player_sprite.center_y = 0

        #go down
        elif self.player_sprite.center_y < 0 and self.current_level == 1:
            self.current_level = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.levels[self.current_level].wall_list)
            self.player_sprite.center_y = settings.HEIGHT
        elif self.player_sprite.center_y < 0 and self.current_level == 2:
            self.current_level = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.levels[self.current_level].wall_list)
            self.player_sprite.center_y = settings.HEIGHT

        #next view
        elif self.player_sprite.center_y > settings.HEIGHT and self.current_level == 2:
            self.director.next_view()
            #error in sys.excepthook when manually going to next view???

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

if __name__ == "__main__":
    """This section of code will allow you to run your View
    independently from the main.py file and its Director.

    You can ignore this whole section. Keep it at the bottom
    of your code.

    It is advised you do not modify it unless you really know
    what you are doing.
    """
    from utils import FakeDirector
    window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    my_view = Chapter2View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
