import pygame
import time
import random
pygame.init()
width,height=800,600#screen
disp=pygame.display.set_mode((width,height))
pygame.display.set_caption("SNEK")
green,red,black,white,grey=(0,204,153),(255,8,0),(0,0,0),(255,255,255), (128, 128, 128)
font_style=pygame.font.SysFont(None,30)
def gameloop():
    end=0
    x,y,x1,y1=width/2,height/2,0,0#x,y->head pos;x1,y1->change in pos
    cell=20
    snake_speed=10
    body,blen=[],1
    clk=pygame.time.Clock()
    dir = "direction"

    food_x=round(random.randrange(0,width-cell)/cell)*cell
    food_y=round(random.randrange(0,height-cell)/cell)*cell

    brick_x = []
    for i in range(0,5):
        brick_x.append(round(random.randrange(0,width-cell)/cell)*cell)
    brick_y = []
    for i in range(0,5):
        brick_y.append(round(random.randrange(0,width-cell)/cell)*cell)



    while not end:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=1
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and dir not in ["right"]:
                    x1,y1=-cell,0
                    dir = "left"
                elif event.key==pygame.K_UP and dir not in ["down"]:
                    x1,y1=-0,-cell
                    dir = "up"
                elif event.key==pygame.K_RIGHT and dir not in ["left"]:
                    x1,y1=cell,0
                    dir = "right"
                elif event.key==pygame.K_DOWN and dir not in ["up"]:
                    x1,y1=0,cell
                    dir = "down"


        x+=x1;y+=y1
        if x>width-cell or x<0 or y>height-cell or y<0:#screen boundary condition
            if x>width-cell:
                x=0
            elif x<0:
                x = width
            elif y> height-cell:
                y = 0
            elif y<0:
                y = height

        disp.fill(black)
        pygame.draw.rect(disp,red,[food_x,food_y,cell,cell])

        if blen > 10:
            for i in range(0,5):
                pygame.draw.rect(disp,grey,[brick_x[i],brick_y[i],cell,cell])

        head=[]
        head.append(x);head.append(y)
        body.append(head)#append new head to body
        for block in body[:blen-1]:
            if block==head:#snake head touches body
                end=1
        if len(body)>blen:#snake movement display
            del body[0]
        for block in body:
            pygame.draw.rect(disp,green,[block[0],block[1],cell,cell])
        score=font_style.render("Score: "+str(blen-1),True,white)
        disp.blit(score,[0,0])
        pygame.display.update()


        if food_x==x and food_y==y:#contact with food
            food_x=round(random.randrange(0,width-cell)/cell)*cell
            food_y=round(random.randrange(0,height-cell)/cell)*cell
            blen+=1#body length increases
            if snake_speed<30: snake_speed+=0.5;

        if blen>10:
            for i in range(0,5):
                if brick_x[i]==x and brick_y[i]==y:
                    end = 1


        clk.tick(snake_speed)#fps
    clk.tick(snake_speed)
    disp.fill(black)
    m=font_style.render("Game Over",True,red)
    disp.blit(m,[(width/2)-40,height/2])
    f_score=font_style.render("Score: "+str(blen-1),True,white)
    disp.blit(f_score,[(width/2)-30,(height/2)+27])
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()
gameloop()
