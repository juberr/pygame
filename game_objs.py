import pygame

class Line:

    def __init__(self, screen, colour, start, end, width):
        self.start = start
        self.end = end
        self.colour = colour
        self.screen = screen
        self.width = width
        self.line = pygame.draw.line(self.screen, self.colour, self.start, self.end, self.width)


    def move(self, vel):
        self.end[0] += vel
        self.line = pygame.draw.line(self.screen, self.colour, self.start, self.end, self.width)