from settings import Color
import pygame
from position import Position

class Block:
    def __init__(self, bType):
        self.bType = bType
        self.cells = {}
        self.cell_size = 30
        self.offsetRow = 0
        self.offsetColumn = 0
        self.rotation = 0
        self.color = Color.getColor()
    
    def move(self, rows, columns):
        self.offsetRow = self.offsetRow + rows
        self.offsetColumn = self.offsetColumn + columns
    
    def position(self):
        tiles = self.cells[self.rotation]
        tilesMoved = []
        for i in tiles:
            i = Position(i.row + self.offsetRow, i.column + self.offsetColumn)
            tilesMoved.append(i)
        return tilesMoved
    
    def rotate(self):
        self.rotation = self.rotation + 1
        if self.rotation == len(self.cells):
            self.rotation = 0
    
    def undoRotate(self):
        self.rotation = self.rotation - 1
        if self.rotation == -1:
            self.rotation = len(self.cells) - 1
    
    def draw(self, screen, x, y):
        tiles = self.position()
        for i in tiles:
            rectTile = pygame.Rect(x + i.column * self.cell_size, y + i.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.color[self.bType], rectTile)