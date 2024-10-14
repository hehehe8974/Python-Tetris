import pygame, sys
from game import Game
from settings import Color, Button, Text, VolumeBar, Shape, Image
import settings as s
from grid import Grid
from grid2 import Grid2
from game2 import Game2
from sound import *

timer = pygame.time.get_ticks()
starttime = pygame.time.get_ticks()

#Main setting
pygame.init()

font = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 70)
txtScore = font.render("SCORE", True, Color.white)
txtLevel = font.render("LEVEL", True, Color.white)
txtNext = font.render("NEXT", True, Color.white)
txtLine = font.render("LINES", True, Color.white)
txtHold = font.render("HOLD", True, Color.white)
txtGameover = font.render("GAME OVER", True, Color.white)
txtGameover1 = font.render("PLAYER 2 WINS", True, Color.white)
txtGameover2 = font.render("PLAYER 1 WINS", True, Color.white)
txtTime = font.render("TIME", True, Color.white)
txtLineleft = font.render("LINE LEFT", True, Color.white)


rectScore = pygame.Rect(720, 55, 170, 60)
rectLevel = pygame.Rect(210, 55, 170, 60)
rectLine = pygame.Rect(210, 500, 170, 60)
rectNext = pygame.Rect(720, 215, 170, 180)
rectHold = pygame.Rect(210, 215, 170, 180)

rectNext2 = pygame.Rect(10, 100, 170, 180)
rectHold2 = pygame.Rect(10, 400, 170, 180)

rectNext22 = pygame.Rect(900, 100, 170, 180)
rectHold22 = pygame.Rect(900, 400, 170, 180)

screen = pygame.display.set_mode((1100, 620))
pygame.display.set_caption("TETRIS")

downc = 0
downc2 = 0
clock = pygame.time.Clock()

g = Grid()
game = Game()
game2 = Game2()
g2 = Grid2()
game2 = Game2()


GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 60)

screenType = 'menu'

mVolume = 0.5
for i in soundlist:
        i.set_volume(mVolume)
pygame.mixer.music.set_volume(mVolume)

place = True
placec = 0

place2 = True
placec2 = 0

speed = 20
level = 0
time = font.render("1", True, Color.red)
time2 = font.render("1", True, Color.red)
timec = 0

button = True
start = True

logoImg = pygame.image.load('tetris.gif')
backImg = pygame.image.load('background.gif')

#Button
#Quit
def Quit():
    pygame.quit()
    sys.exit()

#Back button
def back():
    sBack.play()
    bQuit = Button((480, 510), "Quit", 40, Quit)
    bHelp = Button((480, 370), "Help", 40, pgHelp)
    bPlay = Button((480, 300), "Play", 40, pgPlay)
    bAbout = Button((900, 35), 'About', 55, pgAbout)
    bSet = Button((480, 440), "Settings", 40, pgSet)
    logo = Image(logoImg, (380, 50))
    for i in s.texts:
        i.kill()
    for i in s.shapes:
        i.kill()
    for i in s.Gvolumebar:
        i.kill()

#Settings Page
def pgSet():
    global mVolume
    sClick.play()
    tVol = Text((450, 160), "Volume", 60, Color.lightblue)
    bPlus = Button((820, 300), "+", 60, plus)
    bMinus = Button((240, 300), "-", 60, minus)
    bBack = Button((50, 550), "Back", 40, back)
    VolumeBar((300, 310), Color.lightblue)

#Reduce volume
def minus():
    global mVolume
    sClick.play()
    if round(mVolume, 1) > 0:
        mVolume = mVolume - 0.1
    for i in soundlist:
        i.set_volume(mVolume)
    pygame.mixer.music.set_volume(mVolume)
    tVol = Text((450, 160), "Volume", 60, Color.lightblue)
    bPlus = Button((820, 300), "+", 60, plus)
    bMinus = Button((240, 300), "-", 60, minus)
    bBack = Button((50, 550), "Back", 40, back)
    VolumeBar((300, 310), Color.lightblue)

#Increase volume
def plus():
    global mVolume
    sClick.play()
    if round(mVolume, 1) < 1:
        mVolume = mVolume + 0.1
    for i in soundlist:
        i.set_volume(mVolume)
    pygame.mixer.music.set_volume(mVolume)
    tVol = Text((450, 160), "Volume", 60, Color.lightblue)
    bPlus = Button((820, 300), "+", 60, plus)
    bMinus = Button((240, 300), "-", 60, minus)
    bBack = Button((50, 550), "Back", 40, back)
    VolumeBar((300, 310), Color.lightblue)

