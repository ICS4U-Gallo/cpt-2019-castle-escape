import arcade
import settings
import os


main_player = arcade.load_texture("pics\maleAdventurer_idle.png")


class Player():

    def __init__(self, position_x, position_y, change_x, change_y, width, height, texture, angle):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.texture = texture
        self.angle = angle

    def draw(self):
        arcade.draw_texture_rectangle(self.position_x, self.position_y, self.width, self.height, self.texture, self.angle)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x < self.width:
            self.position_x = self.width
        if self.position_x > settings.WIDTH - self.width:
            self.position_x = settings.width - self.width

        if self.position_y < self.width:
            self.position_y = self.width
        if self.position_y > settings.HEIGHT - self.width:
            self.position_y = settings.HEIGHT - self.width


class Chapter2View(arcade.View):

    def __init__(self):
        super().__init__()

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.GRAY_BLUE)

        self.main_player = Player(400, 100, 0, 0, .5 * main_player.width, .5 * main_player.height, main_player, 0)
    
    def on_draw(self):
        arcade.start_render()
        self.main_player.draw()

    def on_update(self, delta_time):
        self.main_player.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.director.next_view()
        elif key == arcade.key.LEFT:
            self.main_player.change_x = -3
        elif key == arcade.key.RIGHT:
            self.main_player.change_x = 3
        elif key == arcade.key.UP:
            self.main_player.change_y = 3
        elif key == arcade.key.DOWN:
            self.main_player.change_y = -3

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or arcade.key.RIGHT:
            self.main_player.change_x = 0
        if key == arcade.key.UP or arcade.key.DOWN:
            self.main_player.change_y = 0


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
