from grid import Grid
from blocks import *
import random
import pygame
from sound import *
from settings import Color

class Game:
    def __init__(self):
        self.grid = Grid()
        self.color = Color.getColor()
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
        self.totalline = 0
        self.lineleft = 40
        self.doattack = 0

    def attack(self, line):
        self.doattack = line
    
    def damage(self, line):
        self.cBlock.move(-line, 0)
        self.dBlock.move(-line, 0)
        while self.atTop() == True:
            self.cBlock.move(1, 0)

    def level(self):
        #return speed, level
        if self.totalline < 10:
            return 20, 1
        elif self.totalline < 20:
            return 19, 2
        elif self.totalline < 30:
            return 18, 3
        elif self.totalline < 40:
            return 17, 4
        elif self.totalline < 50:
            return 16, 5
        elif self.totalline < 70:
            return 15, 6
        elif self.totalline < 90:
            return 14, 7
        elif self.totalline < 110:
            return 13, 8
        elif self.totalline < 130:
            return 12, 9
        elif self.totalline < 150:
            return 11, 10
        elif self.totalline < 180:
            return 10, 11
        elif self.totalline < 210:
            return 9, 12
        elif self.totalline < 240:
            return 8, 13
        elif self.totalline < 270:
            return 7, 14
        elif self.totalline < 300:
            return 6, 15
        elif self.totalline < 340:
            return 5, 16
        elif self.totalline < 380:
            return 4, 17
        elif self.totalline < 420:
            return 3, 18
        elif self.totalline < 460:
            return 2, 19
        else:
            return 1, 20

    def drawScore(self, line, b):
        if line == 1:
            self.score += 100 + (self.combo*50)
            self.totalline += 1
        elif line == 2:
            self.score += 300 + (self.combo*50)
            self.totalline += 2
        elif line == 3:
            self.score += 500 + (self.combo*50)
            self.totalline += 3
        elif line == 4:
            self.score += 800 + (self.combo*50)
            self.totalline += 4
        self.score += b
        self.combo += 1

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
            self.drawScore(rowcleared, 0)
        else:
            self.combo = 0
        self.usedHold = False
        sHover.play()
        if self.blockFits() == False:
            sDeath.play()
            self.gameover = True
    
    def place40(self):
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
            self.lineleft -= rowcleared
            self.combo += 1
        else:
            self.combo = 0
        self.usedHold = False
        sHover.play()
        if self.blockFits() == False:
            sDeath.play()
            self.gameover = True
        if self.lineleft <= 0:
            sFinish.play()
            self.gameover = True
    
    def place2p(self):
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

    def moveDown40(self):
        self.cBlock.move(1, 0)
        if self.blockInside() == False or self.blockFits() == False:
            self.cBlock.move(-1, 0)
            self.place40()

    def moveDown2p(self):
        self.cBlock.move(1, 0)
        if self.blockInside() == False or self.blockFits() == False:
            self.cBlock.move(-1, 0)
            self.place2p()

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
    
    def space40(self):
        while True:
            self.cBlock.move(1, 0)
            if self.blockInside() == False or self.blockFits() == False:
                self.cBlock.move(-1, 0)
                break
        sHarddrop.play()
        self.place40()

    def space2p(self):
        while True:
            self.cBlock.move(1, 0)
            if self.blockInside() == False or self.blockFits() == False:
                self.cBlock.move(-1, 0)
                break
        sHarddrop.play()
        self.place2p()

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

    def draw(self, screen, game):
        # while self.dblockInside() == False or self.dblockFits() == False:
        #     self.dBlock.move(-1, 0)
        while True:
            self.dBlock.move(1, 0)
            if self.dblockInside() == False or self.dblockFits() == False:
                self.dBlock.move(-1, 0)
                break
        self.grid.draw(screen, game)
        b = self.choosenBlock(self.nBlock)
        h = self.choosenBlock(self.hBlock)

        if game == '2p':
            self.dBlock.draw(screen, 211, 11)
            self.cBlock.draw(screen, 211, 11)
            if self.nBlock == 0:
                b.draw(screen, -55, 165)
            elif self.nBlock == 3:
                b.draw(screen, -55, 155)
            else:
                b.draw(screen, -40, 145)

            if self.hBlock == -1:
                pass
            elif self.hBlock == 0:
                h.draw(screen, -55, 475)
            elif self.hBlock == 3:
                h.draw(screen, -55, 465)
            else:
                h.draw(screen, -40, 455)
        else:
            self.dBlock.draw(screen, 411, 11)
            self.cBlock.draw(screen, 411, 11)
            if self.nBlock == 0:
                b.draw(screen, 655, 290)
            elif self.nBlock == 3:
                b.draw(screen, 655, 280)
            else:
                b.draw(screen, 670, 270)

            if self.hBlock == -1:
                pass
            elif self.hBlock == 0:
                h.draw(screen, 135, 290)
            elif self.hBlock == 3:
                h.draw(screen, 135, 280)
            else:
                h.draw(screen, 160, 270)
            font = pygame.font.Font(None, 50)
            if self.combo > 0:
                combo = font.render('+ ' + str(self.combo) + " COMBO", True, self.color[self.combo])
                screen.blit(combo, (760, 500, 50, 50))
            else:
                pass

    def reset(self):
        self.grid.reset()
        self.num = [0, 1, 2, 3, 4, 5, 6]
        self.cBlock = self.ranBlock()
        self.dBlock = self.choosedBlock(self.cBlock)
        self.cBlock = self.chooseBlock(self.cBlock)
        self.nBlock = self.ranBlock()
        self.score = 0
        self.hBlock = -1
        self.totalline = 0
        self.lineleft = 40
        self.doattack = 0