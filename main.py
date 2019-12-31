import pygame
pygame.init()

screenWidth = 640
screenHeight = 480

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Super Python World")

#character dimentions and velocity
x= 250
y = 250
width = 20
height = 30
vel = 5

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screenHeight - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
        
    win.fill((0,0,0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    #pygame.draw.circle(win, (255, 0, 255), (50, 50), 30)
    pygame.display.update()
            
pygame.quit()
    