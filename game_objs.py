import pygame

class Line:

    def __init__(self, screen, width):
        self.start = pygame.mouse.get_pos()
        self.colour = [250, 250, 250]
        self.screen = screen
        self.width = width
        self.cursor = pygame.image.load('cursor.png')
        self.cursor = pygame.transform.scale(self.cursor, (60, 60))

    def draw(self):

        curr_pos = [i-30 for i in list(pygame.mouse.get_pos())]

        self.screen.blit(self.cursor, curr_pos)
        



        

        


