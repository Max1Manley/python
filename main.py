#IDEAS
#hexagonal dungeon layout
#items/pickups/areas that provide new elemental powers and give advantages over certain enemies
#fairy(pink) > dragon(gold) > light(white) > void(black) > psychic(purple) > fairy(pink) 
#turn based? time based? real time?
#high ground advantage

import pygame
pygame.init()

#some good old global variable for you
screenWidth = 1080
screenHeight = 720
fairy = 255, 102, 204
dragon = 204, 153, 0
light = 255, 255, 255
void = 115, 115, 115
psychic = 204, 0, 204

#setting window size and window title
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Element Dungeon")

#used to help set image background
bg = pygame.image.load('elementdungeontest.png')

#used to help set framerate
clock = pygame.time.Clock()

#player class
class player:
#character dimentions and velocity
    def __init__(self, x, y, width, height, charElement):
        self.x= x
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

#redraws game window so there isn't a million of the same image, order matters
def redrawGameWindow():
    win.fill((0,0,0))
    #image background
    win.blit(bg, (0, 0))
    #pygame.draw.polygon(win,(100, 200, 200), ((50,100), (75, 75), (125, 75), (150, 100), (150,150), (125, 175), (75, 175), (50, 150)))
    pygame.draw.rect(win, (man.charElement), (man.x, man.y, man.width, man.height))
    pygame.draw.rect(win, (bad.charElement), (bad.x, bad.y, bad.width, bad.height))
    #example of drawing a circle and a polygon
    #pygame.draw.circle(win, (255, 0, 255), (190, 190), 30, 5)
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
        print('left click', event.pos)
    if mouse[1]:
        print('middle click', mouse)
    if mouse[2]:
        print('right click', event)

#creating character
man = player(500, 500, 20, 30, light)
bad = baddie(300, 300, 30, 20, void, 3, 5, 15)

run = True
#main game loop
while run:
    #frame rate 27/s
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #listeners for mouse and key presses        
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    
    #movement listeners
    if keys[pygame.K_a] and man.x > man.vel:
        man.x -= man.vel
    if keys[pygame.K_d] and man.x < screenWidth - man.width - man.vel:
        man.x += man.vel
    if keys[pygame.K_w] and man.y > man.vel:
        man.y -= man.vel
    if keys[pygame.K_s] and man.y < screenHeight - man.height - man.vel:
        man.y += man.vel
        
    #player2
    if keys[pygame.K_a] and bad.x > bad.vel:
        bad.x -= bad.vel
    if keys[pygame.K_d] and bad.x < screenWidth - bad.width - bad.vel:
        bad.x += bad.vel
    if keys[pygame.K_w] and bad.y > bad.vel:
        bad.y -= bad.vel
    if keys[pygame.K_s] and bad.y < screenHeight - bad.height - bad.vel:
        bad.y += bad.vel
    
    handleElement()
    redrawGameWindow()
    
pygame.quit()