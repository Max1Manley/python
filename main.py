import pygame
pygame.init()

screenWidth = 640
screenHeight = 480

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Super Python World")

#used to help set image background
#bg = pygame.image.load('bg.jpg')

#used to help set framerate
clock = pygame.time.Clock()

#character dimentions and velocity
x= 250
y = 250
width = 20
height = 30
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
charColor = 255, 0, 255
white = 255, 255, 255
purple = 255, 0, 255

#this is a function in python
def redrawGameWindow():
    global walkCount
    win.fill((0,0,0))
    #image background
    #win.blit(bg, (-100, -100))
    pygame.draw.rect(win, (charColor), (x, y, width, height))
    pygame.draw.circle(win, (255, 0, 255), (190, 190), 50, 5)
    pygame.draw.circle(win, (255, 0, 255), (190, 190), 30, 5)
    pygame.draw.polygon(win, (100, 200, 200), ((0,0), (130, 0), (130, 130), (75, 200), (55, 75)))
    pygame.display.update()

def handleColor():
    global charColor
    if keys[pygame.K_SPACE]:
        if charColor == purple:
            charColor = white
            print('if purple')

run = True
while run:
    #frame rate 27/s
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    #movement listeners
    if keys[pygame.K_a] and x > vel:
        x -= vel
    if keys[pygame.K_d] and x < screenWidth - width - vel:
        x += vel
    if keys[pygame.K_w] and y > vel:
        y -= vel
    if keys[pygame.K_s] and y < screenHeight - height - vel:
        y += vel
    handleColor()
            
    redrawGameWindow()
    

    
pygame.quit()
    