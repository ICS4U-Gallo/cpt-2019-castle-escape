import arcade

import settings


class Chapter1View(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.GOLDEN_BROWN)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Part 1", settings.WIDTH/2, settings.HEIGHT - 30,
                         arcade.color.BLACK, font_size=30, anchor_x="center", anchor_y="top")
        arcade.draw_text("       You wake up in a dungeon cell- nothing new.\n\nWhile eating, you discover a note and a key.\n\nIt says to get to get to the gardens without being caught,\n\n and that there'll be someone waiting.",
                         settings.WIDTH//2, settings.HEIGHT//2, arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Press Enter to continue...", settings.WIDTH//2, 200,
                         arcade.color.ANTIQUE_RUBY, font_size=20, anchor_x="center")
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
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
    my_view = Chapter1View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
