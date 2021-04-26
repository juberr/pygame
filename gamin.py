import sys, pygame
from game_objs import Player

pygame.init()

main_clock = pygame.time.Clock()
framerate = 60

size = width, height = 1920, 1080
speed = [2, 2]
black = 0, 0, 0

img = pygame.image.load('intro_ball.gif')

screen = pygame.display.set_mode(size)

black = (255,255,255)

start = [100, 200]

end = [150,200]

pressed_butt = False




while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
           pressed_butt = True

        if event.type == pygame.KEYUP:
           pressed_butt = False
            

        if pressed_butt:
            end[0] += 5

    j = pygame.draw.line(screen, black, start, end, 25)


    


    #screen.fill(black)
    #screen.blit(j)
    pygame.display.update()
    main_clock.tick(framerate)