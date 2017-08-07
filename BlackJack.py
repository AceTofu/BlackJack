import pygame, sys
import time
from random import randint
import random

pygame.init()

score = 50

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (7, 99, 36)
pink = (255, 51, 51)

displayX = 800
displayY = 600

buttonX = 240
buttonY = 100

button2X = 180
button2Y = 75

logoX = 350
logoY = 300

card_backX = 165
card_backY = 250

cardX = 100
cardY = 150

chipX = 100
chipY = 100

gameDisplay = pygame.display.set_mode((displayX,displayY))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)
big_font = pygame.font.SysFont(None, 45)

play_button = pygame.image.load("play_button.png")
play_button = pygame.transform.scale(play_button, (buttonX,buttonY))

play_button_click = pygame.image.load("play_button_click.png")
play_button_click = pygame.transform.scale(play_button_click, (buttonX,buttonY))

help_button = pygame.image.load("help_button.png")
help_button = pygame.transform.scale(help_button, (buttonX,buttonY))

help_button_click = pygame.image.load("help_button_click.png")
help_button_click = pygame.transform.scale(help_button_click, (buttonX,buttonY))

quit_button = pygame.image.load("quit_button.png")
quit_button = pygame.transform.scale(quit_button, (buttonX,buttonY))

quit_button_click = pygame.image.load("quit_button_click.png")
quit_button_click = pygame.transform.scale(quit_button_click, (buttonX,buttonY))

blackjack_logo = pygame.image.load("blackjack_logo.png")
blackjack_logo = pygame.transform.scale(blackjack_logo, (logoX,logoY))

back_card1 = pygame.image.load("back_card1.png")
back_card1 = pygame.transform.scale(back_card1, (card_backX, card_backY))

back_card1_click = pygame.image.load("back_card1_click.png")
back_card1_click = pygame.transform.scale(back_card1_click, (card_backX, card_backY))

back_card2 = pygame.image.load("back_card2.png")
back_card2 = pygame.transform.scale(back_card2, (card_backX, card_backY))

back_card2_click = pygame.image.load("back_card2_click.png")
back_card2_click = pygame.transform.scale(back_card2_click, (card_backX, card_backY))

back_card3 = pygame.image.load("back_card3.png")
back_card3 = pygame.transform.scale(back_card3, (card_backX, card_backY))

back_card3_click = pygame.image.load("back_card3_click.png")
back_card3_click = pygame.transform.scale(back_card3_click, (card_backX, card_backY))

chip1 = pygame.image.load("chip1.png")
chip1 = pygame.transform.scale(chip1, (chipX, chipY))

chip1_click = pygame.image.load("chip1_click.png")
chip1_click = pygame.transform.scale(chip1_click, (chipX, chipY))

chip5 = pygame.image.load("chip5.png")
chip5 = pygame.transform.scale(chip5, (chipX, chipY))

chip5_click = pygame.image.load("chip5_click.png")
chip5_click = pygame.transform.scale(chip5_click, (chipX, chipY))

chip25 = pygame.image.load("chip25.png")
chip25 = pygame.transform.scale(chip25, (chipX, chipY))

chip25_click = pygame.image.load("chip25_click.png")
chip25_click = pygame.transform.scale(chip25_click, (chipX, chipY))

chip100 = pygame.image.load("chip100.png")
chip100 = pygame.transform.scale(chip100, (chipX, chipY))

chip100_click = pygame.image.load("chip100_click.png")
chip100_click = pygame.transform.scale(chip100_click, (chipX, chipY))

chip_clear = pygame.image.load("chip_clear.png")
chip_clear = pygame.transform.scale(chip_clear, (chipX, chipY))

chip_clear_click = pygame.image.load("chip_clear_click.png")
chip_clear_click = pygame.transform.scale(chip_clear_click, (chipX, chipY))

chip_go = pygame.image.load("chip_go.png")
chip_go = pygame.transform.scale(chip_go, (chipX, chipY))

chip_go_click = pygame.image.load("chip_go_click.png")
chip_go_click = pygame.transform.scale(chip_go_click, (chipX, chipY))

stick_button = pygame.image.load("stick_button.png")
stick_button = pygame.transform.scale(stick_button, (button2X,button2Y))

stick_button_click = pygame.image.load("stick_button_click.png")
stick_button_click = pygame.transform.scale(stick_button_click, (button2X,button2Y))

hit_button = pygame.image.load("hit_button.png")
hit_button = pygame.transform.scale(hit_button, (button2X,button2Y))

