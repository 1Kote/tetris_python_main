from colors import Colors
import pygame
from position import Position

class Block:
    #METODO QUE DEFINE OS ATRIBUTOS DE CADA PEÇA DE TETRIS
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0 
        self.colors = Colors.get_cell_colors()

    #METODO PARA MEXER AS PEÇAS DE TETRIS
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns   

    #METODO QUE RETORNA A POSIÇÃO ATUAL DAS PEÇAS DE TETRIS
    def get_cell_positions(self):
        titles = self.cells[self.rotation_state]
        moved_titles = []
        for position in titles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_titles.append(position)
        return moved_titles

    #METODO QUE DESENHA AS PEÇAS NA TELA E DESENHA A GRID DO JOGO
    def draw(self, screen):
        titles = self.get_cell_positions()
        for title in titles:
            title_rect = pygame.Rect(title.column*self.cell_size + 1, title.row * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], title_rect)