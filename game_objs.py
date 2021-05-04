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
        self.GRAV = 1
        self.DENSITY = 1
        self.radius = 1
        self.growing = True
        self.id = id
        self.vel = [0,0] if self.id == 0 else  [random.uniform(0,0.10),random.uniform(0,0.10)]

    def grow(self):
        if pygame.mouse.get_pressed()[0] == 1 and self.growing:
            self.radius += 0.5
        else:
            self.growing = False
            print(self.radius)

    def get_volume(self):
        return (4/3) * math.pi * ((self.radius) ** 3)

    def get_mass(self):
        return self.get_volume() * self.DENSITY

    def set_vels(self, planets):
        if not self.growing:
            for planet in planets:
                if planet.id != self.id and not planet.growing:
                    dt = 0.00001
                    #r_hat = self.pos
                    # calculate x and y total distance
                    r = tuple(map(lambda i, j: i -j, planet.pos, self.pos))
                    distance = math.sqrt(r[0]**2 + r[1]**2)
                    # calculate gravitational force
                    G = self.GRAV * ((planet.get_mass() * self.get_mass()) / (distance ** 2)) 

                    # get rs
                    r_mag = math.sqrt(r[0]**2 + r[1]**2)
                    r_hat = tuple([i/r_mag for i in r])

                    r_hat_x = ((self.GRAV * (self.get_mass()/r_mag**2)) * r_hat[0]) * dt
                    r_hat_y = ((self.GRAV * (self.get_mass()/r_mag**2)) * r_hat[1]) * dt
                    planet.vel[0] -= r_hat_x
                    planet.vel[1] -= r_hat_y



    def update_pos(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.last_pos = self.pos

    def update(self, planets):

        if self.growing:
            self.grow()

        self.set_vels(planets)
        self.update_pos()
        #print(self.vel, self.pos)
        pygame.draw.circle(self.screen, (255,255,255), self.pos, self.radius)
        if self.id == 1:
            print(self.pos)
        


        



        

        


