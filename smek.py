import pygame,sys

pygame.init()


#screen
screen= pygame.display.set_mode((800,600))

#rules
font=pygame.font.SysFont('MENU',36)
i1=font.render('MENU',True,(0,255,0))

f1=pygame.font.SysFont('Change in the direction of movement ends the game.',28)
i2=font.render('Change in the direction of movement ends the game.',True,(250,0,0))

f2=pygame.font.SysFont('Touching the edge results in movement from opp side.',28)
i3=font.render('Touching the edge results in movement from opp side.',True,(250,0,0))

f3=pygame.font.SysFont('Blue food makes the snake invulnerable and fast for 5 sec.',28)
i4=font.render('Blue food makes the snake invulnerable and fast for 5 sec.',True,(250,0,0))


f4=pygame.font.SysFont('Blue and white foods disappear after consumption of 2 reds.',28)
i5=font.render('Blue and white foods disappear after consumption of 2 reds.',True,(250,0,0))


f5=pygame.font.SysFont('White food results on slower speed and deduction of 3 points',28)
i6=font.render('White food results on slower speed and deduction of 3 points',True,(250,0,0))

f6=pygame.font.SysFont('A score of 10 unlocks a new level',28)
i7=font.render('A score of 10 unlocks a new level',True,(250,0,0))


#name and logo
pygame.display.set_caption("SNEK")
logo=pygame.image.load("snake.png")
pygame.display.set_icon(logo)



#to quit

while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        
            
    #bg
    screen.fill((0,0,150))
    screen.blit(i1,(250,50))
    screen.blit(i2,(0,80))
    screen.blit(i3,(0,100))
    screen.blit(i4,(0,120))
    screen.blit(i5,(0,140))
    screen.blit(i6,(0,160))
    screen.blit(i7,(0,180))
    

    
    pygame.display.update()
    

