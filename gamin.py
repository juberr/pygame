import sys, pygame
from game_objs import Line

pygame.init()

# game logic parameters
main_clock = pygame.time.Clock()
framerate = 60

# screen size
size = width, height = 1920, 1080
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
white = (250, 250, 250)

# global drawing variable, remove later

drawing = False

while 1:

   for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()

   # Handling input

   mouse = pygame.mouse.get_pressed(num_buttons = 3)
   
   if mouse[0] == 1:
      if not drawing:
         line = Line(screen, 25)
         drawing = True

   if mouse[2] == 1:
      drawing = False

   if drawing:
      line.begin()
      line.draw()

   
      
   #screen.blit()
   pygame.display.update()
   screen.fill(black)
   main_clock.tick(framerate)