hit_button_click = pygame.image.load("hit_button_click.png")
hit_button_click = pygame.transform.scale(hit_button_click, (button2X,button2Y))


def text(msg,colour,textX,textY):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [textX,textY])

def help_text(msg,textY):
    screen_text = font.render(msg, True, white)
    gameDisplay.blit(screen_text, [displayX/20,textY])

def big_text(msg,colour,textX,textY):
    screen_text = big_font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [textX,textY])

def button(x, y, inactive, active, action = None):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + buttonX > cursor[0] > x and y + buttonY > cursor[1] > y:
        gameDisplay.blit(active, (x, y))
        if click[0] == 1 and action != None:
            
            if action == "quit":
                pygame.quit()
                quit()
                
            if action == "help":
                help_screen()
                
            if action == "play":
                choose_card_back()
    else:
        gameDisplay.blit(inactive, (x, y))
                
def bet_screen(back_card,back_card_click):

    bet = 0
    valid_bet = True

    gameExit = False
    while gameExit == False:

        bet_click = 0
            
        gameDisplay.fill(green)

        if valid_bet == False:
            big_text("That is not a valid bet",red,displayX/4,(displayY/60)*28)
            
        big_text("How much would you like to bet?",white,displayX/16,displayY/12)
        big_text("The money you have remaining is",white,displayX/16,displayY/6)
        big_text(str(score),white,displayX/16,displayY/4)
        big_text(str(bet),white,displayX/16,displayY/2)

        gameDisplay.blit(chip1, (displayX/16,(displayY/3)*2))
        gameDisplay.blit(chip5, (displayX/4,(displayY/3)*2))
        gameDisplay.blit(chip25, ((displayX/16)*7,(displayY/3)*2))
        gameDisplay.blit(chip100, ((displayX/16)*10,(displayY/3)*2))
        gameDisplay.blit(chip_clear, ((displayX/16)*13,(displayY/3)*2))
        gameDisplay.blit(chip_go, ((displayX/16)*13 ,(displayY/60)*28))

        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        
        if displayX/16 + chipX > cursor[0] > displayX/16 and (displayY/3)*2 + chipY > cursor[1] > (displayY/3)*2:
            gameDisplay.blit(chip1_click, (displayX/16,(displayY/3)*2))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    bet += 1
                    
        elif displayX/4 + chipX > cursor[0] > displayX/4 and (displayY/3)*2 + chipY > cursor[1] > (displayY/3)*2:
            gameDisplay.blit(chip5_click, (displayX/4,(displayY/3)*2))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    bet += 5
                    
        elif (displayX/16)*7 + chipX > cursor[0] > (displayX/16)*7 and (displayY/3)*2 + chipY > cursor[1] > (displayY/3)*2:
            gameDisplay.blit(chip25_click, ((displayX/16)*7,(displayY/3)*2))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    bet += 25
                    
        elif (displayX/16)*10 + chipX > cursor[0] > (displayX/16)*10 and (displayY/3)*2 + chipY > cursor[1] > (displayY/3)*2:
            gameDisplay.blit(chip100_click, ((displayX/16)*10,(displayY/3)*2))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    bet += 100
                    
        elif (displayX/16)*13 + chipX > cursor[0] > (displayX/16)*13 and (displayY/3)*2 + chipY > cursor[1] > (displayY/3)*2:
            gameDisplay.blit(chip_clear_click, ((displayX/16)*13,(displayY/3)*2))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    bet = 0

        elif (displayX/16)*13 + chipX > cursor[0] > (displayX/16)*13 and (displayY/60)*28 + chipY > cursor[1] > (displayY/60)*28:
            gameDisplay.blit(chip_go_click, ((displayX/16)*13 ,(displayY/60)*28))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if bet == 0 or bet > score:
                        valid_bet = False
                    else:
                        start_deal(bet,score,back_card,back_card_click)
                        
        for event in pygame.event.get():                 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
   
        pygame.display.update()

        
