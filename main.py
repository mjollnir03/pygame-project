#Ellmaer Ranjber

import pygame as pg 
from sys import exit
from settings import *

class Main(): 
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.clock = pg.time.Clock()
        self.screen.fill("white")

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN: 
                if event.key == pg.K_w:
                    print("w")
                if event.key == pg.K_a:
                    print("a")
                if event.key == pg.K_s:
                    print("s")
                if event.key == pg.K_d:
                    print("d")
                    
    def update(self):
            pg.display.update()
            self.clock.tick(60)

    def run(self):
        while (True):
            self.event_loop()
            self.update()
            player.draw(self.screen)


class Player(pg.sprite.Sprite, Main):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (200,300))

#Run the program
main = Main()
player = pg.sprite.GroupSingle()
player.add(Player())
main.run()

