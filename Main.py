import pygame
pygame.init()  
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#Player 1 CONSTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
#Player 2 CONSTANTS
A = 0
D = 1
W = 2
S = 3

#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform

#player 2 variables
xpos2 = 100 #xpos of player
ypos2 = 200 #ypos of player
vx2 = 0 #x velocity of player
vy2 = 0 #y velocity of player
keys2 = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround2 = False #this variable stops gravity from pulling you down more when on a platform

while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
    
    #Input Section (Player 2) ------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            elif event.key == pygame.K_UP:
                keys[UP]=True
            if event.key == pygame.K_a:
                keys2[A]=True
            elif event.key == pygame.K_d:
                keys2[D]=True
            elif event.key == pygame.K_w:
                keys2[W]=True
           
                
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False

            elif event.key == pygame.K_UP:
                keys[UP]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False

            if event.key == pygame.K_a:
                keys2[A]=False

            elif event.key == pygame.K_w:
                keys2[W]=False
            elif event.key == pygame.K_d:
                keys2[D]=False     
    #physics section--------------------------------------------------------------------
    #LEFT AND RIGHT MOVEMENT (Player 1)
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
        
    elif keys[RIGHT]==True:
        vx=+3
        direction = RIGHT
    else:
        vx = 0
    #LEFT AND RIGHT MOVEMENT (Player 2)
    if keys2[A]==True:
        vx2=-3
        direction = A
        
    elif keys2[D]==True:
        vx2=+3
        direction = D
    else:
        vx2 = 0


        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
    if keys2[UP] == True and isOnGround2 == True: #only jump when on the ground
        vy2 = -8
        isOnGround2 = False
        
    

    
    #COLLISION
    if xpos>100 and xpos<200 and ypos+40 >750 and ypos+40 <770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    elif xpos>200 and xpos<300 and ypos+40 >650 and ypos+40 <670:
        ypos = 650-40
        isOnGround = True
        vy = 0
    elif xpos>200 and xpos<400 and ypos+40 >550 and ypos+40 <570:
        ypos = 550-40
        isOnGround = True
        vy = 0
    else:
        isOnGround = False


    
    #stop falling if on bottom of game screen (Player 1)
    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760
        
    #stop falling if on bottom of game screen (Player 2)
    if ypos2 > 760:
        isOnGround = True
        vy2 = 0
        ypos2 = 760
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
    if isOnGround2 == False:
        vy2+=.2

    #update player(1) position
    xpos+=vx 
    ypos+=vy
    #update player(2) position
    xpos2+=vx2 
    ypos2+=vy2
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
  
    pygame.draw.rect(screen, (100, 200, 100), (xpos, ypos, 20, 40))
    pygame.draw.rect(screen, (100, 200, 100), (xpos2, ypos2, 20, 40))
    
    #first platform
    pygame.draw.rect(screen, (200, 0, 100), (100, 750, 100, 20))
    
    #second platform
    pygame.draw.rect(screen, (160, 15, 215), (200, 650, 100, 20))
    
    #third platform
    pygame.draw.rect(screen, (65, 35, 195), (300, 550, 100, 20))
    
    #fourth platform
    pygame.draw.rect(screen, (40, 85, 185), (400, 450, 100, 20))
    
    #fifth platform
    pygame.draw.rect(screen, (70, 200, 240), (500, 350, 100, 20))
    

    
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
