import arcade
import settings
import os

movement_speed = 5


class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > settings.WIDTH - 1:
            self.right = settings.WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > settings.HEIGHT - 1:
            self.top = settings.HEIGHT - 1


class Chapter2View(arcade.View):

    def __init__(self):
        super().__init__()

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.player_list = None
        self.main_player = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        arcade.set_background_color(arcade.color.GRAY_BLUE)

    def setup(self):
        self.player_list = arcade.SpriteList()

        self.main_player = Player("pics/maleAdventurer_idle.png")
        self.main_player.center_x = 50
        self.main_player.center_y = 50
        self.player_list.append(self.main_player)
    
    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
                 
    def on_update(self, delta_time):
        self.main_player.change_x = 0
        self.main_player.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.main_player.change_y = movement_speed
        elif self.down_pressed and not self.up_pressed:
            self.main_player.change_y = -movement_speed
        
        if self.left_pressed and not self.right_pressed:
            self.main_player.change_x = -movement_speed
        elif self.right_pressed and not self.left_pressed:
            self.main_player.change_x = movement_speed

        self.player_list.update()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.director.next_view()
        elif key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False


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
    my_view.setup()
    arcade.run()
