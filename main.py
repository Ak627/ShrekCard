
#pygame hearts
#gets you started to draw a valentine's day card

import pygame #gaming module (aka library) 
import random
pygame.init() #initializes Pygame
pygame.display.set_caption("Valentine's day card") #sets the window title
screen = pygame.display.set_mode((800, 800)) #creates game screen
font = pygame.font.Font('freesansbold.ttf', 32) #load font
img = pygame.image.load("dog.jpg") #make sure this is saved to the same folder as your code
img.set_colorkey((255,255,255))
shrk = pygame.image.load("Shrek.jpg")
shrk.set_colorkey((255,255,255))
class heart:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.vy = 1
    def draw(self):
        color1 = random.randrange(0, 250)
        color2 = random.randrange(0, 250)
        color3 = random.randrange(0, 250)
        pygame.draw.circle(screen, (color1,0,color3), (self.xpos, self.ypos), 20) #top left circle
        pygame.draw.circle(screen, (color1,0,color3), (self.xpos+40, self.ypos), 20) #top right circle
        pygame.draw.polygon(screen, (color1,0,color3), ((self.xpos-20, self.ypos+5),(self.xpos+59, self.ypos+5), (self.xpos+20, self.ypos+50)))
    def move(self):
        if self.ypos < 800:
            self.vy = .8
            self.ypos += self.vy

        elif self.ypos >= 800:
            self.xpos = random.randrange(10, 790)
            self.ypos = 0
            self.vy = 0
bob = heart(200, 300)
steve = heart(300, 400)
heartrain = []
for i in range(70):
    heartrain.append(heart(random.randrange(10, 790), random.randrange(10, 790)))
while True:
    screen.fill((0,0,0))
    #text
    text1 = font.render('I Love You!', True, (250, 100, 100)) #numbers give color
    text2 = font.render('Happy Valentines Day', True, (250, 0, 0), (200,150,150)) #this one includes background color
    text3 = font.render('Im head ogre', True, (250,0,0))
    text4 = font.render('heels for you', True, (250,0,0))
    
    bob.draw()
    steve.draw()
    bob.move()
    steve.move()
    
    for i in range(len(heartrain)):
        heartrain[i].draw()
    for i in range(len(heartrain)):
        heartrain[i].move()
    screen.blit(text1, (100, 100)) #numbers give position
    screen.blit(text2, (400, 300))
    screen.blit(text3, (570, 80))
    screen.blit(text4, (570, 110))
    #image
    screen.blit(img, (0, 400))#draw pic
    screen.blit(shrk, (350, 10))
    pygame.display.flip() #this flips all those shapes onto the game screen (needed for every game)
pygame.quit()


