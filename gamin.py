import sys, pygame
from game_objs import Line

pygame.init()

main_clock = pygame.time.Clock()
framerate = 60

size = width, height = 1920, 1080
speed = [2, 2]
black = 0, 0, 0

img = pygame.image.load('intro_ball.gif')

screen = pygame.display.set_mode(size)

white = (255,255,255)
black = (0,0,0)
start = [100, 200]

end = [150,200]


while 1:

   line = Line(screen,white,start,end, 50)

   for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()

   # Handling input
   if pygame.key.get_pressed()[pygame.K_d]:
      line.move(5)
      

   if pygame.key.get_pressed()[pygame.K_a]:
      line.move(-5)   


    


    


   
   #screen.blit()
   pygame.display.update()
   screen.fill(black)
   main_clock.tick(framerate)