#Help page
def pgHelp():
    sClick.play()
    sBg = Shape(((200, 50), (900, 50), (900, 500), (200, 500)), Color.lightblue)
    taboutH = Text((410, 55), "How to Play", 45, Color.blue)
    tabout1 = Text((210, 120), "Single Player", 30, Color.blue)
    tabout2 = Text((210, 210), "Move : Right/Down/Left", 25, Color.blue)
    tabout3 = Text((210, 280), "Rotate : Up", 25, Color.blue)
    tabout4 = Text((210, 350), "Place : Space", 25, Color.blue)
    tabout5 = Text((210, 420), "Hold : Hold", 25, Color.blue)
    #Multiplayer
    tabout1 = Text((560, 120), "Multi Player", 30, Color.blue)
    tabout1 = Text((560, 160), "1P", 30, Color.blue)
    tabout2 = Text((560, 210), "A/S/D", 25, Color.blue)
    tabout3 = Text((560, 280), "W", 25, Color.blue)
    tabout4 = Text((560, 350), "F", 25, Color.blue)
    tabout5 = Text((560, 420), "Shift", 25, Color.blue)
    #2P
    tabout1 = Text((680, 160), "2P", 30, Color.blue)
    tabout2 = Text((680, 210), "Right/Down/Left", 25, Color.blue)
    tabout3 = Text((680, 280), "Up", 25, Color.blue)
    tabout4 = Text((680, 350), "K", 25, Color.blue)
    tabout5 = Text((680, 420), "L", 25, Color.blue)
    bBack = Button((50, 550), "Back", 40, back)

#Play button
def pgPlay():
    sClick.play()
    bBack = Button((50, 550), "Back", 40, back)
    b40 = Button((300, 250), "40 LINES", 80, g40)
    bInfinity = Button((300, 100), "INFINITY", 80, gInfinity)
    b2p = Button((300, 400), "2 PLAYERS", 80, g2p)
    
def gInfinity():
    global screenType, starttime
    sClick.play()
    sBg = Shape(((411, 11), (711, 11), (711, 611), (411, 611)), Color.darkblue)
    screenType = 'infinity' #Change to gamemode
    starttime = pygame.time.get_ticks()
    game.reset()

def g2p():
    global screenType, starttime
    sClick.play()
    sBg1 = Shape(((211, 11), (511, 11), (511, 611), (211, 611)), Color.darkblue)
    sBg2 = Shape(((571, 11), (871, 11), (871, 611), (571, 611)), Color.darkblue)
    screenType = '2p' #Change to gamemode
    starttime = pygame.time.get_ticks()
    game.reset()

def g40():
    global screenType, timer, starttime
    sClick.play()
    sBg = Shape(((411, 11), (711, 11), (711, 611), (411, 611)), Color.darkblue)
    screenType = '40' #Change to gamemode
    starttime = pygame.time.get_ticks()
    game.reset()

def resett():
    global screenType, button, start, timec
    sClick.play()
    for i in s.shapes:
        i.kill()
    for i in s.buttons:
        i.kill()
    bQuit = Button((480, 510), "Quit", 40, Quit)
    bHelp = Button((480, 370), "Help", 40, pgHelp)
    bPlay = Button((480, 300), "Play", 40, pgPlay)
    bAbout = Button((900, 35), 'About', 55, pgAbout)
    bSet = Button((480, 440), "Settings", 40, pgSet)
    logo = Image(logoImg, (380, 50))
    game.gameover = False
    game2.gameover = False
    button = True
    start = True
    timec = 0
    screenType = 'menu' #Change to main menu mode

def replay():
    global button, timer, start, starttime, timec
    sClick.play()
    game.reset()
    game2.reset()
    game.gameover = False
    game2.gameover = False
    button = True
    start = True
    timer = pygame.time.get_ticks()
    starttime = pygame.time.get_ticks()
    timec = 0

