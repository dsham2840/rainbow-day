# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that involves a sunny rainbow day -- and gets Lit. 


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Lit Rainbow"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Configuration
unlit = True


# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
BLUE_BOW = (0, 0, 255)
YELLOW = (255, 255, 175)
YELLOW_BOW = (255, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 135, 0)
PURPLE = (255, 0 , 255)
BLACK = (0, 0, 0)

#Templates for Drawing Birds and Clouds
def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

def draw_bird(x, y):
    pygame.draw.ellipse(screen, BLACK, [x, y, 40, 20])
    pygame.draw.ellipse(screen, BLACK, [x+5, y -10, 15, 15])
    pygame.draw.ellipse(screen, BLACK, [x-1, y-5, 15, 5])
    pygame.draw.ellipse(screen, BLACK, [x+15, y+5, 11, 20])

def draw_flower(x, y):
    pygame.draw.rect(screen, DARKGREEN, [x + 5, y + 5, 4, 20])
    pygame.draw.circle(screen, RED, [x +7, y + 5], 10)
    pygame.draw.circle(screen, YELLOW, [ x + 7, y + 5], 5)

def draw_sun(x,y):
    pygame.draw.circle(screen, YELLOW, [x, y], 50)

sun = [draw_sun]

sun = []
for i in range(1):
    x = random.randrange(50, 750)
    y = random.randrange(50, 350)
    sun.append([x,y])




''' make clouds '''
clouds = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0,200)
    clouds.append([x, y])


'''make birds''' 

birds = []
for g in range(5):
    a = random.randrange(-100, 1600)
    b = random.randrange(0, 200)
    birds.append([a,b])

''' make flowers '''
flowers = []
for f in range(7):
    m = random.randrange(0, 790)
    n = random.randrange(400, 600)
    flowers.append([m,n])


    
# Game loop
done = False

up = False
down = False
left = False
right = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                unlit = not unlit

    state = pygame.key.get_pressed()
    up = state[pygame.K_UP]
    down = state[pygame.K_DOWN]
    left = state[pygame.K_LEFT]
    right = state[pygame.K_RIGHT]
    

    # Game logic

    '''creating different colors'''

    if unlit == False :
        GREEN = (255, 85, 255)
        WHITE = (0, 0, 0)
        BLUE = (180, 55, 0)
        BLUE_BOW = (255, 255, 0)
        YELLOW = (0, 0, 80)
        YELLOW_BOW = (0, 0, 255)
        RED = (0, 255, 255)
        ORANGE = (0, 120, 255)
        PURPLE = (0, 255 , 0)
        BLACK = (255, 255, 255)
        DARKGREEN = (170, 0, 170)
    elif unlit == True:
        GREEN = (0, 175, 0)
        WHITE = (255, 255, 255)
        BLUE = (75, 200, 255)
        BLUE_BOW = (0, 0, 255)
        YELLOW = (255, 255, 175)
        YELLOW_BOW = (255, 255, 0)
        RED = (255, 0, 0)
        ORANGE = (255, 135, 0)
        PURPLE = (255, 0 , 255)
        BLACK = (0, 0, 0)
        DARKGREEN = (85, 255, 85)

    ''' move clouds and birds '''        

    for c in clouds:
        c[0] -= 1

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 200)

    for b in birds:
        b[0] -= 3

        if b[0] < -100:
            b[0] = random.randrange(800, 1600)
            b[1] = random.randrange(0, 200)
  
    # Drawing code
    ''' sky '''
    screen.fill(BLUE)

    ''' sun '''
    for p in sun:
        draw_sun(p[0],p[1])

    ''' rainbow '''
    pygame.draw.ellipse(screen, ORANGE, [-50, 200, 800, 1000], 10)
    pygame.draw.ellipse(screen, RED, [-15, 190, 730, 800], 10)
    pygame.draw.ellipse(screen, YELLOW_BOW, [-7, 210, 715, 790], 10)
    pygame.draw.ellipse(screen, GREEN, [-10, 220, 720, 810], 10)
    pygame.draw.ellipse(screen, BLUE_BOW, [-10, 230, 715, 815], 10)
    pygame.draw.ellipse(screen, PURPLE, [-7, 240, 710, 810], 10)

    ''' clouds '''
    for c in clouds:
        draw_cloud(c[0], c[1])

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    ''' grass2 '''
    y = 450
    for x in range(5, 800, 250):
        pygame.draw.polygon(screen, DARKGREEN, [ [x, y], [x + 2, y], [x, y + 10], [x+2, y+10] ])
        pygame.draw.polygon(screen, DARKGREEN, [ [x+4, y], [x + 6, y], [x, y + 10], [x+6, y+10] ])
        pygame.draw.polygon(screen, DARKGREEN, [ [x+8, y], [x + 10, y], [x, y + 10], [x+10, y+10] ])
    y = 500
    for x in range(50, 800, 142):
        pygame.draw.polygon(screen, DARKGREEN, [ [x, y], [x + 2, y], [x, y + 10], [x+2, y+10] ])
        pygame.draw.polygon(screen, DARKGREEN, [ [x+4, y], [x + 6, y], [x, y + 10], [x+6, y+10] ])
        pygame.draw.polygon(screen, DARKGREEN, [ [x+8, y], [x + 10, y], [x, y + 10], [x+10, y+10] ])
    y = 530
    for x in range(-100, 800, 175):
        pygame.draw.polygon(screen, DARKGREEN, [ [x, y], [x + 2, y], [x, y + 10], [x+2, y+10] ])
        pygame.draw.polygon(screen, DARKGREEN, [ [x+4, y], [x + 6, y], [x, y + 10], [x+6, y+10] ])
        pygame.draw.polygon(screen, DARKGREEN, [ [x+8, y], [x + 10, y], [x, y + 10], [x+10, y+10] ])
        
    ''' birds '''
    for b in birds:
        draw_bird(b[0], b[1])

    ''' flowers '''
    for f in flowers:
        draw_flower(f[0], f[1])

    #Move Sun
    if up == True:
        for x in sun:
            x[1] -= 3
    elif down == True:
        for x in sun:
            x[1] += 3
    elif left == True:
        for x in sun:
            x[0] -= 3
    elif right == True:
        for x in sun:
            x[0] += 3

    
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)



# Close window on quit
pygame.quit()
