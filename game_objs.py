import pygame

class Line:

    def __init__(self, screen, colour, start, end, width):
        self.start = start
        self.end = end
        self.colour = colour
        self.screen = screen
        self.width = width
        self.line = pygame.draw.line(self.screen, self.colour, self.start, self.end, self.width)


    def horiz_move(self, vel):

        # add or remove distance to end of line
        self.end[0] += vel

        # if line has no length arbitrarily add one to end, removes visual bug
        if self.end == self.start:
            self.end[0] += 1