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


class player(object):
#character dimentions and velocity
    def __init__(self, x, y, width, height):
        self.x= x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
charColor = 255, 0, 255
white = 255, 255, 255
purple = 255, 0, 255

#this is a function in python
def redrawGameWindow():
    global walkCount
    win.fill((0,0,0))
    #image background
    #win.blit(bg, (-100, -100))
    pygame.draw.rect(win, (charColor), (man.x, man.y, man.width, man.height))
    pygame.draw.circle(win, (255, 0, 255), (190, 190), 50, 5)
    pygame.draw.circle(win, (255, 0, 255), (190, 190), 30, 5)
    pygame.draw.polygon(win,
        (100, 200, 200),
        ((0,0), (130, 0), (130, 130), (75, 200), (55, 75)))
    pygame.draw.polygon(win,
        (100, 200, 200),
        ((150,0), (280, 0), (280, 130), (225, 200), (205, 75)))
    pygame.display.update()

def handleColor():
    global charColor
    if keys[pygame.K_SPACE]:
        if charColor == purple:
            charColor = white
            print('if purple')
            
man = player(250, 250, 20, 30)
run = True
while run:
    #frame rate 27/s
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    #movement listeners
    if keys[pygame.K_a] and man.x > man.vel:
        man.x -= man.vel
    if keys[pygame.K_d] and man.x < screenWidth - man.width - man.vel:
        man.x += man.vel
    if keys[pygame.K_w] and man.y > man.vel:
        man.y -= man.vel
    if keys[pygame.K_s] and man.y < screenHeight - man.height - man.vel:
        man.y += man.vel
    handleColor()
            
    redrawGameWindow()
    

    
pygame.quit()
    