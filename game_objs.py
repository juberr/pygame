import pygame
import math

class Cursor:

    def __init__(self, screen, width):
        self.start = pygame.mouse.get_pos()
        self.colour = [250, 250, 250]
        self.screen = screen
        self.width = width
        self.cursor = pygame.image.load('cursor.png')
        self.cursor = pygame.transform.scale(self.cursor, (20, 20))

    def update(self):

        curr_pos = [i-10 for i in list(pygame.mouse.get_pos())]

        self.screen.blit(self.cursor, curr_pos)


class Planet:

    def __init__(self, screen, id):
        self.screen = screen
        self.pos = pygame.mouse.get_pos()
        self.radius = 0
        self.growing = True
        self.planet = pygame.draw.circle(self.screen, (255,255,255), self.pos, self.radius)
        self.id = id

    def grow(self):
        if pygame.mouse.get_pressed()[0] == 1 and self.growing:
            self.radius += 0.5
        else: self.growing = False


    def update(self):
        self.grow()
        pygame.draw.circle(self.screen, (255,255,255), self.pos, self.radius)
        


        



        

        


