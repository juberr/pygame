import pygame
import math
import random
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

    def __init__(self, screen, id, GRAV):
        self.screen = screen
        self.last_pos = None
        self.pos = list(pygame.mouse.get_pos())
        self.GRAV = GRAV
        self.vel = [random.uniform(0,0.05),random.uniform(0,0.05)]
        self.DENSITY = 2 * (10 ** 4)
        self.radius = 1
        self.growing = True
        self.id = id

    def grow(self):
        if pygame.mouse.get_pressed()[0] == 1 and self.growing:
            self.radius += 0.5
        else:
            self.growing = False

    def get_volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

    def get_mass(self):
        return self.get_volume() * self.DENSITY

    def get_gravs(self, planets):
        if not self.growing:
            for planet in planets:
                if planet.id != self.id and not planet.growing:

                    # calculate x and y total distance
                    dx = (planet.pos[0] - self.pos[0])
                    dy = (planet.pos[1] - self.pos[1])

                    distance = math.sqrt(dx**2 + dy**2)

                    angle = math.atan2(dy, dx)

                    # calculate gravitational force
        
                    F = self.GRAV * planet.get_mass() * self.get_mass() / (distance ** 2)
                    
                    self.vel[0] += (math.cos(angle) * F) / self.get_mass()
                    self.vel[1] += (math.sin(angle) * F) / self.get_mass()




    def update_pos(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.last_pos = self.pos

    def update(self, planets):

        if self.growing:
            self.grow()

        self.get_gravs(planets)
        self.update_pos()
        #print(self.vel, self.pos)
        pygame.draw.circle(self.screen, (255,255,255), self.pos, self.radius / 2)
        if self.id == 1:
            print(self.pos)
        


        



        

        


