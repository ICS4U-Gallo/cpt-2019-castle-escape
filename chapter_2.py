import arcade
import settings
import os

#information for sprites
wall_scaling = 0.1
wall_size = 10
movement_speed = 3


class Player(arcade.Sprite):
    """Player class

    """
    def __init__(self):
        super().__init__()

        #load textures for player
        self.first_version = arcade.load_texture("pics\maleAdventurer_idle.png")
        self.first_version.scale = 0.3
        self.new_version = arcade.load_texture("pics\warrior.png")
        self.new_version.scale = 0.15

    def update_animation(self, inventory: int, delta_time: float=1/60):
        """Updates texture of player sprite based on inventory value

        Args:
            inventory (int): number of items the player sprite has collided with.
            delta_time (float): allows textures to be updated with time.
        Return:
            Sprite texture depending on inventory value
        """
        #if item in second level is picked up, player "changes outfits"
        if inventory >= 2:
            self.texture = self.new_version
        else:
            self.texture = self.first_version
        return


class Dialogue:
    """Dialogue class
    
    Attrs:
        center_x (float): x coordinate of center of text box.
        center_y (float): y coordinate of center of text box.
        width (float): Width of text box.
        height (float): Height of text box.
        text (str): Dialogue in text box.
        font_size (int): Size of text.

    """
    def __init__(self, center_x: float, center_y: float, width: float, height: float, text: str, font_size: int=13,
                 font: str="Arial", color: str=arcade.color.LIGHT_GRAY):
        self._center_x = center_x
        self._center_y = center_y
        self._width = width
        self._height = height
        self._text = text
        self._font_size = font_size
        self._font = font
        self._color = color
        self.pressed = False

    def get_center_x(self):
        return(self._center_x)

    def set_center_x(self, value: float):
        self._center_x = value

    def get_center_y(self):
        return(self._center_y)

    def set_center_y(self, value: float):
        self._center_y = value

    def get_width(self):
        return(self._width)

    def set_width(self, value: float):
        self._width = value

    def get_height(self):
        return(self._height)

    def set_height(self, value: float):
        self._height = value

    def get_text(self):
        return(self._text)

    def set_text(self, value: str):
        self._text = value

    def get_font_size(self):
        return(self._font_size)

    def set_font_size(self, value: int):
        self._font_size = value

    def get_font(self):
        return(self._font)

    def set_font(self, value: str):
        self._font = value

    def get_color(self):
        return(self._color)

    def set_color(self, value: arcade.color):
        self._color = value

    def draw(self):
        """Draws exclamation point or dialogue box for character based on if button is pressed

        Returns:
            Box with exclamation or dialogue box
        """
        if not self.pressed:
            #draw dialogue prompt
            arcade.draw_rectangle_filled(self.center_x, self.center_y, 20, 20, arcade.color.ALABAMA_CRIMSON)
            arcade.draw_text("!", self.center_x, self.center_y, arcade.color.BLACK, anchor_x="center", anchor_y="center")
        else:
            #draw dialogue box
            arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
            arcade.draw_text(self.text, self.center_x, self.center_y, arcade.color.BLACK, anchor_x="center", anchor_y="center")
   
    def on_press(self):
        """Makes button pressed true
        Returns:
            Button is pressed
        """
        self.pressed = True

    def on_release(self):
        """Makes button pressed false
        Returns:
            Button is not pressed
        """
        self.pressed = False


class RoomInfo:
    """Room information class

    Attrs:
        center_x (float): x coordinate of center of info prompt box.
        center_y (float): y coordinate of center of info prompt box.
        text (str): All room information
        width (float): Width of info prompt box.
        height (float): Height of info prompt box.

    """
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
        """Draws question mark for character or dialogue box based on if button is pressed

        """
        if not self.pressed:
            #draw info prompt in room
            arcade.draw_rectangle_filled(self.center_x, self.center_y, 20, 20, arcade.color.ANTIQUE_BRASS)
            arcade.draw_text("?", self.center_x, self.center_y, arcade.color.BLACK, anchor_x="center", anchor_y="center")
        else:
            #draw info to top of screen when clicked
            arcade.draw_text(self.text, 10, settings.HEIGHT - 10, arcade.color.BLACK, anchor_x="left", anchor_y="top")

    def on_press(self):
        """Makes button pressed false
        Returns:
            Button is not pressed
        """
        self.pressed = True
    def on_release(self):
        """Makes button pressed false
        Returns:
            Button is not pressed
        """
        self.pressed = False


