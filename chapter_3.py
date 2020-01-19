import arcade
import os
import settings

prison_guard = arcade.Sprite("pics\prison_guard.png", 0.5)
prison_guard.center_x = 150
prison_guard.center_y = 525
prison_guard.change_x = 3
prison_guard.scale = 0.3
prison_guard.points = [[-20, -20], [20, -20], [20, 20], [-20, 20]]

prison_guard2 = arcade.Sprite("pics\prison_guard.png", 0.5)
prison_guard2.center_x = 350
prison_guard2.center_y = 525
prison_guard2.change_x = 3
prison_guard2.scale = 0.3
prison_guard2.points = [[-20, -20], [20, -20], [20, 20], [-20, 20]]

prison_guard3 = arcade.Sprite("pics\prison_guard.png", 0.5)
prison_guard3.center_x = 550
prison_guard3.center_y = 525
prison_guard3.change_x = 3
prison_guard3.scale = 0.3
prison_guard3.points = [[-20, -20], [20, -20], [20, 20], [-20, 20]]

prison_guard4 = arcade.Sprite("pics\prison_guard.png", 0.5)
prison_guard4.center_x = 750
prison_guard4.center_y = 525
prison_guard4.change_x = 3
prison_guard4.scale = 0.3
prison_guard4.points = [[-20, -20], [20, -20], [20, 20], [-20, 20]]

prison_guard5 = arcade.Sprite("pics\prison_guard.png", 0.5)
prison_guard5.center_x = 100
prison_guard5.center_y = 475
prison_guard5.change_x = 3
prison_guard5.scale = 0.3
prison_guard5.points = [[-20, -20], [20, -20], [20, 20], [-20, 20]]

prison_guard6 = arcade.Sprite("pics\prison_guard.png", 0.5)
prison_guard6.center_x = 300
prison_guard6.center_y = 475
prison_guard6.change_x = 3
prison_guard6.scale = 0.3
prison_guard6.points = [[-20, -20], [20, -20], [20, 20], [-20, 20]]

prison_guard7 = arcade.Sprite("pics\prison_guard.png", 0.5)
prison_guard7.center_x = 500
prison_guard7.center_y = 475
prison_guard7.change_x = 3
prison_guard7.scale = 0.3
prison_guard7.points = [[-20, -20], [20, -20], [20, 20], [-20, 20]]

prison_guard8 = arcade.Sprite("pics\prison_guard.png", 0.5)
prison_guard8.center_x = 700
prison_guard8.center_y = 475
prison_guard8.change_x = 3
prison_guard8.scale = 0.3
prison_guard8.points = [[-20, -20], [20, -20], [20, 20], [-20, 20]]

arrow = arcade.Sprite("pics\darrow.png",)
arrow.center_x = 400
arrow.center_y = -50
arrow.change_y = 0
arrow.angle = 225
arrow.scale = .1
arrow.points = [[-20, -20], [20, -20], [20, 20], [-20, 20]]
arrowstate = "ready"

