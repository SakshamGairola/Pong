import pygame
from paddle import Paddle
from ball import Ballinit
from random import randint



def GameFnc():

    #defing boundries of the play area
    Left_Boundry = [0,0,5,600]
    Bottom_Boundry = [0,595,800,5]
    Right_Boundry = [795,0,5,600]
    Top_Boundry = [0,0,800,5]
    Middle_Line = [400,0,1,600]

    #defining colors used
    white = (255, 255, 255)
    black = (0,0,0)
    red = (255, 0, 0)

    #Window size
    WindowSize = (800, 600)

    #Store sscore of both players
    scoreA = 0 
    scoreB = 0 

    #Area to render on
    gameDisplay = pygame.display.set_mode(WindowSize)
    pygame.display.set_caption('Tennis')

    pygame.display.update()

    clock = pygame.time.Clock()

    #Left Player's paddle
    paddleA = Paddle(black, 5, 30)
    paddleA.rect.x = 15
    paddleA.rect.y = 285
    
    #Right Player's paddle
    paddleB = Paddle(black, 5, 30)
    paddleB.rect.x = 780
    paddleB.rect.y = 285

    #Ball
    Ball = Ballinit(black, 6, 6)
    Ball.rect.x = 397
    Ball.rect.y = 297

    Sprite = pygame.sprite.Group()
    Sprite.add(paddleA)
    Sprite.add(paddleB)
    Sprite.add(Ball)
        
    gameExit = False

    def BallReset():
        Ball.rect.x = 397
        Ball.rect.y = 297
        Ball.velocity[1] =  randint(1, 4)

    def RenderBoundries():
        gameDisplay.fill(white)
        gameDisplay.fill(black, rect = Left_Boundry) #Lelt_Boundry
        gameDisplay.fill(black, rect = Bottom_Boundry) #Bottom_Boundry
        gameDisplay.fill(black, rect = Right_Boundry) #Right_Boundry
        gameDisplay.fill(black, rect = Top_Boundry) #Top_Boundry
        gameDisplay.fill(black, rect = Middle_Line) #Middle_Line

    #game loop
    while not gameExit:
        
        #checks if game is being quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        
        #Checking the (Verticle) Y boundries 
        if Ball.rect.y >= 589 or Ball.rect.y <= 5:
            Ball.velocity[1] = -Ball.velocity[1]
        
        #Input Check
        key_pressed = pygame.key.get_pressed()  

        if key_pressed[pygame.K_w]:
            paddleA.Move(-5)
        elif key_pressed[pygame.K_s]:
            paddleA.Move(5)
        if key_pressed[pygame.K_UP]:
            paddleB.Move(-5)
        elif key_pressed[pygame.K_DOWN]:
            paddleB.Move(5)
    
        #Colloision's Conditions
        condition_one = Ball.rect.x == paddleA.rect.x + 2.5 and Ball.rect.x < paddleA.rect.x + 5
        condition_two = Ball.rect.y >= paddleA.rect.y + 15 and Ball.rect.y < paddleA.rect.y + 30
        
        condition_three = Ball.rect.x >= paddleB.rect.x + 2.5 and Ball.rect.x < paddleB.rect.x + 5
        condition_four = Ball.rect.y >= paddleB.rect.y + 15 and Ball.rect.y < paddleB.rect.y + 30
        
        if Ball.colliderect(paddleA):#condition_one and condition_two:
            Ball.bounce()
        elif Ball.rect.x < 10:
            scoreB += 1
            BallReset()
        if Ball.colliderect(paddleB):#condition_three and condition_four:
            Ball.bounce()
        elif Ball.rect.x > 790:
            scoreA += 1
            BallReset()

        #if Ball.rect.x > 800:
            #scoreA += 1
            #Ball.rect.x = 397
            #Ball.rect.y = 297
        #if Ball.rect.x < 0:
            #scoreB += 1
            #Ball.rect.x = 397
            #Ball.rect.y = 297

        RenderBoundries()

        Sprite.update()

        font = pygame.font.Font(None, 74)
        
        text1 = font.render(str(scoreA), 1, black)
        gameDisplay.blit(text1, (197,10))
        
        text2 = font.render(str(scoreB), 1, black)
        gameDisplay.blit(text2, (597,10))

        
        Sprite.update()

        Ball.Update()

        Sprite.draw(gameDisplay)

        #pass paddles and ball as arguments to update
        pygame.display.update()
        
        #sets framelimit
        clock.tick(60)

    pygame.quit()