def check_mouse_press_for_buttons(x: float, y: float, button_list: list):
    """Checks if mouse clicks within area of button and calls button on_press method if so

    Args:
        x (float): x coordinate of mouse.
        y (float): y coordinate of mouse.
        button_list (list): list of buttons.
    """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        #sets button pressed to true
        button.on_press()


def check_mouse_release_for_buttons(x: float, y: float, button_list: list):
    """Calls all button on_release methods when mouse is released

    Args:
        x (float): x coordinate of mouse.
        y (float): y coordinate of mouse.
        button_list (list): list of buttons.
    """
    for button in button_list:
        if button.pressed:
            #sets button pressed to false
            button.on_release()


class Level:
    """Holds information for all levels

    """
    def __init__(self):
        #empty lists to be filled when objects are defined
        self.wall_list = arcade.SpriteList()
        self.character_list = arcade.SpriteList()
        self.item_list = arcade.SpriteList()
        self.dialogue_list = []
        self.room_info_list = []
        self.writing_on_screen = []


def setup_level_1() -> object:
    """Calls walls, items, characters, and room information to setup level 1

    Returns:
        Level object of Level class, containing lists of all elements of level
    """
    #create level object
    level = Level()

    #create vertical walls for level
    create_and_add_vertical_walls_to_list(4, 39, 4, level.wall_list)
    create_and_add_vertical_walls_to_list(4, 25, 19, level.wall_list)
    create_and_add_vertical_walls_to_list(33, 54, 19, level.wall_list)
    create_and_add_vertical_walls_to_list(4, 25, 34, level.wall_list)
    create_and_add_vertical_walls_to_list(33, 54, 34, level.wall_list)
    create_and_add_vertical_walls_to_list(14, 25, 54, level.wall_list)
    create_and_add_vertical_walls_to_list(33, 44, 54, level.wall_list)
    create_and_add_vertical_walls_to_list(14, 45, 74, level.wall_list)
    create_and_add_vertical_walls_to_list(54, settings.HEIGHT, 23, level.wall_list)
    create_and_add_vertical_walls_to_list(54, settings.HEIGHT, 30, level.wall_list)

    #create horizontal walls for level
    create_and_add_horiontal_walls_to_list(4, 34, 4, level.wall_list)
    create_and_add_horiontal_walls_to_list(4, 9, 19, level.wall_list)
    create_and_add_horiontal_walls_to_list(15, 24, 19, level.wall_list)
    create_and_add_horiontal_walls_to_list(30, 54, 19, level.wall_list)
    create_and_add_horiontal_walls_to_list(54, 74, 14, level.wall_list)
    create_and_add_horiontal_walls_to_list(4, 24, 39, level.wall_list)
    create_and_add_horiontal_walls_to_list(30, 54, 39, level.wall_list)
    create_and_add_horiontal_walls_to_list(54, 74, 44, level.wall_list)
    create_and_add_horiontal_walls_to_list(19, 24, 54, level.wall_list)
    create_and_add_horiontal_walls_to_list(30, 35, 54, level.wall_list)

    #create knight character for level
    create_and_add_character_to_list("pics\prison_guard.png", 0.2, 270, 470, level.character_list)

    #knight asks for bribe
    guard_convo = Dialogue(300, 500, 150, 50, "I know who you are...\n if you pay me,\n I'll turn a blind eye.")
    level.dialogue_list.append(guard_convo)

    #create coin item to bribe knight character
    create_and_add_item_to_list("pics\gold_1.png", 0.5, 400, 250, level.item_list)

    #create prompts and info for rooms for object
    cell = RoomInfo(120, 100, "Dungeon cell. There's a note and key. Someone's waiting for you in the garden.")
    level.room_info_list.append(cell)
    guard_room = RoomInfo(450, 280, "Guardroom. There's the unconconsious bodies of the guards. Your saviours must've gone to great lengths...")
    level.room_info_list.append(guard_room)
    torture_chamber = RoomInfo(120, 280, "Torture chamber. You've been here before. They were questioning you, but you didn't answer.")
    level.room_info_list.append(torture_chamber)
    battle_room = RoomInfo(650, 280, "Battle room. You see that your captors are fighting revolutionaries- those who seek to bring back a lost king.")
    level.room_info_list.append(battle_room)
    stairwell = RoomInfo(220, 520, "Stairwell. There's a lone guard who doesn't look surprised to see you")
    level.room_info_list.append(stairwell)

    return level


