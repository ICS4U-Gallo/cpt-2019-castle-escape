import arcade
import settings
import os

sprite_scale = 0.5
wall_scaling = 0.1
wall_size = 10
movement_speed = 5


class Dialogue:
    def __init__(self, center_x: float, center_y: float, width: float, height: float, text: str, font_size: int=18,
                 font_face: str="Arial", color: str=arcade.color.LIGHT_GRAY):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.color = color

    def draw(self):
        if not self.pressed:
            arcade.draw_rectangle_filled(self.center_x, self.center_y, 20, 20, arcade.color.ALABAMA_CRIMSON)
            arcade.draw_text("?", self.center_x, self.center_y, arcade.color.BLACK, anchor_x="center", anchor_y="center")
        else:
            arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
            arcade.draw_text(self.text, self.center_x, self.center_y, arcade.color.BLACK, anchor_x="center", anchor_y="center")
   
    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False


class RoomInfo:
    def __init__(self, center_x: float, center_y: float, text: str, width: float=20, height: float=20, font_size: str=18,
                 font_face: str="Arial", color: str=arcade.color.LIGHT_GRAY):
        self.center_x = center_x
        self.center_y = center_y
        self.text = text
        self.width = width
        self.height = height
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.color = color
    def draw(self):
        arcade.draw_rectangle_filled(settings.WIDTH//2, settings.HEIGHT - 15, settings.WIDTH, 30, arcade.color.ANTIQUE_BRASS)
        if not self.pressed:
            arcade.draw_rectangle_filled(self.center_x, self.center_y, 20, 20, arcade.color.ANTIQUE_BRASS)
            arcade.draw_text("?", self.center_x, self.center_y, arcade.color.BLACK, anchor_x="center", anchor_y="center")
        else:
            arcade.draw_text(self.text, 10, settings.HEIGHT - 10, arcade.color.BLACK, anchor_x="left", anchor_y="top")
    def on_press(self):
        self.pressed = True
    def on_release(self):
        self.pressed = False

def check_mouse_press_for_buttons(x, y, button_list):
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()

def check_mouse_release_for_buttons(_x, _y, button_list):
    for button in button_list:
        if button.pressed:
            button.on_release()

class Level:
    def __init__(self):
        self.wall_list = arcade.SpriteList()
        self.character_list = arcade.SpriteList()
        self.item_list = arcade.SpriteList()
        self.dialogue_list = []
        self.room_info_list = []
        #self.background = None

def setup_level_1():
    level = Level()

    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", wall_scaling)
    wall.left = 7 * wall_size
    wall.bottom = 5 * wall_size
    level.wall_list.append(wall)

    create_and_add_vertical_walls_to_list(3, 13, 24, level.wall_list)
    create_and_add_horiontal_walls_to_list(5, 200, 50, level.wall_list)
    create_and_add_character_to_list("pics\prison_guard.png", 200, 300, level.character_list)
    create_and_add_item_to_list("pics\gold_1.png", 0.5, 400, 25, level.item_list)

    cell_info = RoomInfo(90, 200, "aaaaaaaaaaaaaaaaaaaaaaah")
    level.room_info_list.append(cell_info)
    return level

def setup_level_2():
    level = Level()

    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",wall_scaling)
    wall.left = 15 * wall_size
    wall.bottom = 20 * wall_size
    level.wall_list.append(wall)

    create_and_add_vertical_walls_to_list(3, 13, 24, level.wall_list)
    create_and_add_horiontal_walls_to_list(5, 200, 50, level.wall_list)
    
    guard_convo = Dialogue(100, 300, 50, 50, "omgf")
    level.dialogue_list.append(guard_convo)

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

def create_and_add_character_to_list(filename: str, center_x: float, center_y: float, character_list: arcade.SpriteList) -> list:
    character = arcade.Sprite(filename, sprite_scale)
    character.center_x = center_x
    character.center_y = center_y
    character_list.append(character)

def create_and_add_item_to_list(filename: str, scale: float, center_x: float, center_y: float, item_list: arcade.SpriteList) -> list:
    item = arcade.Sprite(filename, scale)
    item.center_x = center_x
    item.center_y = center_y
    item_list.append(item)

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
        for convo in self.levels[self.current_level].dialogue_list:
            convo.draw()
        for info in self.levels[self.current_level].room_info_list:
            info.draw()

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

    def on_mouse_press(self, x, y, button, key_modifiers):
        check_mouse_press_for_buttons(x, y, self.levels[self.current_level].dialogue_list)
        check_mouse_press_for_buttons(x, y, self.levels[self.current_level].room_info_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        check_mouse_release_for_buttons(x, y, self.levels[self.current_level].dialogue_list)
        check_mouse_release_for_buttons(x, y, self.levels[self.current_level].room_info_list)

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
