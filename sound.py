import pygame

pygame.mixer.init()

sTetris = pygame.mixer.Sound('tetris.wav')
sPerfect = pygame.mixer.Sound('allclear.wav')
sBack = pygame.mixer.Sound('back.wav')
sClear = pygame.mixer.Sound('clear.wav')
sClick = pygame.mixer.Sound('click.wav')
sCombo1 = pygame.mixer.Sound('combo1.wav')
sCombo2 = pygame.mixer.Sound('combo2.wav')
sCombo3 = pygame.mixer.Sound('combo3.wav')
sCombo4 = pygame.mixer.Sound('combo4.wav')
sCombo5 = pygame.mixer.Sound('combo5.wav')
sCount1 = pygame.mixer.Sound('count1.wav')
sCount2 = pygame.mixer.Sound('count2.wav')
sCount3 = pygame.mixer.Sound('count3.wav')
sDeath = pygame.mixer.Sound('death.wav')
sFinish = pygame.mixer.Sound('finish.wav')
sHarddrop = pygame.mixer.Sound('harddrop.wav')
sHold = pygame.mixer.Sound('hold.wav')
sHover = pygame.mixer.Sound('hover.wav')
sLevelup = pygame.mixer.Sound('levelup.wav')
sMove = pygame.mixer.Sound('move.wav')
sSpin = pygame.mixer.Sound('spin.wav')
sStart = pygame.mixer.Sound('start.wav')

soundlist = [sTetris, sPerfect, sBack, sClear, sClick, sCombo1, sCombo2, sCombo3, sCombo4, sCombo5,
          sCount1, sCount2, sCount3, sDeath, sFinish, sHarddrop, sHold, sHover, sLevelup,
          sMove, sSpin, sStart]