def setup_level_2() -> object:
    """Calls walls, items, characters, and room information to setup level 2

    Returns:
        Level object of Level class, containing lists of all elements of level
    """
    #create level object
    level = Level()

    #create vertical walls for level
    create_and_add_vertical_walls_to_list(4, 19, 4, level.wall_list)
    create_and_add_vertical_walls_to_list(12, 54, 19, level.wall_list)
    create_and_add_vertical_walls_to_list(0, 5, 23, level.wall_list)
    create_and_add_vertical_walls_to_list(0, 4, 30, level.wall_list)
    create_and_add_vertical_walls_to_list(55, settings.HEIGHT, 23, level.wall_list)
    create_and_add_vertical_walls_to_list(55, settings.HEIGHT, 30, level.wall_list)
    create_and_add_vertical_walls_to_list(4, 15, 34, level.wall_list)
    create_and_add_vertical_walls_to_list(24, 54, 34, level.wall_list)
    create_and_add_vertical_walls_to_list(29, 45, 47, level.wall_list)
    create_and_add_vertical_walls_to_list(24, 29, 54, level.wall_list)
    create_and_add_vertical_walls_to_list(44, 54, 54, level.wall_list)
    create_and_add_vertical_walls_to_list(14, 55, 73, level.wall_list)

    #create horizontal walls for level
    create_and_add_horiontal_walls_to_list(4, 24, 4, level.wall_list)
    create_and_add_horiontal_walls_to_list(30, 34, 4, level.wall_list)
    create_and_add_horiontal_walls_to_list(20, 24, 14, level.wall_list)
    create_and_add_horiontal_walls_to_list(30, 74, 14, level.wall_list)
    create_and_add_horiontal_walls_to_list(4, 19, 19, level.wall_list)
    create_and_add_horiontal_walls_to_list(34, 54, 24, level.wall_list)
    create_and_add_horiontal_walls_to_list(48, 60, 29, level.wall_list)
    create_and_add_horiontal_walls_to_list(68, 74, 29, level.wall_list)
    create_and_add_horiontal_walls_to_list(48, 60, 44, level.wall_list)
    create_and_add_horiontal_walls_to_list(68, 74, 44, level.wall_list)
    create_and_add_horiontal_walls_to_list(54, 73, 54, level.wall_list)
    create_and_add_horiontal_walls_to_list(19, 24, 54, level.wall_list)
    create_and_add_horiontal_walls_to_list(30, 35, 54, level.wall_list)   

    #create sword item for "outfit change" 
    create_and_add_item_to_list("pics\sword_item.png", 0.05, 75, 100, level.item_list)

    #create mysterious figure for level
    create_and_add_character_to_list("pics\mystery_figure.png", 0.095, 270, 350, level.character_list)

    #create dialogue for mysterious figure character
    find_disguise_convo = Dialogue(300, 390, 300, 50, "Someone will notice you!\n I've hidden something in the servant's quarters,\n to make you fit in with the nobility.")
    level.dialogue_list.append(find_disguise_convo)

    #info prompts and text for level
    balcony = RoomInfo(640, 500, "Balcony. Along with the forest and sea, you can see that a battle is coming.")
    level.room_info_list.append(balcony)
    kitchen = RoomInfo(270, 90, "Kitchen. There are plentry of servants around. Your torn clothes are eye-catching, and may sabotage your escape")
    level.room_info_list.append(kitchen)
    great_hall = RoomInfo(270, 470, "Great hall. You could have sworn that someone recognized you, but nobody acts to capture you.")
    level.room_info_list.append(great_hall)
    sitting_room = RoomInfo(650, 230, "Private sitting room. You find several sketches... sketches that look like a richer, healthier version of you.")
    level.room_info_list.append(sitting_room)

    return level


