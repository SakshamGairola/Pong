import pygame
import Main_Game

#initialising pygame
pygame.init()

#variablr that exits the game
gameExit = False

#font used
font = pygame.font.Font(None, 74)
font1 = pygame.font.Font(None, 24)

#colors used
white = (255, 255, 255)
black = (0,0,0)
light_red = (200, 0, 0)
light_green = (0, 200, 0)
red = (255, 0, 0)
green = (0,255,0)

#size of the window
WindowSize = (800, 600)

#Area to render on
gameDisplay = pygame.display.set_mode(WindowSize)

#updates the whole game scene
pygame.display.update()

#fuction responsible for frames per second
clock = pygame.time.Clock()


#game loop
while not gameExit:
    
    #stores mouse cordinates
    mouse = pygame.mouse.get_pos()  

    #loop to check for gmae quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    
    #get mouse button status
    mouse_pressed = pygame.mouse.get_pressed()
    
    #fiils game background with white color
    gameDisplay.fill(white)

    #checks if mouse is on the button
    if 250 + 100 > mouse[0] > 250 and 350 + 50 > mouse[1] > 350:    
        pygame.draw.rect(gameDisplay, light_green, [250, 350, 100, 50])
    
        #checks for mouse click
        if mouse_pressed[0]: 
            #call game
            Main_Game.GameFnc()
    else:
        pygame.draw.rect(gameDisplay, green, [250, 350, 100, 50])
    
    #checks if mouse is on the button
    if 450 + 100 > mouse[0] > 450 and 350 + 50 > mouse[1] > 350:    
        pygame.draw.rect(gameDisplay, light_red, [450, 350, 100, 50])
        #checks for mouse click
        if mouse_pressed[0]:
            #exits game
            gameExit = True
    else:
        pygame.draw.rect(gameDisplay, red, [450, 350, 100, 50])
    
    
    srt = "Tennis"
    Play = "Play"
    Exit = "Exit"
    
    #fonts that has to be rendered to the game scene
    text = font.render(srt, 1, red)
    gameDisplay.blit(text, (300,250))

    text_Play = text = font1.render(Play, 1, black)
    gameDisplay.blit(text, (285,368))

    text_Exit = text = font1.render(Exit, 1, black)
    gameDisplay.blit(text, (485,368))
    
    #pass paddles and ball as arguments to update
    pygame.display.update()
    
    #sets framelimit
    clock.tick(60)

pygame.quit()