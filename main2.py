#Copy the contents from http://arcade.academy/examples/move_keyboard.html#move-keyboard and see if you can figure out what is going on. Add comments to any uncommented lines

"""
This simple animation example shows how to move an item with the keyboard.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_keyboard
"""

# import aracade to create a 2D game
import arcade

# set up the size, title of the window and the moving speed of the ball
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Move Keyboard Example"
MOVEMENT_SPEED = 3

# the class of the ball
class Ball:
    # initialized the position, radius and color of the ball
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        # the location on the x axis
        self.position_x = position_x
        # the location on the y axis
        self.position_y = position_y
        # the position change on the x axis
        self.change_x = change_x
        # the position change on the y axis
        self.change_y = change_y
        # the radius of the ball
        self.radius = radius
        # set up the color of the ball
        self.color = color

    # define a function called draw
    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    # define a function called update
    def update(self):
        # Move the ball
        # the position and the changes on y axis when press the keyboard
        self.position_y += self.change_y
        # the position and the changes on x axis when press the keyboard
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        # if the ball moves less than the x axis 
        if self.position_x < self.radius:
            # the ball cannot moves past the x axis
            self.position_x = self.radius
        # if the ball moves pass the x axis
        if self.position_x > SCREEN_WIDTH - self.radius:
            # when the ball hit the edge or the corner, it cannot go farther
            self.position_x = SCREEN_WIDTH - self.radius
        # if the ball cannot less than the y axis
        if self.position_y < self.radius:
            # the ball cannot pass the y axis
            self.position_y = self.radius
        # if the ball cannot pass the y axis
        if self.position_y > SCREEN_HEIGHT - self.radius:
            # when the ball hit the edge or the corner, it cannot go farther
            self.position_y = SCREEN_HEIGHT - self.radius

# the class of the game
class MyGame(arcade.Window):
    # initializewd the window's size and title
    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)
     
        # Set up the background
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

    # define a function called on draw
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        # draw a ball on the screen
        self.ball.draw()

    # moving the ball on the screen
    def update(self, delta_time):
        # update the ball's position
        self.ball.update()

    # define a function called on_key_press
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        # if left arrow
        if key == arcade.key.LEFT:
            # ball move to the left
            self.ball.change_x = -MOVEMENT_SPEED
        # if right arrow
        elif key == arcade.key.RIGHT:
            # ball move to the right
            self.ball.change_x = MOVEMENT_SPEED
        # if up arrow
        elif key == arcade.key.UP:
            # ball move to the up
            self.ball.change_y = MOVEMENT_SPEED
        # if down arrow
        elif key == arcade.key.DOWN:
            # ball move to the down
            self.ball.change_y = -MOVEMENT_SPEED

    # define the function called on_key_release
    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        # if you don't press the keyboard, the ball won't move on the x axis
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        # if you don't press the keyboard, the ball won't move on the y axis
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0

# define a function called main
def main():
    # the main game window
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    # run the game
    arcade.run()

# if you are in the main file, run the game
if __name__ == "__main__":
    main()