def card_back(x, y, inactive, active, action = None):
    
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + card_backX > cursor[0] > x and y + card_backY > cursor[1] > y:
        gameDisplay.blit(active, (x,y))
        if click[0] == 1 and action != None:

            if action == "back_card1":
                back_card = pygame.image.load("back_card1.png") 
                back_card = pygame.transform.scale(back_card, (cardX, cardY))

                back_card_click = pygame.image.load("back_card1_click.png") 
                back_card_click = pygame.transform.scale(back_card_click, (cardX, cardY))

                bet_screen(back_card,back_card_click)

            if action == "back_card2":
                back_card = pygame.image.load("back_card2.png")
                back_card = pygame.transform.scale(back_card, (cardX, cardY))

                back_card_click = pygame.image.load("back_card2_click.png")
                back_card_click = pygame.transform.scale(back_card_click, (cardX, cardY))
                
                bet_screen(back_card,back_card_click)

            if action == "back_card3":
                back_card = pygame.image.load("back_card3.png")
                back_card = pygame.transform.scale(back_card, (cardX, cardY))

                back_card_click = pygame.image.load("back_card3_click.png")
                back_card_click = pygame.transform.scale(back_card_click, (cardX, cardY))
                
                bet_screen(back_card,back_card_click)
    else:
        gameDisplay.blit(inactive, (x,y))


def help_screen():

    gameExit = False
    
    while gameExit == False:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(green)
        help_text("The aim of blackjack is to get a higher card total than the dealer",displayY/20)
        help_text("However, if you get a total higher than 21, you go 'Bust' and lose",displayY/20*2)
        help_text("You can choose to 'Hit' (get an extra card) or 'Stick'(stop taking cards)",displayY/20*4)
        help_text("After you stick, the dealer will then draw their hand",displayY/20*5)
        help_text("Jack, Queen and King add 10 to your total, and Ace adds either 1 or 11",displayY/20*7)
        help_text("You will be dealt 2 cards at the start",displayY/20*9)
        help_text("If one is an Ace and the other a is card of value 10 you get a 'Blackjack'",displayY/20*10)
        help_text("You then automatically win if the dealer doesn't get a Blackjack",displayY/20*11)
        help_text("If you get 5 cards without going bust you get a 'Five card trick'",displayY/20*13)
        help_text("This is also an auto-win if the dealer has neither of the two wins stated above",displayY/20*14)
        help_text("Pres [Esc] to return to the main menu",displayY/20*17)

        pygame.display.update()
        clock.tick(10)
    menu()

def choose_card_back():

    gameExit = False

    while gameExit == False:
        
        gameDisplay.fill(green)
        big_text("Choose your card back...",white,displayX/10, displayY/6)
        card_back((displayX/20)*2, (displayY/10)*3.5, back_card1, back_card1_click, action="back_card1")
        card_back((displayX/20)*2 + card_backX*1.5, (displayY/10)*3.6, back_card2, back_card2_click, action="back_card2")
        card_back((displayX/20)*2 + card_backX*3, (displayY/10)*3.5, back_card3, back_card3_click, action="back_card3")

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
        
        pygame.display.update()

def menu():

    gameExit = False
    gameDisplay.blit(blackjack_logo, (displayX/8, displayY/2 - logoY/2))

    while gameExit == False:

        gameDisplay.fill(green)
        gameDisplay.blit(blackjack_logo, (displayX/8, displayY/2 - logoY/2))

        button(displayX - (1.2*buttonX), displayY/6,play_button, play_button_click, action="play")
        button(displayX - (1.2*buttonX),(displayY/6)*2.5,help_button, help_button_click, action="help")
        button(displayX - (1.2*buttonX), (displayY/6)*4,quit_button, quit_button_click, action="quit")

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
            
        pygame.display.update()
        clock.tick(20)

def start_deal(bet,score,back_card,back_card_click):

    gameExit = False
    
    urCardY = 50

    urCardY2 = 50
    
    dCardX = 50
    dCardY = 50

    startX = 50
    startY = 50

    while gameExit == False:

        urCardX = 50
        
        gameDisplay.fill(green)
        for x in range(0,10):               
            gameDisplay.blit(back_card, (startX + 20 - (x*2),startY))

        if urCardY >= 400:
            urCardY = 400
        else:
            urCardY += 20


        if urCardY == 400:
            if dCardX >= 500:
                dCardX = 500
            else:
                dCardX += 20

        if dCardX == 500:
            if urCardY2 >= 400:
                urCardY2 = 400
            else:
                urCardY2 += 20

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameExit = True

        gameDisplay.blit(back_card, (urCardX, urCardY))
        gameDisplay.blit(back_card, (dCardX, dCardY))

        if urCardY2 == 400:
            urCardX = 100
            
        gameDisplay.blit(back_card, (urCardX, urCardY2))
                    
        pygame.display.update()
        clock.tick(30)

        if urCardX == 100:
            time.sleep(1)
            gameLoop(bet,score,back_card,back_card_click)
            

