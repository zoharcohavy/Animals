import arcade
import math
import random
import globals
#import cv2

class Bacteria(arcade.Sprite):

    def update(self):
        self.fix_bounds()
        #universally, all moving objects slow down
        if abs(self.acceleration_x) < 0.02 and abs(self.acceleration_y) < 0.02:
            self.slow_down()
        else:
            self.velocity_x += self.acceleration_x
            self.velocity_y += self.acceleration_y
            self.decelerate()
        self.dir_timer -= 1
        self.center_x += self.velocity_x
        self.center_y += self.velocity_y
        if self.dir_timer == 0:
            self.redirect()
#		if self.energy < 0:
#			self.kill()
			
#            if self.energy < 0:
#				self.kill()
#                for i in range(len(self.experiences)):
#                    cv2.imwrite("practice_images/" + str(self.ID) + "/experience_" + str(i) + ".png", self.experiences[i])
#                self.kill()

    def redirect(self):  # the number is 2PI / 0.9
        self.dir_angle = (random.random() - 0.1) * 6.98
        self.acceleration_x = math.cos(self.dir_angle)/7.5
        self.acceleration_y = math.sin(self.dir_angle)/7.5
        self.dir_timer = random.randrange(25) + 50
        self.energy -= 1

    def fix_bounds(self):
        if self.center_x < 0:
            self.center_x = 1
            self.velocity_x = -self.velocity_x
        if self.center_x > globals.SCREEN_WIDTH:
            self.center_x = globals.SCREEN_WIDTH - 1
            self.velocity_x = -self.velocity_x
        if self.center_y < 0:
            self.center_y = 1
            self.velocity_y = -self.velocity_y
        if self.center_y > globals.SCREEN_HEIGHT:
            self.center_y = globals.SCREEN_HEIGHT - 1
            self.velocity_y = -self.velocity_y
    def slow_down(self):
        if self.velocity_x > 0:
            self.velocity_x = self.velocity_x - 0.01
        else:
            self.velocity_x = self.velocity_x + 0.01
        if self.velocity_y > 0:
            self.velocity_y = self.velocity_y - 0.01
        else:
            self.velocity_y = self.velocity_y + 0.01

    def decelerate(self):
        if self.acceleration_x > 0:
            self.acceleration_x = self.acceleration_x - 0.01
        else:
            self.acceleration_x = self.acceleration_x + 0.01
        if self.acceleration_y > 0:
            self.acceleration_y = self.acceleration_y - 0.01
        else:
            self.acceleration_y = self.acceleration_y + 0.01

class Orange(arcade.Sprite):
	def update(self):
		self.center_x += 1
