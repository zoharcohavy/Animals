import random
import arcade
import organisms
import math
import globals
#import pyscreenshot
#import cv2

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height, fullscreen = True)
        arcade.set_background_color(arcade.color.WHITE)
        self.learning_timer = 20

    def setup(self):
        # Set up your game here
        self.bacteria_list = arcade.SpriteList()
        self.orange_list = arcade.SpriteList()

    # Create the organisms
        for i in range(20):

            bacteria = organisms.Bacteria("images/bacteria.png", 1)

            bacteria.ID = i
            bacteria.center_x = random.randrange(globals.SCREEN_WIDTH)
            bacteria.center_y = random.randrange(globals.SCREEN_HEIGHT)
            bacteria.energy = 50
            bacteria.velocity_x = random.random() - 0.55
            bacteria.velocity_y = random.random() - 0.55
            bacteria.acceleration_x = 0.0
            bacteria.acceleration_y = 0.0
            if (bacteria.velocity_x > 0 and bacteria.velocity_y > 0) or \
                    (bacteria.velocity_x < 0 and bacteria.velocity_y < 0):
                bacteria.dir_angle = math.atan(bacteria.velocity_y/bacteria.velocity_x)
            else:
                bacteria.dir_angle = math.atan(-bacteria.velocity_y/bacteria.velocity_x)
            bacteria.dir_timer = random.randrange(200) + 100
            bacteria.experiences = []
            self.bacteria_list.append(bacteria)

    # Create the food
        for i in range(20):

            block_height = random.randrange(3) + 2
            block_width = random.randrange(3) + 2

            food_cluster_start_x = random.randrange(globals.SCREEN_WIDTH - block_width)
            food_cluster_start_y = random.randrange(globals.SCREEN_HEIGHT - block_height)
            for j in range(block_height):
                for k in range (block_width):
                    orange = organisms.Orange("images/orange.png", 0.02)
                    orange.center_x = food_cluster_start_x + 10*k
                    orange.center_y = food_cluster_start_y + 10*j
                    self.orange_list.append(orange)


    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.bacteria_list.draw()
        self.orange_list.draw()
        # Your drawing code goes here

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.bacteria_list.update()
        self.learning_timer -= 1
        if self.learning_timer == 0:
            self.learning_timer = 20
#			im = ImageGrab.grab()
#			im.save('screenshot.png')
#            im = ImageGrab.grab_to_file('practice_images/image_1.png')
#            img = cv2.imread("practice_images/image_1.png")
#            for bacteria in self.bacteria_list:
#                bottom = globals.SCREEN_HEIGHT - globals.floor(bacteria.center_y - 100)
#                top = globals.SCREEN_HEIGHT - globals.roof_y(bacteria.center_y + 100)
#                left = globals.floor(bacteria.center_x - 100)
#                right = globals.floor(bacteria.center_x + 100)
#                bacteria.experiences.append(img[top:bottom,left:right])

        for bacteria in self.bacteria_list:
            bacteria.update()
            bacteria_hit_list = arcade.check_for_collision_with_list(bacteria, self.orange_list)
            for food_item in bacteria_hit_list:
                food_item.kill()

def main():
    game = MyGame(globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
