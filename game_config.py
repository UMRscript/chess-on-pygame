import pygame

WINDOWS_SIZE = (700, 700)

CELL_SIZE = 70
CELL_QTY = 8

#Upload color of cell and just color
LIGHT_BROWN = (222, 184, 135)
DARK_BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND = (150,90,30)
COLORS = ['black_cell.jpg', 'white_cell.jpg']
ACTIVE_CELL_COLOR = (174, 111, 237, 64)

#Загрузка изоображений
IMG_PATH = 'assets/Images/'
WIN_BG_IMG = 'back_window.jpg'
BOARD_BG_IMG = 'back_BOARD.jpg'

# Шрифт
# font = pygame.font.Font(None, 36)
FNT_PATH = 'assets/Font/Srbija_Sans.otf'
FNT_SIZE = 18
LTRS = 'abcdefghijlkmnopqrstuvwxyz'


# задаем координаты начальной клетки
x = 0
y = 0

PIECE_PATH = 'assets/pieces/'

# Рсскодировка шахматных символов
PIECES_TYPES = {
    'k':('King', 'b'), 'K':('King', 'w'),
    'q':('Queen', 'b'), 'Q':('Queen', 'w'),
    'r':('Rook', 'b'), 'R':('Rook', 'w'),
    'b':('Bishop', 'b'), 'B':('Bishop', 'w'),
    'n':('Knight', 'b'), 'N':('Knight', 'w'),
    'p':('Pawn', 'b'), 'P':('Pawn', 'w')
}
 