def randCard(card,x,y,total):
    value = 0
    if card == "A":
        show_card = pygame.image.load("cardA.jpg")
        value = 1
    elif card == 2:
        show_card = pygame.image.load("card2.jpg")
        value = 2
    elif card == 3:
        show_card = pygame.image.load("card3.jpg")
        value = 3
    elif card == 4:
        show_card = pygame.image.load("card4.jpg")
        value = 4
    elif card == 5:
        show_card = pygame.image.load("card5.jpg")
        value = 5
    elif card == 6:
        show_card = pygame.image.load("card6.jpg")
        value = 6
    elif card == 7:
        show_card = pygame.image.load("card7.jpg")
        value = 7
    elif card == 8:
        show_card = pygame.image.load("card8.jpg")
        value = 8
    elif card == 9:
        show_card = pygame.image.load("card9.jpg")
        value = 9
    elif card == 10:
        show_card = pygame.image.load("card10.jpg")
    elif card == "J":
        show_card = pygame.image.load("cardJ.jpg")
    elif card == "Q":
        show_card = pygame.image.load("cardQ.jpg")
    elif card == "K":
        show_card = pygame.image.load("cardK.jpg")

    if card == 10 or card == "J" or card == "Q" or card == "K":
        value = 10
        
    show_card = pygame.transform.scale(show_card, (cardX, cardY))
    gameDisplay.blit(show_card, (x, y))
    
    total += value
    return (total)
    

def gameLoop(bet,score,back_card,back_card_click):

    gameExit = False

    cards = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    x1 = randint(0,12)
    x2 = randint(0,12)
    x3 = randint(0,12)

    pTotal = 0
    dTotal = 0
    totalX = (displayX/16)*5

    pTotal = randCard(cards[x1],50,400,pTotal)
    pTotal = randCard(cards[x2],100,400,pTotal)
    dTotal = randCard(cards[x3],500,50,dTotal)

    hit_no = 0

    pygame.display.update()
    clock.tick(30)

    while gameExit == False:
        
        big_text("Would you like to hit or stick?",white,displayX/16,(displayY/12)*5)
        gameDisplay.blit(hit_button, (displayX/16,(displayY/12)*6))
        gameDisplay.blit(stick_button, ((displayX/16 + button2X * 1.2),(displayY/12)*6))
        big_text(str(pTotal),white,totalX,(displayY/12)*8)
        
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if displayX/16 + button2X > cursor[0] > displayX/16 and (displayY/12)*6 + button2Y > cursor[1] > (displayY/12)*6:
            gameDisplay.blit(hit_button_click, (displayX/16,(displayY/12)*6))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    hit_no += 1
                    hit(back_card,back_card_click,hit_no)

        if (displayX/16 + button2X * 1.2) + button2X > cursor[0] > (displayX/16 + button2X * 1.2) and (displayY/12)*6 + button2Y > cursor[1] > (displayY/12)*6:
            gameDisplay.blit(stick_button_click, ((displayX/16 + button2X * 1.2),(displayY/12)*6))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    print ("stick")
            
        for event in pygame.event.get():
            pass

        pygame.display.update()
        clock.tick(20)

def hit(back_card,back_card_click,hit_no):

    gameExit = False

    gameDisplay.fill(green, rect=[displayX/16,(displayY/12)*5,(button2X*2.4),(button2Y + displayY/12)])
    
    cards = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    urCardY = displayY/12
    
    while gameExit == False:

        x = randint(0,12)
        gameDisplay.fill(green, rect=[displayX/16,urCardY-(displayY/12),cardX,cardY])
        gameDisplay.blit(back_card, (displayX/16,displayY/12))
        gameDisplay.blit(back_card, (displayX/16,urCardY))

        if urCardY >= 250:
            urCardY = 250
        else:
            urCardY += 20
        
        for event in pygame.event.get():
                pass

        if urCardY == 250:
            
            cursor = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            big_text("Take your card",white,displayX/4,(displayY/12)*5)
            
            if displayX/16 + cardX > cursor[0] > displayX/16 and (displayY/12)*5 + cardY > cursor[1] > (displayY/12) * 5:
                gameDisplay.blit(back_card_click,(displayX/16,(displayY/12)*5))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        pTotal = randCard(cards[x2],,,pTotal)
                        
                
        pygame.display.update()
        clock.tick(30)

menu()
