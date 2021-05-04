import sys, pygame
from game_objs import *

pygame.init()

# game logic parameters
main_clock = pygame.time.Clock()
framerate = 500
# screen size
size = width, height = 2560, 1400
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
white = (250, 250, 250)

# global drawing variable, remove later. Constants courtesy of https://github.com/000Nobody/Orbit-Simulator/blob/master/main.py
GRAV = 6.67408 * (10 ** -11)
MASS_RATIO = 1000

# create game class later to abstract these
drawing = False
player_objs = []
game_objs = []
id = 0

while 1:

   for event in pygame.event.get():

      if event.type == pygame.QUIT: sys.exit()
   

      # handle mouse input
      if event.type == pygame.MOUSEBUTTONDOWN:

         # enter ball mode
         if pygame.mouse.get_pressed()[0] == 1 and not drawing:
            blip = Cursor(screen, 50)
            player_objs.append(blip)
            drawing = True
            continue

         # spawn ball on mouse click
         if pygame.mouse.get_pressed()[0] == 1 and drawing:
            planet = Planet(screen, id, GRAV)
            id += 1
            game_objs.append(planet)
            
         # exit ball mode   
         if pygame.mouse.get_pressed()[2] == 1 and drawing:
            player_objs.pop()
            drawing = False
            


      
   for obj in game_objs:
      obj.update(planets=game_objs)
   
   for obj in player_objs:
      obj.update()   

   pygame.display.update()
   screen.fill(black)
   main_clock.tick(framerate)