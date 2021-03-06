import pygame
import random
from sys import exit
pygame.init()#initializing pygame
screen=pygame.display.set_mode((800,480))#creating a display surface
screen.fill("Green")
pygame.display.set_caption("Flappy run")#name to be displayed on top of window

clock=pygame.time.Clock()#creating the clock object

bg_surface=pygame.Surface((800,300))
bg_surface=pygame.image.load("graphics/sky.png")

red_surface=pygame.Surface((800,500))
red_surface.fill('Red')

ground_surface=pygame.Surface((800,200))
ground_surface=pygame.image.load("graphics/ground.png")

rosemary_surface=pygame.Surface((90,36))
rosemary_surface=pygame.image.load("graphics/rosemary.png")

test_font=pygame.font.Font(None,50)
text_surface=test_font.render("Flappy Run",True,"Yellow")
text_rect=text_surface.get_rect(center=(395,65))

pygame.draw.rect(bg_surface,'#c0e8ec',text_rect,10)
pygame.draw.rect(bg_surface,'#c0e8ec',text_rect)
#if the attribute is true we get normal text if false we get text in pixels

#snail_surface=pygame.Surface((72,36))
snail_surface=pygame.image.load("graphics/snail1.png")
snail_rect=snail_surface.get_rect(midbottom=(800,300))
#snail_xcoordinate=800

#fox_surface=pygame.Surface((72,36))
fox_surface=pygame.image.load("graphics/lemon.png")
fox_rect=fox_surface.get_rect(midbottom=(0,300))
fox_xcoordinate=0

player_surface=pygame.image.load("graphics/player_stand.png")
player_rect=player_surface.get_rect(midbottom =(10,300))
player_gravity=0
while True:

    for event in pygame.event.get():#to all the possible events
        if event.type==pygame.QUIT:# constant irrespective of the type of window
            pygame.quit()#opposite of pygame.init()
            exit()

        if event.type==pygame.KEYDOWN and snail_rect.colliderect(player_rect)==False: #Checks if any key is pressed, if the snail and the player already collided
            if event.key==pygame.K_UP and player_rect.bottom>=100:
                player_gravity= -15
                
            if event.key==pygame.K_SPACE and player_rect.bottom>=100: #If we press the up arrow  or space player jumps
                player_gravity= -20
                
            if event.key==pygame.K_DOWN:
                player_gravity= 10

            if event.key==pygame.K_RIGHT:
                player_rect.left+=3
                
    screen.blit(bg_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    screen.blit(rosemary_surface,(0,280))
    screen.blit(rosemary_surface,(750,280))

    player_rect.left+=2
    player_gravity+=1
    player_rect.y += player_gravity

    if player_rect.left<40:
         player_rect.bottom= -20
    
    if player_rect.right>=800:
        player_rect.left=0
        player_rect.bottom= -20

    if player_rect.bottom >=300:
        player_rect.bottom=300
        
    screen.blit(player_surface,player_rect)
    
    snail_rect.left-=1
    if snail_rect.left==0:
        snail_rect.right=800
        #snail_rect.left-=1
    screen.blit(snail_surface,snail_rect)

    fox_rect.left+=1
    if fox_rect.right>=800:
        fox_rect.left=0
        #fox_rect.left+=1
    screen.blit(fox_surface,fox_rect)

    if snail_rect.colliderect(player_rect):   #check for collision between the snail,player
        player_rect.left+= -2
        snail_rect.left+=1
        fox_rect.left+= -1
        text_surface=test_font.render("Game over",True,"Yellow")

    if fox_rect.colliderect(player_rect):
        fox_rect.left= random.randint(0,800)
            
    pygame.display.update()#for updating the initial display surface
#framerate:how fast the game is going to run
    clock.tick(60)#The while true loop should not run faster than 60 times a sec
    
