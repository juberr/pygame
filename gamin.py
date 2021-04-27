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


# initialize line attributes
white = (255,255,255)
black = (0,0,0)
start = [100, 200]
end = [150,200]


while 1:

   line = Line(screen,white,start,end, 50)

   for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()

   # Handling input

   keys = pygame.key.get_pressed()

   if keys[pygame.K_d]:
      line.horiz_move(5)
      print(line.end, line.start)
      

   if keys[pygame.K_a]:
      line.horiz_move(-5)
      print(line.end, line.start)   


    

   #screen.blit()
   pygame.display.update()
   screen.fill(black)
   main_clock.tick(framerate)