#About page
def pgAbout():
    sClick.play()
    sBg = Shape(((325, 50), (770, 50), (770, 500), (325, 500)), Color.lightblue)
    taboutH = Text((480, 55), "About", 45, Color.blue)
    tabout1 = Text((360, 140), "Made by : Taehyun Lee", 30, Color.blue)
    tabout2 = Text((360, 210), "2024-2-21", 30, Color.blue)
    tabout3 = Text((360, 280), "London, ON", 30, Color.blue)
    bBack = Button((50, 550), "Back", 40, back)

resett()

while True:
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouse = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if screenType == 'menu':
        screen.blit(backImg, (0, 0))
        s.shapes.update(screen)
        s.buttons.update(screen, events, mouse)
        s.buttons.draw(screen)
        s.texts.update(screen)
        s.texts.draw(screen)
        s.Gvolumebar.update(screen, mVolume)
        s.images.update(screen)
############################################################################
#INFINITY
    elif screenType == 'infinity':
        if start == True:
            if (pygame.time.get_ticks()-starttime)/100 >= 0 and timec == 0:
                time = font2.render("3", True, Color.white)
                sCount3.play()
                timec = 1
            elif (pygame.time.get_ticks()-starttime)/100 >= 10 and timec == 1:
                time = font2.render("2", True, Color.yellow)
                sCount2.play()
                timec = 2
            elif (pygame.time.get_ticks()-starttime)/100 >= 20 and timec == 2:
                time = font2.render("1", True, Color.red)
                sCount1.play()
                timec = 3
            elif (pygame.time.get_ticks()-starttime)/100 >= 30 and timec == 3:
                sStart.play()
                start = False
                timec = 0
                time = font2.render(" ", True, Color.red)
        else:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and game.gameover == False:
                        game.rotate()
                        if placec < 5:
                            place = False
                    if event.key == pygame.K_LEFT and game.gameover == False:
                        game.moveLeft()
                    if event.key == pygame.K_RIGHT and game.gameover == False:
                        game.moveRight()
                    if event.key == pygame.K_SPACE and game.gameover == False:
                        game.space()
                    if event.key == pygame.K_LSHIFT and game.gameover == False:
                        game.hold()
                if keys[pygame.K_DOWN] and game.gameover == False:
                    game.umoveDown()
                    sHover.play()
                    if placec < 5:
                        place = False
                if event.type == GAME_UPDATE and game.gameover == False:
                    downc += 1
                    speed, level = game.level()
                    if downc >= speed:
                        if place == True:
                            game.moveDown()
                            placec = 0
                            downc = 0
                        else:
                            game.umoveDown()
                            placec += 1
                            downc = 0
                        place = True
                if game.gameover == True and button == True:
                    button = False
                    bMenu = Button((950, 500), "Menu", 40, resett)
                    bReplay = Button((750, 500), "Replay", 40, replay)
                    
        drawScore = font.render(str(game.score), True, Color.white)
        drawLevel = font.render(str(level), True, Color.white)
        drawLine = font.render(str(game.totalline), True, Color.white)
        screen.blit(backImg, (0, 0))
        screen.blit(txtScore, (760, 20, 50, 50))
        screen.blit(txtLevel, (255, 20, 50, 50))
        screen.blit(txtLine, (255, 470, 50, 50))
        screen.blit(txtNext, (775, 180, 50, 50))
        screen.blit(txtHold, (255, 180, 50, 50))
        #Draw Score
        pygame.draw.rect(screen, Color.lightblue, rectScore, 0)
        screen.blit(drawScore, drawScore.get_rect(centerx = rectScore.centerx, centery = rectScore.centery))
        #Draw Level
        pygame.draw.rect(screen, Color.lightblue, rectLevel, 0)
        screen.blit(drawLevel, drawLevel.get_rect(centerx = rectLevel.centerx, centery = rectLevel.centery))
        #Draw lines cleared
        pygame.draw.rect(screen, Color.lightblue, rectLine, 0)
        screen.blit(drawLine, drawLine.get_rect(centerx = rectLine.centerx, centery = rectLine.centery))
        #Next block square
        pygame.draw.rect(screen, Color.lightblue, rectNext, 0)
        #Hold block square
        pygame.draw.rect(screen, Color.lightblue, rectHold, 0)
        s.shapes.update(screen)
        game.draw(screen, screenType)
        screen.blit(time, (550, 100, 50, 50))
        s.buttons.update(screen, events, mouse)
        s.buttons.draw(screen)
        if game.gameover == True:
            screen.blit(txtGameover, (800, 450, 50, 50))
