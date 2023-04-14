from game_config import *
from chees_items import *


#Сoздание окна и заголовка
screen = pygame.display.set_mode((WINDOWS_SIZE))
pygame.display.set_caption("Chees")
clock = pygame.time.Clock()
screen.fill(BACKGROUND)

cheesboard = Cheesboard(screen)

#Цикл обработки сбытий 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            exit()

pygame.quit()