import pygame

class Cursor:

    def __init__(self, screen, width):
        self.start = pygame.mouse.get_pos()
        self.colour = [250, 250, 250]
        self.screen = screen
        self.width = width
        self.cursor = pygame.image.load('cursor.png')
        self.cursor = pygame.transform.scale(self.cursor, (60, 60))

    def update(self):

        curr_pos = [i-30 for i in list(pygame.mouse.get_pos())]

        self.screen.blit(self.cursor, curr_pos)


class Ball:


    def __init__(self, screen):
        self.screen = screen
        self.pos = [i-30 for i in list(pygame.mouse.get_pos())]
        self.ball = pygame.image.load('cursor.png')
        self.ball = pygame.transform.scale(self.ball, (60, 60))

    def spawn(self):
        self.screen.blit(self.ball, self.pos)

    def update(self):
        self.pos[1] += 5
        self.screen.blit(self.ball, self.pos)


#class World;
        



        

        


