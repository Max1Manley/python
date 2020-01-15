#IDEAS
#items/pickups/areas that provide new elemental powers and give advantages over certain enemies
#fairy(pink) > dragon(gold) > light(white) > void(darkgrey) > psychic(purple) > fairy(pink) 
#turn based? time based? real time?
#high ground advantage?
#blasted into space to destroy dark energy monsters that want to pump dark energy into our world to make our universe habitable for them
#radiation meter as a time limit? but i don't really like time/move limits

#turn this into an object somehow to track movement?
#row0 = [0,1,2,3,4,5,6,7,8]
#row1 = [0,1,2,3,4,5,6,7]
#row3 = [0,1,2,3,4,5,6,7,8]
#row4 = [0,1,2,3,4,5,6,7]
#row5 = [0,1,2,3,4,5,6,7,8]
#row6 = [0,1,2,3,4,5,6,7]
#row7 = [0,1,2,3,4,5,6,7,8]
#JS example of what would be useful
#a1 = {
#    element: 'normal',
#    neighbors: [a2, b1]
#}


import pygame
pygame.init()

#some good old global variable for you
turnCount = 0
screenWidth = 1080
screenHeight = 720
fairy = 255, 102, 204
dragon = 204, 153, 0
light = 255, 255, 255
void = 115, 115, 115
psychic = 204, 0, 204

#setting window size and window title
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Super Element Galaxy")

#used to help set image background
bg = pygame.image.load('elementdungeontestcolored.png')
bluechar = pygame.image.load('bluecharacter0.png')
purplechar = pygame.image.load('purplecharacter0.png')

#used to help set framerate
clock = pygame.time.Clock()

#player class
class player:
#character dimentions and velocity
    def __init__(self, x, y, width, height, charElement):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.charElement = charElement
        self.vel = 5
        self.left = False
        self.right = False
#bad buy class
class baddie:
    def __init__(self, x, y, width, height, charElement, movement, attack, hp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.charElement = charElement
        self.vel = 3
        self.left = False
        self.right = False
        self.movement = movement
        self.attack = attack
        self.hp = hp

#setup for text display
font = pygame.font.SysFont(None, 25)

def messageToScreen(msg,color,x,y):
    screen_text = font.render(msg, True, color)
    win.blit(screen_text, [x, y])

#redraws game window so there isn't a million of the same image, order matters
def redrawGameWindow():
    #win.fill((0,0,0))
    #image background
    win.blit(bg, (0, 0))
    #pygame.draw.polygon(win,(100, 200, 200), ((50,100), (75, 75), (125, 75), (150, 100), (150,150), (125, 175), (75, 175), (50, 150)))
    pygame.draw.rect(win, (man.charElement), (man.x, man.y, man.width, man.height))
    pygame.draw.rect(win, (bad.charElement), (bad.x, bad.y, bad.width, bad.height))
    
    win.blit(bluechar, (man.x, man.y))
    win.blit(purplechar, (bad.x, bad.y))
    messageToScreen("[X]" + str(bad.hp), (0,0,0), 50, screenHeight - 100)
    messageToScreen('BlueCharacter Element:' + str(man.charElement), (0,0,0,), 50, screenHeight - 75)
    
    pygame.display.update()

#function for changing player state
def handleElement():
    #changing colors with keys
    if keys[pygame.K_1]:
        man.charElement = fairy
        print('making fairy')
    if keys[pygame.K_2]:
        man.charElement = dragon
        print('making dragon')
    if keys[pygame.K_3]:
        man.charElement = light
        print('making light')
    if keys[pygame.K_4]:
        man.charElement = void
        print('making void')
    if keys[pygame.K_5]:
        man.charElement = psychic
        print('making psychic')
        
    #playing with mouse events
    if mouse[0]:
        print('left click', event)
    if mouse[1]:
        print('middle click', mouse)
    if mouse[2]:
        print('right click', event.pos)

#creating character from class object
man = player(566, 420, 64, 74, light)
bad = baddie(670, 420, 64, 74, void, 3, 5, 15)
#1 spot on x axis = 105px 1 spon on y axis = 75

run = True

#main game loop
while run:
    #frame rate 27/s
    clock.tick(30)
    
    #x and y can get off by a pixel with horizontal movement
    if abs(man.x - bad.x) <= 104 and abs(man.y - bad.y) <= 79:
        print('within striking range')
    else:
        print('outside striking range')
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #listeners for mouse and key presses        
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    
    #movement listeners
    if turnCount == 0:
        if keys[pygame.K_a]: #and man.x > man.vel:
            man.x -= 104
            turnCount += 1
        if keys[pygame.K_d]: #and man.x < screenWidth - man.width - man.vel:
            man.x += 104
            turnCount += 1
        if keys[pygame.K_q]: #and man.y > man.vel:
            man.y -= 79
            man.x -= 52
            turnCount += 1
        if keys[pygame.K_c]: #and man.y < screenHeight - man.height - man.vel:
            man.y += 79
            man.x += 52
            turnCount += 1
        if keys[pygame.K_e]:
            man.y -= 79
            man.x += 52
            turnCount += 1
        if keys[pygame.K_z]:
            man.y += 79
            man.x -= 52
            turnCount += 1
            
        #attack test
        if keys[pygame.K_SPACE]:
            bad.hp -= 3
        
    #player2 / just pigybacking player1 movement at the moment
    if turnCount == 1:
        if keys[pygame.K_f]: #and man.x > man.vel:
            bad.x -= 104
            turnCount = 0
        if keys[pygame.K_h]: #and man.x < screenWidth - man.width - man.vel:
            bad.x += 104
            turnCount = 0
        if keys[pygame.K_r]: #and man.y > man.vel:
            bad.y -= 79
            bad.x -= 52
            turnCount = 0
        if keys[pygame.K_n]: #and man.y < screenHeight - man.height - man.vel:
            bad.y += 79
            bad.x += 52
            turnCount = 0
        if keys[pygame.K_y]:
            bad.y -= 79
            bad.x += 52
            turnCount = 0
        if keys[pygame.K_v]:
            bad.y += 79
            bad.x -= 52
            turnCount = 0
    
    handleElement()
    redrawGameWindow()
    
pygame.quit()