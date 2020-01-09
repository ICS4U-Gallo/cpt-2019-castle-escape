import arcade

import settings

Width = 600
Height = 600
Character_Movement = 4
Enemy_Movement = 3

class Ball:
    def __init__(self, position_x, position_y, change_x, radius, color):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > Width - self.radius:
            self.position_x = Width - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius
class Enemy:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > Width - self.radius:
            self.position_y = self.position_y - 50
            self.change_x = -2

        if self.position_x == self.radius:
            self.position_y = self.position_y - 50
            self.change_x = 2

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > Height:
            self.position_y = Height - self.radius

class MyGame(arcade.Window):

    def __init__(self, width, height):

        # Call the parent class's init function
        super().__init__(width, height)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # Create our ball
        self.ball = Ball(300, 50, 0, 15, arcade.color.WHITE)
        self.enemy = Enemy(50,550,2, 2, 15, arcade.color.RED)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        self.enemy.draw()

    def on_update(self, delta_time):
        self.ball.update()
        self.enemy.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -Character_Movement
        elif key == arcade.key.RIGHT:
            self.ball.change_x = Character_Movement

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0

def main():
    MyGame(Width, Height)
    arcade.run()

if __name__ == "__main__":
    main()


class Chapter3View(arcade.View,):
    def on_show(self):
        arcade.set_background_color(arcade.color.CHAMOISEE)

    def on_draw(self):
        arcade.start_render()

    def on_key_press(self, key, modifiers):
        self.director.next_view()


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
    my_view = Chapter3View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()