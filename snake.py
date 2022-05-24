
import pygame
from pygame.locals import *
import time
import random
"""----------------------------
Coś tam zrobiłam ale wymaga dopracowania XD, w każdym razie poczatek mamy
wymiary kratki - 50x50px
wielkosc okna 600x600px
-----------------------------------"""
class Apple():
    def __init__(self, okno, kratka):
        self.image = pygame.image.load("apple.png").convert()
        self.okno = okno
        self.size = kratka
        self.x, self.y = 5*self.size, 2*self.size #polozenie jablka na planszy (wspolrzedne)

    def draw(self):
        self.okno.blit(self.image, (self.x, self.y))
        pygame.display.flip()

class Snake():
    def __init__(self, okno, dlugosc, kratka):
        self.dlugosc = dlugosc
        self.okno = okno
        self.head = pygame.image.load("head.png").convert()
        self.block = pygame.image.load("klocek.png").convert()
        self.size= kratka
        self.x = [self.size]*dlugosc
        self.y =[self.size]*dlugosc
        self.direction = "up"

    def draw(self):
        self.okno.fill((93,185,127))
        for i in range(self.dlugosc):
            if i==0:
                self.okno.blit(self.head, (self.x[i], self.y[i]))
            else:
                self.okno.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move(self, key): #nadaje kierunek wezowi
        if key=="up":
            self.direction="up"
        elif key=="down":
            self.direction="down"
        elif key=="left":
            self.direction="left"
        elif key=="right":
            self.direction="right"

    def walk(self): #robi żeby szedl klocek za klockiem
        for i in range(self.dlugosc-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]
        if self.direction=="up":
            self.y[0]-=self.size
            self.draw()
        elif self.direction=="down":
            self.y[0]+=self.size
            self.draw()
        elif self.direction=="left":
            self.x[0]-=self.size
            self.draw()
        elif self.direction=="right":
            self.x[0]+=self.size
            self.draw()

class Snakegame():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake z przeszkodami")
        self.scrn_width, self.scrn_height = 900, 600
        self.surface = pygame.display.set_mode((self.scrn_width, self.scrn_height)) #rysuje powierzchnie do gry
        self.surface.fill((93,185,127)) #kolorek, wybralam taki brzydki, ale to sie zmieni
        self.kratka = 30
        self.snake=Snake(self.surface,5,self.kratka) #idk, zeby bylo latwiej na razie snake jest z dlugoscia 5 zeby bylo widac jak dziala (gra w powijakach! xd0
        self.snake.draw()
        self.apple = Apple(self.surface, self.kratka)
        self.apple.draw()
        self.points=0

    def eat_apple(self, x1, y1, x2, y2): #sprawdza czy snake zjadl jablko
        if x1==x2 and y1==y2:
            self.points+=1
            print(self.points)
            return True
        else:
            return False


    def run(self):
        game = True
        while game:
            for event in pygame.event.get(): #pobiera info o klawiszach
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
            if self.eat_apple(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
                #czary mary, jablko zmienia pozycje (Trzeba zrobic randoma)
                self.apple.x=random.randint(0,29)*self.kratka #random.randint(0,550) - kratka ma 50! - ale jeszcze trzeba zrobić zeby losowalo co 50, bo dziwnie inaczej
                self.apple.y=random.randint(0,19)*self.kratka
            self.snake.walk()
            self.apple.draw()
            time.sleep(0.3)


game = Snakegame()
game.run()
