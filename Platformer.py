import pygame
import time
from random import randint

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (5, 255, 51)
pink = (255, 51, 51)

gameDisplay = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
font2 = pygame.font.SysFont(None, 100)

image_one = pygame.image.load("Brokeback.png")
image_one = pygame.transform.scale(image_one, (50,45))

pygame.display.set_caption("Platformer")

pygame.display.update()

def text(msg,colour,text_x,text_y):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [text_x,text_y])

def pause():
    paused = True

    while paused == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        text("Paused",black,300,100)
        text("Pres c to continue or q to quit.",black,200,300)
        pygame.display.update()
        clock.tick(10)
    
def gameLoop():
    
    gameExit = False
    gameOver = False
    
    head_x = 300
    head_y = 300
    head_x_change = 0
    head_y_change = 0
    score = 0

    apple_x = 0
    apple_y = 0

    apple_x = round(randint(400,750)/10.0)*10.0
    if apple_x < 500:
        apple_y = round(randint(200,300)/10.0)*10.0
    else:
        apple_y = randint(100,300)
        
    land = False
    dead = False
    
    while not gameExit:
        
        while gameOver == True:  #when the block falls off
            gameDisplay.fill(white)
            text("Game over, press C to play again or Q to quit", red,200,300)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            #when the user lets go of the arrow key
            if event.type == pygame.KEYUP and event.type != pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    head_x_change = 0

            #when th user presses an arrow key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    head_x_change -= 8
                if event.key == pygame.K_RIGHT:
                    head_x_change += 8
                if event.key == pygame.K_UP and head_y_change == 0:
                    head_y_change -= 16
                elif event.key == pygame.K_ESCAPE:
                    pause()

        #determines whether the box meets the conditions to land on the top platform
        if head_y <= 200 and head_x > 450:
            land = True
        else:
            land = False
            
        #movement
        head_x += head_x_change
        head_y += head_y_change

        #if object hits bottom of platform
        if head_x > 450 and land == False and head_y <= 260 and head_y >= 250:
            head_y = 260
            head_y_change = 0

        #gravity
        if head_y < 300:
            if head_y != 200 or head_x <= 450:
                head_y_change += 1

        #makes block keep still on ground
        if head_y > 300 and head_x > 150 and dead == False:
            head_y_change = 0
            head_y = 300

        #if object lands on platform
        if head_x > 450 and land == True and head_y > 200:
            head_y = 200
            head_y_change = 0

        #if object hits side of platform
        if head_x >= 450 and head_y < 260 and head_y > 200:
            head_x = 450

        #if object falls off
        if head_x <= 150:
            head_y_change += 2
            if head_y > 350:
                dead = True
                
        gameDisplay.fill(white) #background
        gameDisplay.blit(image_one, (head_x,head_y,))
 
        gameDisplay.fill(black, rect=[200,350,600,10]) #bottom platform
        gameDisplay.fill(black, rect=[500,250,300,10]) #top platform

        #apple(top left)
        gameDisplay.fill(green, rect=[25,27,20,8])
        gameDisplay.fill(green, rect=[35,35,10,10])
        gameDisplay.fill(pink, rect=[20,40,40,40])

        #apple
        gameDisplay.fill(green, rect=[apple_x + 5, apple_y - 13, 20, 8])
        gameDisplay.fill(green, rect=[apple_x + 15,apple_y - 5,10,10])
        gameDisplay.fill(pink, rect=[apple_x,apple_y,40,40])
        
        #score
        text(str(score), black,80,50)
        
        #collecting the apple
        if head_x < apple_x +35 and head_x > apple_x -50:
            
            if head_y < apple_y +40 and head_y > apple_y -50:
                score += 1
                
                #respawning the apple
                apple_x = round(randint(200,750)/10.0)*10.0
                if apple_x < 500:
                    apple_y = round(randint(200,300)/10.0)*10.0
                else:
                    apple_y = randint(100,300)

        if head_y > 650:
            gameOver = True

        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
    quit()

gameLoop()
