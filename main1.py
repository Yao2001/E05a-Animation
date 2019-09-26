#Copy the contents from http://arcade.academy/examples/move_mouse.html#move-mouse and see if you can figure out what is going on. Add comments to any uncommented lines

"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""
# import arcade to create a 2D game
import arcade

# Set up the width adn height for the window
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
# Will appear on the top of the window
SCREEN_TITLE = "Move Mouse Example"

# the class of the ball
class Ball:
    # initialized the ball's position and color
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        # the location on the x axis
        self.position_x = position_x
        # the location on the y axis
        self.position_y = position_y
        # the radius of the ball
        self.radius = radius
        # the color of the ball
        self.color = color

    # denfined a draw function
    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

# the class of the game window
class MyGame(arcade.Window):

    # initialized the size and title of the window
    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # Set up the background
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x
        self.ball.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        print(f"You clicked button number: {button}")
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.BLACK

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.AUBURN

# define a main function, the main game
def main():
    # Create a window the player can move the ball in it
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    # use the aracde to fun the file
    arcade.run()

# if the main is opening
if __name__ == "__main__":
    # main
    main()