from game import Game
from grid2 import Grid2
from grid import Grid
from blocks import *
from settings import *
import random
import pygame

class Game2:
    def __init__(self):
        self.grid = Grid2()
        self.game = Game()
        self.num = [0, 1, 2, 3, 4, 5, 6]
        self.cType = 0
        self.cBlock = self.ranBlock()
        self.dBlock = self.choosedBlock(self.cBlock)
        self.cBlock = self.chooseBlock(self.cBlock)
        self.nBlock = self.ranBlock()
        self.gameover = False
        self.score = 0
        self.hBlock = -1
        self.usedHold = False
        self.combo = 0
        self.doattack = 0
    
    def attack(self, line):
        self.doattack = line

    def damage(self, line):
        self.cBlock.move(-line, 0)
        self.dBlock.move(-line, 0)
        while self.atTop() == True:
            self.cBlock.move(1, 0)

    def perfectScore(self, line, b):
        if line == 1:
            self.score += 800
        elif line == 2:
            self.score += 1200
        elif line == 3:
            self.score += 1800
        elif line == 4:
            self.score += 2000
        self.score += b

    def ranBlock(self):
        num = random.choice(self.num)
        self.num.remove(num)
        if len(self.num) == 0:
            self.num = [0, 1, 2, 3, 4, 5, 6]
        return num
    
    def chooseBlock(self, b):
        if b == 0:
            self.cType = 0
            return IBlock()
        elif b == 1:
            self.cType = 1
            return JBlock()
        elif b == 2:
            self.cType = 2
            return LBlock()
        elif b == 3:
            self.cType = 3
            return OBlock()
        elif b == 4:
            self.cType = 4
            return SBlock()
        elif b == 5:
            self.cType = 5
            return TBlock()
        elif b == 6:
            self.cType = 6
            return ZBlock()
        else:
            print('kk')

    def choosedBlock(self, c):
        if c == 0:
            return dIBlock()
        elif c == 1:
            return dJBlock()
        elif c == 2:
            return dLBlock()
        elif c == 3:
            return dOBlock()
        elif c == 4:
            return dSBlock()
        elif c == 5:
            return dTBlock()
        elif c == 6:
            return dZBlock()
        else:
            print('kk')

    def choosenBlock(self, b):
        if b == 0:
            return IBlock()
        elif b == 1:
            return JBlock()
        elif b == 2:
            return LBlock()
        elif b == 3:
            return OBlock()
        elif b == 4:
            return SBlock()
        elif b == 5:
            return TBlock()
        elif b == 6:
            return ZBlock()

    def blockInside(self):
        tiles = self.cBlock.position()
        for i in tiles:
            if self.grid.isInside(i.row, i.column) == False:
                return False
        return True
    
    def blockFits(self):
        tiles = self.cBlock.position()
        for i in tiles:
            if self.grid.isEmpty(i.row, i.column) == False:
                return False
        return True
    
    def dblockInside(self):
        tiles = self.dBlock.position()
        for i in tiles:
            if self.grid.isInside(i.row, i.column) == False:
                return False
        return True
    
    def dblockFits(self):
        tiles = self.dBlock.position()
        for i in tiles:
            if self.grid.isEmpty(i.row, i.column) == False:
                return False
        return True
    
    def atLeft(self):
        tiles = self.cBlock.position()
        for i in tiles:
            if self.grid.isLeft(i.column) == True:
                return True
        return False
    
    def atRight(self):
        tiles = self.cBlock.position()
        for i in tiles:
            if self.grid.isRight(i.column) == True:
                return True
        return False
    
    def atBottom(self):
        tiles = self.cBlock.position()
        for i in tiles:
            if self.grid.isBottom(i.row) == True:
                return True
        return False

    def atTop(self):
        tiles = self.cBlock.position()
        for i in tiles:
            if self.grid.isTop(i.row) == True:
                return True
        return False

    def place(self):
        tiles = self.cBlock.position()
        #Color the grid
        for i in tiles:
            self.grid.grid[i.row][i.column] = self.cBlock.bType
        self.cBlock = self.chooseBlock(self.nBlock)
        self.dBlock = self.choosedBlock(self.nBlock)
        self.nBlock = self.ranBlock()
        rowcleared = self.grid.clearRowFull()
        if rowcleared > 0:
            if self.grid.perfect() == True:
                self.perfectScore(rowcleared, 0)
                sPerfect.play()
            #Row cleared sound
            if rowcleared == 4:
                sTetris.play()
            else:
                sClear.play()
            #Combo sound
            if self.combo == 0:
                sCombo1.play()
            elif self.combo == 1:
                sCombo2.play()
            elif self.combo == 2:
                sCombo3.play()
            elif self.combo == 3:
                sCombo4.play()
            else:
                sCombo5.play()
            self.attack(rowcleared)
        else:
            self.combo = 0
        self.usedHold = False
        sHover.play()
        if self.blockFits() == False:
            sDeath.play()
            self.gameover = True
    
    def moveLeft(self):
        move = True
        self.cBlock.move(0, -1)
        self.dBlock.offsetRow = self.cBlock.offsetRow
        self.dBlock.move(0, -1)
        if self.atLeft() == True:
            self.cBlock.move(0, 1)
            self.dBlock.move(0, 1)
            move = False
        if self.blockFits() == False:
            self.cBlock.move(0, 1)
            self.dBlock.move(0, 1)
            move = False
        if move == True:
            sMove.play()

    def moveRight(self):
        move = True
        self.cBlock.move(0, 1)
        self.dBlock.offsetRow = self.cBlock.offsetRow
        self.dBlock.move(0, 1)
        if self.atRight() == True:
            self.cBlock.move(0, -1)
            self.dBlock.move(0, -1)
            move = False
        if self.blockFits() == False:
            self.cBlock.move(0, -1)
            self.dBlock.move(0, -1)
            move = False
        if move == True:
            sMove.play()
    
    def moveDown(self):
        self.cBlock.move(1, 0)
        if self.blockInside() == False or self.blockFits() == False:
            self.cBlock.move(-1, 0)
            self.place()

    def umoveDown(self):
        self.cBlock.move(1, 0)
        if self.blockInside() == False or self.blockFits() == False:
            self.cBlock.move(-1, 0)

    def space(self):
        while True:
            self.cBlock.move(1, 0)
            if self.blockInside() == False or self.blockFits() == False:
                self.cBlock.move(-1, 0)
                break
        sHarddrop.play()
        self.place()

    def rotate(self):
        if self.atTop() == True:
            self.cBlock.move(1, 0)
        self.cBlock.rotate()
        self.dBlock.offsetRow = self.cBlock.offsetRow
        self.dBlock.rotate()
        wall = ''
        bottom = False
        while self.atLeft() == True:
            self.cBlock.move(0, 1)
            self.dBlock.move(0, 1)
            wall = 'left'
        while self.atRight() == True:
            self.cBlock.move(0, -1)
            self.dBlock.move(0, -1)
            wall = 'Right'
        while self.atBottom() == True:
            self.cBlock.move(-1, 0)
            self.dBlock.move(-1, 0)
            bottom = True
        if self.blockFits() == False:
            self.cBlock.undoRotate()
            self.dBlock.undoRotate()
            while self.blockFits() == False:
                if wall == 'left':
                    self.cBlock.move(0, -1)
                    self.dBlock.move(0, -1)
                if wall == 'Right':
                    self.cBlock.move(0, 1)
                    self.dBlock.move(0, 1)
        elif bottom == True:
            while True:
                self.cBlock.move(1, 0)
                if self.blockInside() == False or self.blockFits() == False:
                    self.cBlock.move(-1, 0)
                    sSpin.play()
                    break
        else:
            sSpin.play()

    def hold(self):
        if self.hBlock == -1:
            self.hBlock = self.cType
            self.cBlock = self.chooseBlock(self.nBlock)
            self.dBlock = self.choosedBlock(self.nBlock)
            self.nBlock = self.ranBlock()
            sHold.play()
        else:
            if self.usedHold == False:
                h = self.hBlock
                self.hBlock = self.cType
                self.cBlock = self.chooseBlock(h)
                self.dBlock = self.choosedBlock(h)
                self.usedHold = True
                sHold.play()

    def draw(self, screen):
        # while self.dblockInside() == False or self.dblockFits() == False:
        #     self.dBlock.move(-1, 0)
        while True:
            self.dBlock.move(1, 0)
            if self.dblockInside() == False or self.dblockFits() == False:
                self.dBlock.move(-1, 0)
                break
        self.grid.draw(screen)
        self.dBlock.draw(screen, 571, 11)
        self.cBlock.draw(screen, 571, 11)
        b = self.choosenBlock(self.nBlock)
        h = self.choosenBlock(self.hBlock)

        if self.nBlock == 0:
            b.draw(screen, 835, 165)
        elif self.nBlock == 3:
            b.draw(screen, 835, 155)
        else:
            b.draw(screen, 850, 145)

        if self.hBlock == -1:
            pass
        elif self.hBlock == 0:
            h.draw(screen, 835, 475)
        elif self.hBlock == 3:
            h.draw(screen, 835, 465)
        else:
            h.draw(screen, 850, 455)

    def reset(self):
        self.grid.reset()
        self.num = [0, 1, 2, 3, 4, 5, 6]
        print('reset')
        print(self.num)
        self.cBlock = self.ranBlock()
        self.dBlock = self.choosedBlock(self.cBlock)
        self.cBlock = self.chooseBlock(self.cBlock)
        self.nBlock = self.ranBlock()
        self.score = 0
        self.hBlock = -1
        self.doattack = 0