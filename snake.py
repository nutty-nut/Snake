import pygame

scrn_width, scrn_height = 500, 500

pygame.init()
window = pygame.display.set_mode((scrn_width, scrn_height))
pygame.display.set_caption("Snake z przeszkodami")
run=True

while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        #kierunek w gore
      elif event.key == pygame.K_DOWN:
        #kierunek w dol
      elif event.key == pygame.K_LEFT:
        #kierunek w lewo
      elif event.key == pygame.K_RIGHT:
        #kierunek w prawo
        
        

      
    
