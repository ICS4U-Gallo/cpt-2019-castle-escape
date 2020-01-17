import arcade
import math
import settings

Width = 600
Height = 600
Character_Movement = 8
Speed = 20
Arrow_state = "ready"


def collision(c1, c2):
    distance = math.sqrt(math.pow(c1.position_x - c2.position_x(), 2) + math.pow(c1.position_y - position_y, 2))
    if distance < 10:
        return True
    else:
        return False

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
            self.position_y = self.position_y - 40
            self.change_x = self.change_x*-1

        if self.position_x == self.radius:
            self.position_y = self.position_y - 40
            self.change_x = self.change_x*-1

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > settings.HEIGHT:
            self.position_y = settings.HEIGHT - self.radius

class Arrow:

    def __init__(self, position_x, position_y, change_y, radius, color):

        self.position_x = position_x
        self.position_y = position_y
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):

        self.position_y += self.change_y

class Chapter3View(arcade.View,):

    def __init__(self):

        super().__init__()


        self.ball = Ball(400, 50, 0, 15, arcade.color.CHAMOISEE)
        self.enemy = Enemy(50,550,8, 2, 15, arcade.color.CADET_GREY)
        self.enemy2 = Enemy(150,550,8,2,15, arcade.color.CADET_GREY)
        self.enemy3 = Enemy(250, 550, 8, 2, 15, arcade.color.CADET_GREY)
        self.enemy4 = Enemy(350, 550, 8, 2, 15, arcade.color.CADET_GREY)
        self.enemy5 = Enemy(450, 550, 8, 2, 15, arcade.color.CADET_GREY)
        self.enemy6 = Enemy(550, 550, 8, 2, 15, arcade.color.CADET_GREY)
        self.enemy7 = Enemy(650, 550, 8, 2, 15, arcade.color.CADET_GREY)
        self.enemy8 = Enemy(750, 550, 8, 2, 15, arcade.color.CADET_GREY)
        self.enemy9 = Enemy(50, 475, 8, 2, 15, arcade.color.CADET_GREY)
        self.enemy10 = Enemy(150, 475, 8, 2, 15, arcade.color.CADET_GREY)
        self.enemy11 = Enemy(250, 475, 8, 2, 15, arcade.color.CADET_GREY)
        self.enemy12 = Enemy(350, 475, 8, 2, 15, arcade.color.CADET_GREY)
        self.enemy13 = Enemy(450, 475, 8, 2, 15, arcade.color.CADET_GREY)
        self.enemy14 = Enemy(550, 475, 8, 2, 15, arcade.color.CADET_GREY)
        self.enemy15 = Enemy(650, 475, 8, 2, 15, arcade.color.CADET_GREY)
        self.enemy16 = Enemy(750, 475, 8, 2, 15, arcade.color.CADET_GREY)
        self.arrow = Arrow(400,50,0,5,arcade.color.BROWN_NOSE)


    def on_show(self):
        arcade.set_background_color(arcade.color.YELLOW_GREEN)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()
        self.enemy.draw()
        self.enemy2.draw()
        self.enemy3.draw()
        self.enemy4.draw()
        self.enemy5.draw()
        self.enemy6.draw()
        self.enemy7.draw()
        self.enemy8.draw()
        self.enemy9.draw()
        self.enemy10.draw()
        self.enemy11.draw()
        self.enemy12.draw()
        self.enemy13.draw()
        self.enemy14.draw()
        self.enemy15.draw()
        self.enemy16.draw()
        self.arrow.draw()

    def on_update(self, delta_time):
        global Arrow_state

        if self.arrow.position_y > settings.HEIGHT:
            self.arrow.position_y = self.ball.position_y
            self.arrow.position_x = self.ball.position_x
            self.arrow.change_y = 0
            Arrow_state = "ready"

        self.ball.update()
        self.enemy.update()
        self.enemy2.update()
        self.enemy3.update()
        self.enemy4.update()
        self.enemy5.update()
        self.enemy6.update()
        self.enemy7.update()
        self.enemy8.update()
        self.enemy9.update()
        self.enemy10.update()
        self.enemy11.update()
        self.enemy12.update()
        self.enemy13.update()
        self.enemy14.update()
        self.enemy15.update()
        self.enemy16.update()
        self.arrow.update()

    def on_key_press(self, key, modifiers):
        global Arrow_state
        if key == arcade.key.ENTER:
            self.director.next_view()
        if key == arcade.key.LEFT:
            self.ball.change_x = -Character_Movement
        elif key == arcade.key.RIGHT:
            self.ball.change_x = Character_Movement
        if key == arcade.key.SPACE:
            if Arrow_state == "ready":
                Arrow_state = "release"
                self.arrow.position_y = self.ball.position_y
                self.arrow.position_x = self.ball.position_x
                self.arrow.change_y = Speed


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