############################################################################
#40
    elif screenType == '40':
        if start == True:
            drawTime = font.render("0", True, Color.white)
            if (pygame.time.get_ticks()-starttime)/100 >= 0 and timec == 0:
                time = font2.render("3", True, Color.white)
                sCount3.play()
                timec = 1
            elif (pygame.time.get_ticks()-starttime)/100 >= 10 and timec == 1:
                time = font2.render("2", True, Color.yellow)
                sCount2.play()
                timec = 2
            elif (pygame.time.get_ticks()-starttime)/100 >= 20 and timec == 2:
                time = font2.render("1", True, Color.red)
                sCount1.play()
                timec = 3
            elif (pygame.time.get_ticks()-starttime)/100 >= 30 and timec == 3:
                sStart.play()
                start = False
                timec = 0
                time = font2.render(" ", True, Color.red)
                timer = pygame.time.get_ticks()
        else:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and game.gameover == False:
                        game.rotate()
                        if placec < 5:
                            place = False
                    if event.key == pygame.K_LEFT and game.gameover == False:
                        game.moveLeft()
                    if event.key == pygame.K_RIGHT and game.gameover == False:
                        game.moveRight()
                    if event.key == pygame.K_SPACE and game.gameover == False:
                        game.space40()
                    if event.key == pygame.K_LSHIFT and game.gameover == False:
                        game.hold()
                if keys[pygame.K_DOWN] and game.gameover == False:
                    game.umoveDown()
                    sHover.play()
                    if placec < 5:
                        place = False
                if event.type == GAME_UPDATE and game.gameover == False:
                    downc += 1
                    if downc >= 20:
                        if place == True:
                            game.moveDown40()
                            placec = 0
                            downc = 0
                        else:
                            game.umoveDown()
                            placec += 1
                            downc = 0
                        place = True
                if game.gameover == True and button == True:
                    button = False
                    bMenu = Button((950, 500), "Menu", 40, resett)
                    bReplay = Button((750, 500), "Replay", 40, replay)

        drawLine = font.render(str(game.lineleft), True, Color.white)
        screen.blit(backImg, (0, 0))
        screen.blit(txtTime, (770, 20, 50, 50))
        screen.blit(txtLineleft, (225, 20, 50, 50))
        screen.blit(txtNext, (775, 180, 50, 50))
        screen.blit(txtHold, (255, 180, 50, 50))
        #Draw Score
        pygame.draw.rect(screen, Color.lightblue, rectScore, 0)
        if game.gameover == False and start == False:
            drawTime = font.render(str(round((pygame.time.get_ticks() - timer)/1000, 2)), True, Color.white)
        screen.blit(drawTime, (780, 70))
        #Draw Level
        pygame.draw.rect(screen, Color.lightblue, rectLevel, 0)
        screen.blit(drawLine, drawLine.get_rect(centerx = rectLevel.centerx, centery = rectLevel.centery))
        #Next block square
        pygame.draw.rect(screen, Color.lightblue, rectNext, 0)
        #Hold block square
        pygame.draw.rect(screen, Color.lightblue, rectHold, 0)
        s.shapes.update(screen)
        game.draw(screen, screenType)
        screen.blit(time, (550, 100, 50, 50))
        s.buttons.update(screen, events, mouse)
        s.buttons.draw(screen)
        if game.gameover == True:
            screen.blit(txtGameover, (800, 450, 50, 50))
