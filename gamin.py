import sys, pygame
from game_objs import *

pygame.init()

# game logic parameters
main_clock = pygame.time.Clock()
framerate = 144

# screen size
size = width, height = 1920, 1080
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
white = (250, 250, 250)

# global drawing variable, remove later


# create game class later to abstract these
drawing = False
player_objs = []
game_objs = []

while 1:

   for event in pygame.event.get():

      if event.type == pygame.QUIT: sys.exit()
   
      if event.type == pygame.MOUSEBUTTONDOWN:

         if pygame.mouse.get_pressed()[0] == 1 and not drawing:
            blip = Cursor(screen, 50)
            player_objs.append(blip)
            drawing = True

         if pygame.mouse.get_pressed()[0] == 1 and drawing:
            ball = Ball(screen)
            game_objs.append(ball)
            
         if pygame.mouse.get_pressed()[2] == 1 and drawing:
            player_objs.pop()
            drawing = False
            


      
            

   # Handling input

  
   

   for obj in game_objs:
      obj.update()
   
   for obj in player_objs:
      obj.update()   

   pygame.display.update()
   screen.fill(black)
   main_clock.tick(framerate)