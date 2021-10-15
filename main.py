import pygame
import time
import random

pygame.init()
width,height=800,600#screen
disp=pygame.display.set_mode((width,height))
pygame.display.set_caption("SNEK")
green,red,black,white,blue=(0,204,153),(255,8,0),(0,0,0),(255,255,255),(0,0,255)
font_style=pygame.font.SysFont(None,30)

def gameloop():
    current_time = pygame.time.get_ticks()
    end=0
    x,y,x1,y1=width/2,height/2,0,0#x,y->head pos;x1,y1->change in pos
    cell=20
    snake_speed=10
    body,blen=[],1
    clk=pygame.time.Clock()

    food_x=round(random.randrange(0,width-cell)/cell)*cell
    food_y=round(random.randrange(0,height-cell)/cell)*cell

    food_x_blue=round(random.randrange(0,width-cell)/cell)*cell
    food_y_blue=round(random.randrange(0,height-cell)/cell)*cell

    dis_x=food_x_blue
    dis_y=food_y_blue

    counter=0

    while not end:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=1

            if event.type==pygame.KEYDOWN and len(body)==1:
                if event.key==pygame.K_LEFT:
                    x1,y1=-cell,0
                elif event.key==pygame.K_UP:
                    x1,y1=-0,-cell
                elif event.key==pygame.K_RIGHT:
                    x1,y1=cell,0
                elif event.key==pygame.K_DOWN:
                    x1,y1=0,cell

            if event.type==pygame.KEYDOWN and len(body)>1:
                if event.key==pygame.K_LEFT and (x1 != cell):
                    x1,y1=-cell,0
                elif event.key==pygame.K_UP and (y1 != cell):
                    x1,y1=-0,-cell
                elif event.key==pygame.K_RIGHT and (x1 != -cell):
                    x1,y1=cell,0
                elif event.key==pygame.K_DOWN and (y1 != -cell):
                    x1,y1=0,cell

        x+=x1;y+=y1

        if(x>width):x=0
        if(x<0):x=width
        if(y>height):y=0
        if(y<0):y=height            

        i=random.randint(1,10)

        disp.fill(black)
        pygame.draw.rect(disp,red,[food_x,food_y,cell,cell])
                 
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

        if (blen-1)%4==0:
            pygame.draw.rect(disp,blue,[food_x_blue,food_y_blue,cell,cell])

        if (blen-1)!=0 and (blen-1)%2==0:
            pygame.draw.rect(disp,black,[dis_x,dis_y,cell,cell])
        pygame.display.update()


        if food_x==x and food_y==y:#contact with food
            food_x=round(random.randrange(0,width-cell)/cell)*cell
            food_y=round(random.randrange(0,height-cell)/cell)*cell
            blen+=1#body length increases
            if snake_speed<30: snake_speed+=0.5;
            pygame.draw.rect(disp,blue,[food_x_blue,food_y_blue,cell,cell])
                
        if food_x_blue==x and food_y_blue==y:#contact with food
            food_x_blue=round(random.randrange(0,width-cell)/cell)*cell
            food_y_blue=round(random.randrange(0,height-cell)/cell)*cell
            blen+=1#body length increases
            if snake_speed<30: snake_speed+=4.5;
            for block in body[:blen-1]:
                if block==head:pass;
            pygame.time.set_timer(pygame.USEREVENT, 5000)
            
               
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