import pygame
from sys import exit
pygame.init()#initializing pygame
screen=pygame.display.set_mode((800,480),pygame.RESIZABLE)#creating a display surface
screen.fill("Green")
pygame.display.set_caption("Flappy run")#name to be displayed on top of window

clock=pygame.time.Clock()#creating the clock object

bg_surface=pygame.Surface((800,300))
bg_surface=pygame.image.load("graphics/sky.png")

red_surface=pygame.Surface((800,500))
red_surface.fill('Red')

ground_surface=pygame.Surface((800,200))
ground_surface=pygame.image.load("graphics/ground.png")

test_font=pygame.font.Font(None,50)
text_surface=test_font.render("Flappy Run",True,"Yellow")
#if the attribute is true we get normal text if false we get text in pixels

snail_surface=pygame.Surface((72,36))
snail_surface=pygame.image.load("graphics/snail1.png")
snail_xcoordinate=800

fox_surface=pygame.Surface((72,36))
fox_surface=pygame.image.load("graphics/fox.png")
fox_xcoordinate=0

while True:
    for event in pygame.event.get():#to all the possible events
        if event.type==pygame.QUIT:# constant irrespective of the type of window
            pygame.quit()#opposite of pygame.init()
            exit()
    screen.blit(bg_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    snail_xcoordinate-=1
    if snail_xcoordinate==0:
        snail_xcoordinate=800
    screen.blit(snail_surface,(snail_xcoordinate,270))

    fox_xcoordinate+=1
    if fox_xcoordinate==800:
        fox_xcoordinate=0
    screen.blit(fox_surface,(fox_xcoordinate,270))

    #BLIT=block image tansfer puting regular on display
               #name of surface,position  200px from left,100px from top      
    pygame.display.update()#for updating the initial display surface
#framerate:how fast the game is going to run
    clock.tick(60)#The while true loop should not run faster than 60 times a sec
    

"""There are 2 types of sufaces in pygame
DISPLAY SURFACE =Actual window that is displayed,the game window(unique)
REGULAR SURFACE=A single img or plain color
It needs to be put on the display surface to be visible(flexible ammount)"""
