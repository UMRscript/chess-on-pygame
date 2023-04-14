import pygame 
from game_config import *
pygame.init()

fnt_num = pygame.font.Font(FNT_PATH, FNT_SIZE)

class Cheesboard:
    def __init__(self, parent_surface: pygame.Surface,
                 cell_qty: int=CELL_QTY, cell_size: int = CELL_SIZE):
        self.__screen = parent_surface
        self.__draw_playboard(cell_qty, cell_size)
        pygame.display.update()

    def __draw_playboard(self, cell_qty, cell_size):
        total_width = cell_qty * cell_size
        num_fields = self.__create_num_fields(cell_qty, cell_size)
        fields = self.__create_all_cells(cell_qty, cell_size)
        num_fields_depth = num_fields[0].get_width()
        playboard_view = pygame.Surface((
          2 * num_fields_depth + total_width,
          2 * num_fields_depth + total_width
        ))
        playboard_view.blit(num_fields[0],
                            (0, num_fields_depth)),
        playboard_view.blit(num_fields[0], 
                            (num_fields_depth + total_width, num_fields_depth))        
        playboard_view.blit(num_fields[1], 
                            (num_fields_depth, 0))
        playboard_view.blit(num_fields[1], 
                            (num_fields_depth, num_fields_depth + total_width))
        playboard_view.blit(fields, 
                            (num_fields_depth, num_fields_depth))
        
        playboard_rect = playboard_view.get_rect()
        playboard_rect.x += (self.__screen.get_width() - playboard_rect.width) // 2
        playboard_rect.y += (self.__screen.get_height() - playboard_rect.height) // 2
        self.__screen.blit(playboard_view, playboard_rect)


    def __create_num_fields(self, cell_qty, cell_size):
        n_lines = pygame.Surface((cell_qty * cell_size, cell_size // 3))
        n_rows = pygame.Surface((cell_size // 3, cell_qty * cell_size))

        for i in range(0, cell_qty):
            letter = fnt_num.render(LTRS[i], 1, WHITE)
            number = fnt_num.render(str(cell_qty - i), 1, WHITE)
            n_lines.blit(letter, (
                i * cell_size + (cell_size - letter.get_rect().width) // 2, #X
                (n_lines.get_height() - letter.get_rect().height) // 2 #Y
                )
            )
            n_rows.blit(number, (
                (n_rows.get_width() - letter.get_rect().width) // 2, #x
                i * cell_size + (cell_size - number.get_rect().height) // 2 #y
                )
            )
        return (n_rows, n_lines)
    
    def __create_all_cells(self, cell_qty, cell_size):
    #Board
        fields = pygame.Surface((cell_qty * cell_size, cell_qty * cell_size))
        is_even_qty = (cell_qty % 2 == 0)
        cell_color_index = 1 if (is_even_qty) else 0
        for y in range(cell_qty):
            for x in range(cell_qty):
                cell = pygame.Surface((cell_size, cell_size))
                cell.fill((COLORS[cell_color_index]))
                fields.blit(cell, (x*cell_size, y*cell_size))
                cell_color_index ^= True #Бинарный XOR
            cell_color_index = cell_color_index ^ True if (is_even_qty) else cell_color_index
        return fields