
import pygame
from pygame.locals import *
import time
import random
"""----------------------------
Coś tam zrobiłam ale wymaga dopracowania XD, w każdym razie poczatek mamy
wymiary kratki - 30x30px - takie wymiary rysunkow!!!!
wielkosc okna 900x600px
MAMY NEVERENDINGSTORYYY
-----------------------------------"""
class Apple():
    def __init__(self, okno, kratka):
        self.image = pygame.image.load("apple.png").convert() 
        self.owoce= [pygame.image.load("apple.png").convert(), pygame.image.load("cucumber.png").convert(),pygame.image.load("banana.png").convert(), pygame.image.load("cherry.png").convert(),pygame.image.load("orange.png").convert()]
        self.okno = okno
        self.size = kratka
        self.x, self.y = 5*self.size, 2*self.size #POCZATKOWE polozenie jablka na planszy (wspolrzedne)

    def draw(self):
        self.okno.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def new_position(self):
        self.image=random.choice(self.owoce) #zeby bylo ciekawie wiecej owockow!
        self.x=random.randint(0,29)*30 #zeby nam nie wywalilo poza okno - (900-30)=870, 29*30=870
        self.y=random.randint(0,19)*30


class Snake():
    def __init__(self, okno, dlugosc, kratka):
        self.dlugosc = dlugosc
        self.okno = okno
        self.head = pygame.image.load("hd.png").convert() #glowa nie moze byc taka sama jak cialko, potrzeba oczu
        self.block = pygame.image.load("kl.png").convert()
        self.size= kratka
        self.x = [self.size]*dlugosc
        self.y =[self.size]*dlugosc
        self.direction = "down" #kierunek na poczatku
        
    def return_dlugosc(self):
        return self.dlugosc

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
            if self.direction!="down" or self.dlugosc==1:
                self.direction="up"
        elif key=="down":
            if self.direction!="up" or self.dlugosc==1:
                self.direction="down"
        elif key=="left":
            if self.direction!="right" or self.dlugosc==1:
                self.direction="left"
        elif key=="right":
            if self.direction!="left" or self.dlugosc==1:
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

    # def is_dead(self(:

class Snakegame():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake z przeszkodami") #nazwa gry
        self.scrn_width, self.scrn_height = 900, 600 
        self.surface = pygame.display.set_mode((self.scrn_width, self.scrn_height)) #rysuje powierzchnie do gry
        self.surface.fill((0,64,0)) #kolorek, wybralam taki (teraz chyba juz ladny), ale ocencie sami
        self.kratka = 30
        self.snake=Snake(self.surface,1,self.kratka) #snake, na poczatku ma dlugosc 1
        self.snake.draw() #rysuje snake'a
        self.apple = Apple(self.surface, self.kratka)
        self.apple.draw()

        
        
    def eat_apple(self, x1, y1, x2, y2): #sprawdza czy snake zjadl jablko (jego glowa na miejscu owocu)
        if x1==x2 and y1==y2:
            self.snake.dodaj_ogon()
            return True
        else:
            return False

    def show_score(self):
        font = pygame.font.SysFont('comicsans',30) #ustala wlasciwosci czcionki
        score = font.render(f"Points: {self.snake.dlugosc - 1}", True, (255,255,255)) #kolor bialy, mozna zmienic ale imo jest ok
        self.surface.blit(score, (self.scrn_width - 300,10)) #pokazuje punkty

    def apple_on_tail(self):
        for i in range(0,self.snake.return_dlugosc()):
            if self.snake.x[i]==self.apple.x and self.snake.y[i]==self.apple.y:
                print("japko na ogonie")
                return True
        return False        

    def run(self):
        game = True
        while game:
            for event in pygame.event.get(): #pobiera info o klawiszach
                if event.type == pygame.QUIT: #zamyka okno
                    game = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE: 
                        game=False
                    #rusza snake'm
                    elif event.key == K_UP: 
                        self.snake.move("up")
                    elif event.key == K_DOWN:
                        self.snake.move("down")
                    elif event.key == K_RIGHT:
                        self.snake.move("right")
                    elif event.key == K_LEFT:
                        self.snake.move("left")
                        
            #jeśli dotknie ramki - koniec gry [messagebox orientacyjny!]
            if self.snake.x[0] > 870 or self.snake.x[0] < 0 or self.snake.y[0] > 570 or self.snake.y[0] < 0:
                time.sleep(1)
                #tu może być messagebox z informacją o końcu gry
                game = False
                
            if self.eat_apple(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y): #nowa pozycja dla jablka
                self.apple.new_position()
            #wyswietla jablko, snake'a i punkty
            while self.apple_on_tail():
                self.apple.new_position()            
            
            self.snake.walk() 
            self.apple.draw()
            self.show_score() 
            pygame.display.flip() #update obrazu
            
            if self.snake.return_dlugosc()<5:
                time.sleep(0.2) #im wieksza wartosc tym wolniej snake chodzi
            elif self.snake.return_dlugosc()>=5 and self.snake.return_dlugosc()<10:
                time.sleep(0.15)
            elif self.snake.return_dlugosc()>=10:
                time.sleep(0.08)
            elif self.snake.return_dlugosc()>=40:
                time.sleep(0.05)


game = Snakegame()
game.run()