class Chapter3View(arcade.View):
    def __init__(self):
        super().__init__()

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           0.7)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_sprite.change_x = 0
        self.player_sprite.points = [[-20, -20], [20, -20], [20, 20], [-20, 20]]
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        self.player_list.append(prison_guard)
        self.player_list.append(prison_guard2)
        self.player_list.append(prison_guard3)
        self.player_list.append(prison_guard4)
        self.player_list.append(prison_guard5)
        self.player_list.append(prison_guard6)
        self.player_list.append(prison_guard7)
        self.player_list.append(prison_guard8)

        self.player_list.append(arrow)


    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()

    def on_update(self, delta_time):
        global arrowstate

        self.player_sprite.center_x += self.player_sprite.change_x

        if self.player_sprite.center_x < 25:
            self.player_sprite.center_x = 25

        if self.player_sprite.center_x > settings.WIDTH - 25:
            self.player_sprite.center_x = settings.WIDTH - 25

        if self.player_sprite.center_y < 90:
            self.player_sprite.center_y = 90

        prison_guard.center_x += prison_guard.change_x

        if prison_guard.center_x > 750:
            prison_guard.center_y = prison_guard.center_y - 40
            prison_guard.change_x = prison_guard.change_x * -1

        if prison_guard.center_x < 50:
            prison_guard.center_y = prison_guard.center_y - 40
            prison_guard.change_x = prison_guard.change_x * -1

        prison_guard2.center_x += prison_guard2.change_x

        if prison_guard2.center_x > 750:
            prison_guard2.center_y = prison_guard2.center_y - 40
            prison_guard2.change_x = prison_guard2.change_x * -1

        if prison_guard2.center_x < 50:
            prison_guard2.center_y = prison_guard2.center_y - 40
            prison_guard2.change_x = prison_guard2.change_x * -1

        prison_guard3.center_x += prison_guard3.change_x

        if prison_guard3.center_x > 750:
            prison_guard3.center_y = prison_guard3.center_y - 40
            prison_guard3.change_x = prison_guard3.change_x * -1

        if prison_guard3.center_x < 50:
            prison_guard3.center_y = prison_guard3.center_y - 40
            prison_guard3.change_x = prison_guard3.change_x * -1

        prison_guard4.center_x += prison_guard4.change_x

        if prison_guard4.center_x > 750:
            prison_guard4.center_y = prison_guard4.center_y - 40
            prison_guard4.change_x = prison_guard4.change_x * -1

        if prison_guard4.center_x < 50:
            prison_guard4.center_y = prison_guard4.center_y - 40
            prison_guard4.change_x = prison_guard4.change_x * -1

        prison_guard5.center_x += prison_guard5.change_x

        if prison_guard5.center_x > 750:
            prison_guard5.center_y = prison_guard5.center_y - 40
            prison_guard5.change_x = prison_guard5.change_x * -1

        if prison_guard5.center_x < 50:
            prison_guard5.center_y = prison_guard5.center_y - 40
            prison_guard5.change_x = prison_guard5.change_x * -1

        prison_guard6.center_x += prison_guard6.change_x

        if prison_guard6.center_x > 750:
            prison_guard6.center_y = prison_guard6.center_y - 40
            prison_guard6.change_x = prison_guard6.change_x * -1

        if prison_guard6.center_x < 50:
            prison_guard6.center_y = prison_guard6.center_y - 40
            prison_guard6.change_x = prison_guard6.change_x * -1

        prison_guard7.center_x += prison_guard7.change_x

        if prison_guard7.center_x > 750:
            prison_guard7.center_y = prison_guard7.center_y - 40
            prison_guard7.change_x = prison_guard7.change_x * -1

        if prison_guard7.center_x < 50:
            prison_guard7.center_y = prison_guard7.center_y - 40
            prison_guard7.change_x = prison_guard7.change_x * -1

        prison_guard8.center_x += prison_guard8.change_x

        if prison_guard8.center_x > 750:
            prison_guard8.center_y = prison_guard8.center_y - 40
            prison_guard8.change_x = prison_guard8.change_x * -1

        if prison_guard8.center_x < 50:
            prison_guard8.center_y = prison_guard8.center_y - 40
            prison_guard8.change_x = prison_guard8.change_x * -1

        arrow.center_y += arrow.change_y

        if arrow.center_y > settings.HEIGHT:
            arrow.center_y = self.player_sprite.center_y - 150
            arrow.center_x = self.player_sprite.center_x
            arrow.change_y = 0
            arrowstate = "ready"




    def on_key_press(self, key, modifiers):
        global arrowstate
        if key == arcade.key.ENTER:
            self.director.next_view()
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -4
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 4
        if key == arcade.key.SPACE:
            if arrowstate == "ready":
                arrow.center_y = self.player_sprite.center_y
                arrow.center_x = self.player_sprite.center_x
                arrow.change_y = 5
                arrowstate = "fired"



    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


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
