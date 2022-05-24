
import pygame
from pygame.locals import *
import time
import random
"""----------------------------
Coś tam zrobiłam ale wymaga dopracowania XD, w każdym razie poczatek mamy
wymiary kratki - 50x50px
wielkosc okna 600x600px
MAMY NEVERENDINGSTORYYY
-----------------------------------"""
class Apple():
    def __init__(self, okno, kratka):
        self.image = pygame.image.load("apple.png").convert()
        self.owoce= [pygame.image.load("apple.png").convert(), pygame.image.load("cucumber.png").convert(),pygame.image.load("banana.png").convert(), pygame.image.load("cherry.png").convert(),pygame.image.load("orange.png").convert()]
        self.okno = okno
        self.size = kratka
        self.x, self.y = 5*self.size, 2*self.size #polozenie jablka na planszy (wspolrzedne)

    def draw(self):

        self.okno.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def new_position(self, kratka):
        self.image=random.choice(self.owoce)
        self.x=random.randint(0,29)*kratka #zeby nam nie wywalilo poza okno - (900-30)=870, 29*30=870
        self.y=random.randint(0,19)*kratka


class Snake():
    def __init__(self, okno, dlugosc, kratka):
        self.dlugosc = dlugosc
        self.okno = okno
        self.head = pygame.image.load("hd.png").convert()
        self.block = pygame.image.load("kl.png").convert()
        self.size= kratka
        self.x = [self.size]*dlugosc
        self.y =[self.size]*dlugosc
        self.direction = "down"

    def dodaj_ogon(self):
        self.dlugosc+=1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.okno.fill((0,64,0))
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

    # def is_dead(self, scrn_width, scrn_height):
    #     if self.x

class Snakegame():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake z przeszkodami")
        self.scrn_width, self.scrn_height = 900, 600
        self.surface = pygame.display.set_mode((self.scrn_width, self.scrn_height)) #rysuje powierzchnie do gry
        self.surface.fill((0,64,0)) #kolorek, wybralam taki brzydki, ale to sie zmieni
        self.kratka = 30
        self.snake=Snake(self.surface,1,self.kratka) #idk, zeby bylo latwiej na razie snake jest z dlugoscia 5 zeby bylo widac jak dziala (gra w powijakach! xd0
        self.snake.draw()
        self.apple = Apple(self.surface, self.kratka)
        self.apple.draw()

    def eat_apple(self, x1, y1, x2, y2): #sprawdza czy snake zjadl jablko
        if x1==x2 and y1==y2:
            self.snake.dodaj_ogon()
            return True
        else:
            return False

    def show_score(self):
        font = pygame.font.SysFont('comicsans',30)
        score = font.render(f"Points: {self.snake.dlugosc - 1}", True, (255,255,255))
        self.surface.blit(score, (self.scrn_width - 300,10))


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
                self.apple.new_position(self.kratka)
            self.snake.walk()
            self.apple.draw()
            self.show_score()
            pygame.display.flip()
            time.sleep(0.1)


game = Snakegame()
game.run()
