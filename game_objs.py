import pygame

class Line:

    def __init__(self, screen, width):
        self.start = pygame.mouse.get_pos()
        self.colour = [250, 250, 250]
        self.screen = screen
        self.width = width
        self.cursor = None

    def begin(self):
        pygame.draw.circle(self.screen, self.colour, self.start, self.width)


    def draw(self):

        curr_mouse_pos = pygame.mouse.get_pos()

        pygame.draw.line(self.screen, self.colour, self.start, curr_mouse_pos, self.width)
        pygame.draw.circle(self.screen, self.colour, curr_mouse_pos, self.width/2)
        

        