def setup_level_3() -> object:
    """Calls walls, items, characters, and room information to setup level 3

    Returns:
        Level object of Level class, containing lists of all elements of level
    """
    #create level object
    level = Level()

    #create vertical walls for level
    create_and_add_vertical_walls_to_list(4, settings.HEIGHT, 4, level.wall_list)
    create_and_add_vertical_walls_to_list(0, 4, 23, level.wall_list)
    create_and_add_vertical_walls_to_list(0, 4, 30, level.wall_list)
    create_and_add_vertical_walls_to_list(4, 24, 49, level.wall_list)
    create_and_add_vertical_walls_to_list(24, settings.HEIGHT, 74, level.wall_list)

    #create horizontal walls for level
    create_and_add_horiontal_walls_to_list(4, 24, 4, level.wall_list) 
    create_and_add_horiontal_walls_to_list(30, 49, 4, level.wall_list)  
    create_and_add_horiontal_walls_to_list(4, 19, 24, level.wall_list)
    create_and_add_horiontal_walls_to_list(34, 74, 24, level.wall_list)
    
    #create rebels for level
    create_and_add_character_to_list("pics\mystery_figure.png", 0.12, 300, 490, level.character_list)
    create_and_add_character_to_list("pics\prison_guard.png", 0.21, 230, 440, level.character_list)
    create_and_add_character_to_list("pics\prison_guard.png", 0.21, 370, 440, level.character_list)

    #rebels greet player
    rebel_1_greet = Dialogue(200, 490, 100, 20, "It's the lost king!")
    level.dialogue_list.append(rebel_1_greet)
    rebel_2_greet = Dialogue(400, 490, 130, 40, "We've spent so long\ntrying to free you.")
    level.dialogue_list.append(rebel_2_greet)
    rebel_3_greet = Dialogue(300, 540, 150, 40, "You're our only hope,\nkeep going.")
    level.dialogue_list.append(rebel_3_greet)

    return level


def setup_level_4() -> object:
    """Creates empty level with for end of chapter screen

    Returns:
        Empty level object for Level class
    """
    #create level object
    level = Level()
    return level


def create_and_add_vertical_walls_to_list(column_base: int, column_top: int, x: int, wall_list: arcade.SpriteList) -> None:
    """Creates vertical wall and adds to wall list

    Args:
        column_base: Base of the wall.
        column_top: Top of the wall.
        x: Horizontal column placement.
        wall_list: list of wall sprites for level.
    """
    #loop creation of wall sprites 
    for y in range(column_base * wall_size, column_top * wall_size, wall_size):
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", wall_scaling)
        wall.left = x * wall_size
        wall.bottom = y
        wall_list.append(wall)


def create_and_add_horiontal_walls_to_list(row_start: int, row_end: int, y: int, wall_list: arcade.SpriteList) -> None:
    """Creates horizontal wall and adds to wall list

    Args:
        row_start: x value of wall starting point.
        row_end: x value of wall ending point.
        y: y value of row.
        wall_list: list of wall sprites for level.
    """
    #loop creation of wall sprites
    for x in range(row_start * wall_size, row_end * wall_size, wall_size):
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", wall_scaling)
        wall.left = x
        wall.bottom = y * wall_size
        wall_list.append(wall)


def create_and_add_character_to_list(filename: str, scale: float, center_x: float, center_y: float, character_list: arcade.SpriteList) -> None:
    """Creates character and adds to character list

    Args:
        filename: Name of image.
        scale: Scaling of sprite.
        center_x: x coordinate of center of sprite.
        center_y: y coordinate of center of sprite.
        character_list: list of character sprites for level.
    """
    character = arcade.Sprite(filename, scale)
    character.center_x = center_x
    character.center_y = center_y
    character_list.append(character)


def create_and_add_item_to_list(filename: str, scale: float, center_x: float, center_y: float, item_list: arcade.SpriteList) -> None:
    """Creates item and adds to item list

    Args:
        filename: Name of image.
        scale: Scaling of sprite.
        center_x: x coordinate of center of sprite.
        center_y: y coordinate of center of sprite.
        item_list: list of item sprites for level.
    """
    item = arcade.Sprite(filename, scale)
    item.center_x = center_x
    item.center_y = center_y
    item_list.append(item)


