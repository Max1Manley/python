import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Super Python World")

x= 250
y = 250
width = 20
height = 30
vel = 5

run = True
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
        
    win.fill((0,0,0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.draw.circle(win, (255, 0, 255), (50, 50), 30)
    pygame.display.update()
            
pygame.quit()
    