##########################################################################
#2 PLAYERS
    elif screenType == '2p':
        if start == True:
            if (pygame.time.get_ticks()-starttime)/100 >= 0 and timec == 0:
                time = font2.render("3", True, Color.white)
                time2 = font2.render("3", True, Color.white)
                sCount3.play()
                timec = 1
            elif (pygame.time.get_ticks()-starttime)/100 >= 10 and timec == 1:
                time = font2.render("2", True, Color.yellow)
                time2 = font2.render("2", True, Color.yellow)
                sCount2.play()
                timec = 2
            elif (pygame.time.get_ticks()-starttime)/100 >= 20 and timec == 2:
                time = font2.render("1", True, Color.red)
                time2 = font2.render("1", True, Color.red)
                sCount1.play()
                timec = 3
            elif (pygame.time.get_ticks()-starttime)/100 >= 30 and timec == 3:
                sStart.play()
                start = False
                timec = 0
                time = font2.render(" ", True, Color.red)
                time2 = font2.render(" ", True, Color.white)
        else:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    #1p
                    if event.key == pygame.K_w and game.gameover == False and game2.gameover == False:
                        game.rotate()
                        if placec < 5:
                            place = False
                    if event.key == pygame.K_a and game.gameover == False and game2.gameover == False:
                        game.moveLeft()
                    if event.key == pygame.K_d and game.gameover == False and game2.gameover == False:
                        game.moveRight()
                    if event.key == pygame.K_f and game.gameover == False and game2.gameover == False:
                        game.space2p()
                    if event.key == pygame.K_LSHIFT and game.gameover == False and game2.gameover == False:
                        game.hold()
                    #2p
                    if event.key == pygame.K_UP and game.gameover == False and game2.gameover == False:
                        game2.rotate()
                        if placec2 < 5:
                            place2 = False
                    if event.key == pygame.K_LEFT and game.gameover == False and game2.gameover == False:
                        game2.moveLeft()
                    if event.key == pygame.K_RIGHT and game.gameover == False and game2.gameover == False:
                        game2.moveRight()
                    if event.key == pygame.K_l and game.gameover == False and game2.gameover == False:
                        game2.space()
                    if event.key == pygame.K_k and game.gameover == False and game2.gameover == False:
                        game2.hold()
                if keys[pygame.K_s] and game.gameover == False and game2.gameover == False:
                    game.umoveDown()
                    sHover.play()
                    if placec < 5:
                        place = False
                if keys[pygame.K_DOWN] and game.gameover == False and game2.gameover == False:
                    game2.umoveDown()
                    sHover.play()
                    if placec2 < 5:
                        place2 = False
                if event.type == GAME_UPDATE and game.gameover == False and game2.gameover == False:
                    downc += 1
                    if downc >= 20:
                        if place == True:
                            game.moveDown2p()
                            placec = 0
                            downc = 0
                        else:
                            game.umoveDown()
                            placec += 1
                            downc = 0
                        place = True

                    downc2 += 1
                    if downc2 == 20:
                        if place2 == True:
                            game2.moveDown()
                            placec2 = 0
                            downc2 = 0
                        else:
                            game2.umoveDown()
                            placec2 += 1
                            downc2 = 10
                        place2 = True
                    
                        if game.doattack != 0:
                            if game2.grid.damage(game.doattack, screen) == True:
                                game2.gameover = True
                            game2.damage(game.doattack)
                            game.doattack = 0

                        if game2.doattack != 0:
                            if game.grid.damage(game2.doattack, screen) == True:
                                game.gameover = True
                            game.damage(game2.doattack)
                            game2.doattack = 0

                if game.gameover == True and button == True:
                    button = False
                    bMenu = Button((460, 300), "Menu", 40, resett)
                    bReplay = Button((450, 200), "Replay", 40, replay)
                elif game2.gameover == True and button == True:
                    button = False
                    bMenu = Button((460, 300), "Menu", 40, resett)
                    bReplay = Button((450, 200), "Replay", 40, replay)
                
        screen.blit(backImg, (0, 0))
        drawScore = font.render(str(game.score), True, Color.white)
        screen.blit(txtNext, (65, 60, 50, 50))
        screen.blit(txtHold, (55, 350, 50, 50))
        screen.blit(txtNext, (955, 60, 50, 50))
        screen.blit(txtHold, (945, 350, 50, 50))
        #Next block square
        pygame.draw.rect(screen, Color.lightblue, rectHold2, 0)
        pygame.draw.rect(screen, Color.lightblue, rectNext2, 0)
        #Hold block square
        pygame.draw.rect(screen, Color.lightblue, rectHold22, 0)
        pygame.draw.rect(screen, Color.lightblue, rectNext22, 0)
        s.shapes.update(screen)
        game.draw(screen, screenType)
        game2.draw(screen)
        screen.blit(time, (340, 100, 50, 50))
        screen.blit(time2, (710, 100, 50, 50))
        s.buttons.update(screen, events, mouse)
        s.buttons.draw(screen)
        if game.gameover == True:
            screen.blit(txtGameover1, (420, 100, 50, 50))
        if game2.gameover == True:
            screen.blit(txtGameover2, (420, 100, 50, 50))

    pygame.display.update()
    clock.tick(60)