class Chapter2View(arcade.View):
    """Main application class

    """
    def __init__(self):
        super().__init__()

        #faster image loading
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        #setting increasing values to zero 
        self.current_level = 0
        self.inventory = 0

        #make main player and append to list
        self.player_sprite = Player()
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        #create each level
        self.levels = [
            setup_level_1(),
            setup_level_2(),
            setup_level_3(),
            setup_level_4()
        ]

        #physics engine for every level between player and walls
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.levels[self.current_level].wall_list)

        #set background
        arcade.set_background_color(arcade.color.AMAZON)
        
    def on_draw(self):
        """Draws everything

        """
        arcade.start_render()

        #draw lists for room components
        self.levels[self.current_level].wall_list.draw()
        self.levels[self.current_level].character_list.draw()
        self.levels[self.current_level].item_list.draw()
        for convo in self.levels[self.current_level].dialogue_list:
            convo.draw()

        #draw player
        self.player_list.draw()

        #write outro text for end of chapter
        if self.current_level == 3:
                arcade.draw_text("     You ride along with the rebels to the battlefield,\n\n and they tell you how many people have died for your cause.\n\nBut the truth is, you are no king - just a prisoner with a lucky face.\n\n You may not have been who they were looking for,\n\nbut the truth doesn't matter - only what is believed.",
                                 settings.WIDTH//2, settings.HEIGHT//2, arcade.color.WHITE, 20, anchor_x="center", anchor_y="center")
                arcade.draw_text("Press Enter to continue...", settings.WIDTH/2, 100,
                         arcade.color.ANTIQUE_RUBY, font_size=20, anchor_x="center")

        #draw empty bar for room info except at chapter end
        if self.current_level != 3:
            arcade.draw_rectangle_filled(settings.WIDTH//2, settings.HEIGHT - 15, settings.WIDTH, 30, arcade.color.ANTIQUE_BRASS)

        #draw list for room info last so it can go in front of empty rectangle and player
        for info in self.levels[self.current_level].room_info_list:
            info.draw()

    def on_key_press(self, key: arcade.key, modifiers: int):
        """Called when a key is pressed

        """
        #player movement with keys
        if key == arcade.key.UP:
            self.player_sprite.change_y = movement_speed
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -movement_speed
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -movement_speed
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = movement_speed

        #go to next view from level 4
        elif key == arcade.key.ENTER and self.current_level == 3:
            self.director.next_view()

    def on_key_release(self, key: arcade.key, modifiers):
        """Called when a key is released

        """
        #stops sprite movement when key is released
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time: float) -> None:
        """Movement and game logic

        """
        #inventory of items "picked up"
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.levels[self.current_level].item_list)
        for item in hit_list:
            item.remove_from_sprite_lists()
            self.inventory += 1

        #update player sprite "outfit" is sword item is picked up
        self.player_list.update()
        self.player_list.update_animation(self.inventory)

        #update physics engine for player sprite and walls
        self.physics_engine.update()

        #go to next level
        #level 2 blocked if coin item is not picked up
        if self.player_sprite.center_y > settings.HEIGHT and self.current_level == 0 and self.inventory >= 1:  
            self.current_level = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.levels[self.current_level].wall_list)
            self.player_sprite.center_y = 0
        elif self.player_sprite.center_y > settings.HEIGHT and self.current_level == 0 and self.inventory == 0:  
            self.player_sprite.center_y = settings.HEIGHT

        #level 3 blocked if sword item is not picked up
        elif self.player_sprite.center_y > settings.HEIGHT and self.current_level == 1 and self.inventory >= 2:
            self.current_level = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.levels[self.current_level].wall_list)
            self.player_sprite.center_y = 0
        elif self.player_sprite.center_y > settings.HEIGHT and self.current_level == 1 and self.inventory == 1:
            self.player_sprite.center_y = settings.HEIGHT

        #go up to empty level after winning game
        elif self.player_sprite.center_y > settings.HEIGHT and self.current_level == 2:
            self.current_level = 3

        #go down levels
        elif self.player_sprite.center_y < 0 and self.current_level == 1:
            self.current_level = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.levels[self.current_level].wall_list)
            self.player_sprite.center_y = settings.HEIGHT
        elif self.player_sprite.center_y < 0 and self.current_level == 2:
            self.current_level = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.levels[self.current_level].wall_list)
            self.player_sprite.center_y = settings.HEIGHT

    def on_mouse_press(self, x: float, y: float, button, modifiers):
        """Called when mouse is clicked

        """
        #dialogue buttons
        check_mouse_press_for_buttons(x, y, self.levels[self.current_level].dialogue_list)

        #room info prompt buttons
        check_mouse_press_for_buttons(x, y, self.levels[self.current_level].room_info_list)

    def on_mouse_release(self, x: float, y: float, button, modifiers):
        """Called when mouse is released

        """
        #dialogue buttons
        check_mouse_release_for_buttons(x, y, self.levels[self.current_level].dialogue_list)

        #room info prompt buttons
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
