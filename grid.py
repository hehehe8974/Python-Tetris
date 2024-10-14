import pygame
from settings import Color, Shape
import random
class Grid:
    def __init__(self):
        self.numRows = 20
        self.numColumns = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.numColumns)] for i in range(self.numRows)] 
        self.color = Color.getColor()
    
    def printGrid(self):
        for i in range(self.numRows):
            for j in range(self.numColumns):
                print(self.grid[i][j], end = " ")
            print()
        print("########################################")

    def isInside(self, row, column):
        if row >= 0 and row < self.numRows and column >= 0 and column < self.numColumns:
            return True
        return False

    def isEmpty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    def isRowFull(self, row):
        for i in range(self.numColumns):
            if self.grid[row][i] == 0:
                return False
        return True
    
    def isLeft(self, column):
        if column < 0:
            return True
        
    def isRight(self, column):
        if column > 9:
            return True 
        
    def isBottom(self, row):
        if row > 19:
            return True

    def isTop(self, row):
        if row <= 0:
            return True
    
    def damage(self, line, screen):
        row = 19
        for i in range(self.numRows):
            for j in range(self.numColumns):
                if self.grid[i][j] != 0:
                    row = i
                    break
            if row != 19:
                break
        if row <= line:
            for i in range(self.numRows):
                for j in range(self.numColumns):
                    self.grid[i][j] = 9
            return True
        else:
            self.moveRowUp(line)
            return False

    def clearRow(self, row):
        for i in range(self.numColumns):
            self.grid[row][i] = 0
    
    def moveRowDown(self, row, numRows):
        for i in range(self.numColumns):
            self.grid[row + numRows][i] = self.grid[row][i]
            self.grid[row][i] = 0
    
    def moveRowUp(self, line):
        column = random.randint(0, 9)
        for i in range(self.numRows):
            for j in range(self.numColumns):
                if i <= line:
                    pass
                else:
                    self.grid[i-line][j] = self.grid[i][j]
                    if j != column:
                        self.grid[i][j] = 9
                    else:
                        self.grid[i][j] = 0

    def clearRowFull(self):
        completed = 0
        for i in range(self.numRows -1, 0, -1):
            if self.isRowFull(i):
                self.clearRow(i)
                completed = completed + 1
            elif completed > 0:
                self.moveRowDown(i, completed)
        return completed

    def reset(self):
        for i in range(self.numRows):
            for j in range(self.numColumns):
                self.grid[i][j] = 0

    def perfect(self):
        for i in range(self.numRows):
            for j in range(self.numColumns):
                if self.grid[i][j] != 0:
                    return False
        return True

    def draw(self, screen, game):
        for i in range(self.numRows):
            for j in range(self.numColumns):
                cell = self.grid[i][j]
                if game == '2p':
                    rectCell = pygame.Rect(j*self.cell_size + 211, i*self.cell_size + 11, self.cell_size - 1, self.cell_size - 1)
                else:
                    rectCell = pygame.Rect(j*self.cell_size + 411, i*self.cell_size + 11, self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.color[cell], rectCell)