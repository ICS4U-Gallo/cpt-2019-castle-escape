import arcade

import settings

Width = 600
Height = 600
Character_Movement = 4

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

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > settings.WIDTH - self.radius:
            self.position_x = settings.WIDTH - self.radius

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

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > settings.WIDTH - self.radius:
            self.position_y = self.position_y - 50
            self.change_x = self.change_x*-1

        if self.position_x == self.radius:
            self.position_y = self.position_y - 50
            self.change_x = self.change_x*-1

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > settings.HEIGHT:
            self.position_y = settings.HEIGHT - self.radius

class Chapter3View(arcade.View,):

    def __init__(self):

        super().__init__()


        self.ball = Ball(400, 50, 0, 15, arcade.color.WHITE)
        self.enemy = Enemy(80,550,4, 2, 15, arcade.color.RED)
        self.enemy2 = Enemy(240,550,4,2,15, arcade.color.RED)
        self.enemy3 = Enemy(400, 550, 4, 2, 15, arcade.color.RED)
        self.enemy4 = Enemy(560, 550, 4, 2, 15, arcade.color.RED)
        self.enemy5 = Enemy(720, 550, 4, 2, 15, arcade.color.RED)


    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()
        self.enemy.draw()
        self.enemy2.draw()
        self.enemy3.draw()
        self.enemy4.draw()
        self.enemy5.draw()

    def on_update(self, delta_time):
        self.ball.update()
        self.enemy.update()
        self.enemy2.update()
        self.enemy3.update()
        self.enemy4.update()
        self.enemy5.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.director.next_view()
        if key == arcade.key.LEFT:
            self.ball.change_x = -Character_Movement
        elif key == arcade.key.RIGHT:
            self.ball.change_x = Character_Movement

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0

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