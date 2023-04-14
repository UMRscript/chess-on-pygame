import pygame

pygame.init()


WINDOWS_SIZE = (700, 700)

CELL_SIZE = 70
CELL_QTY = 8

#Сoздание окна и заголовка
screen = pygame.display.set_mode((WINDOWS_SIZE))
pygame.display.set_caption("Chees")


#Upload color of cell and just color
LIGHT_BROWN = (222, 184, 135)
DARK_BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND = (150,90,30)
COLORS = [DARK_BROWN, LIGHT_BROWN]

# Шрифт
font = pygame.font.Font(None, 36)
LTRS = 'abcdefghijlkmnopqrstuvwxyz'

# задаем координаты начальной клетки
x = 0
y = 0
pos = (x, y)
# Инициолизация контента
screen.fill(BACKGROUND)
n_lines = pygame.Surface((CELL_QTY*CELL_SIZE, CELL_SIZE //2), pygame.SRCALPHA)
n_rows = pygame.Surface((CELL_SIZE //2, CELL_QTY*CELL_SIZE), pygame.SRCALPHA)
fields = pygame.Surface((CELL_QTY*CELL_SIZE, CELL_QTY*CELL_SIZE), pygame.SRCALPHA)
board = pygame.Surface((
    2*n_rows.get_width() + fields.get_width(),
    2*n_lines.get_height() + fields.get_height()
), pygame.SRCALPHA)


#Board
is_even_qty = (CELL_QTY % 2 == 0)
cell_color_index = 1 if (is_even_qty) else 0
for y in range(CELL_QTY):
    for x in range(CELL_QTY):
        # pygame.draw.rect(screen, COLORS[cell_color_index] ,(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE ))
        cell = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        cell.fill((COLORS[cell_color_index]))
        fields.blit(cell, (x*CELL_SIZE, y*CELL_SIZE))
        cell_color_index ^= True #Бинарный XOR
    cell_color_index = cell_color_index ^ True if (is_even_qty) else cell_color_index

#Numbers and Text
for i in range(0, CELL_QTY):
    letter = font.render(LTRS[i], 1, WHITE)
    number = font.render(str(CELL_QTY - i), 1, WHITE)
    n_lines.blit(letter, (
        i*CELL_SIZE + (CELL_SIZE - letter.get_rect().width) //2, #x
        (n_lines.get_height() - letter.get_rect().height) //2 #y
        )
    )
    n_rows.blit(number, (
        (n_rows.get_width() - letter.get_rect().width) //2, #x
        i*CELL_SIZE + (CELL_SIZE - number.get_rect().height) //2 #y
        )
    )

board.blit(n_rows, (0, n_lines.get_height()))
board.blit(n_rows, (n_rows.get_width() + fields.get_width(), n_lines.get_height()))
board. blit(n_lines, (n_rows.get_width(), 0))
board. blit(n_lines, (n_rows.get_width(), n_rows.get_width() + fields.get_width()))
board.blit(fields, (n_rows.get_width(), n_lines.get_height()))
screen.blit(board, (
    (WINDOWS_SIZE[0] - board.get_width()) //2,
    (WINDOWS_SIZE[1] - board.get_height()) //2
))
pygame.display.update()


#Цикл обработки сбытий 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x, y = mouse_pos
            if n_rows.get_width() < x < (n_rows.get_width() + fields.get_width()) and \
                n_lines.get_height() < y < (n_lines.get_height() + fields.get_height()):
                cell_x = (x - n_rows.get_width()) // CELL_SIZE
                cell_y = (y - n_lines.get_height()) // CELL_SIZE
                print("Cell coordinates: ", cell_x, cell_y)
        
        


pygame.quit()