from math import radians
import pygame as pg
import sys
from pygame.locals import *

from corpygame import MOUTH_EVENT

FPS = 30
MOUTH_EVENT = USEREVENT+1
BLACK = (0,0,0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

class Point(object):
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

class PacMan(object):
    closed_angles = radians(0), radians(360)
    opened_angles = radians(45), radians(315)
    color = YELLOW
    thickness = 16

    def __init__(self, x=0, y=0, width=1, height=1):
        self.pos = Point(x,y)
        self.widht, self.height = width, height
        self.mouth_closed = False

    def toggle_mouth(self):
        self.mouth_closed = not self.mouth_closed

    def draw(self, surface):
        if self.mouth_closed:
            pg.draw.arc(surface, self.color),
            (int(self.pos.x), int(self.pos.y),
            self.closed_angles[0], self.closed_angles[1],
            self.thickness)
        else:
            pg.init()
            fpsclock = pg.time.Clock()
            screen = pg.display.set_mode((500,400), 0 , 32)
            screen.fill(BLACK)

            pacman = PacMan(250-25, 200-25, 50, 50)
            pg.time.set_timer(MOUTH_EVENT, 333)

        while True:
            screen.fill(BLACK)

            for event in pg.event.get():
                if event.type == MOUTH_EVENT:
                    pacman.toggle_mouth()
                    continue
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

            pacman.draw(screen)

            pg.display.update()
            fpsclock.tick(FPS)




