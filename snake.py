
import pygame
from pygame.locals import *
import time
"""----------------------------
Coś tam zrobiłam ale wymaga dopracowania XD, w każdym razie poczatek mamy
wymiary kratki - 50x50px
wielkosc okna 600x600px
-----------------------------------"""
class Apple():
    def __init__(self, okno):
        self.image = pygame.image.load("apple.png").convert()
        self.okno = okno
        self.size = 50 
        self.x, self.y = 50, 100 #polozenie jablka na planszy (wspolrzedne)

    def draw(self):
        self.okno.blit(self.image, (self.x, self.y))
        pygame.display.flip()

class Snake():
    def __init__(self, okno, dlugosc):
        self.dlugosc = dlugosc
        self.okno = okno
        self.block = pygame.image.load("klocek.png").convert()
        self.size=50
        self.x = [self.size]*dlugosc 
        self.y =[self.size]*dlugosc
        self.direction = "up"

    def draw(self):
        self.okno.fill((93,185,127))
        for i in range(self.dlugosc):
            self.okno.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move(self, key):
        if key=="up":
            self.direction="up"
        elif key=="down":
            self.direction="down"
        elif key=="left":
            self.direction="left"
        elif key=="right":
            self.direction="right"

    def walk(self):
        for i in range(self.dlugosc-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]
        if self.direction=="up":
            self.y[0]-=50
            self.draw()
        elif self.direction=="down":
            self.y[0]+=50
            self.draw()
        elif self.direction=="left":
            self.x[0]-=50
            self.draw()
        elif self.direction=="right":
            self.x[0]+=50
            self.draw()


class Snakegame():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake z przeszkodami")
        self.surface = pygame.display.set_mode((600, 600))
        self.surface.fill((93,185,127))
        self.snake=Snake(self.surface,5)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def run(self):
        game = True
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game=False
                    elif event.key == K_UP:
                        self.snake.move("up")
                    elif event.key == K_DOWN:
                        self.snake.move("down")
                    elif event.key == K_RIGHT:
                        self.snake.move("right")
                    elif event.key == K_LEFT:
                        self.snake.move("left")
            self.snake.walk()
            self.apple.draw()
            time.sleep(0.3)


game = Snakegame()
game.run()


        

      
    
