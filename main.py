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
    end=0
    speed = 0
    key = 0
    time_counter = 0
    fdc = 0
    x,y,x1,y1=width/2,height/2,0,0#x,y->head pos;x1,y1->change in pos
    cell=20
    snake_speed=10
    body,blen=[],1
    clk=pygame.time.Clock()
    food_x=round(random.randrange(0,width-cell)/cell)*cell
    food_y=round(random.randrange(0,height-cell)/cell)*cell
    food_bx=round(random.randrange(0,width-cell)/cell)*cell
    food_by=round(random.randrange(0,height-cell)/cell)*cell
    point = random.randrange(0,3)
    while not end:
        head=[]
        head.append(x);head.append(y)
        body.append(head)#append new head to body
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=1
            if blen>1:
                ch = body[1]
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT and head[0] - ch[0]<=0:
                        x1,y1=-cell,0
                    elif event.key==pygame.K_UP and head[1] - ch[1]<=0:
                        x1,y1=-0,-cell
                    elif event.key==pygame.K_RIGHT and head[0] - ch[0]>=0:
                        x1,y1=cell,0
                    elif event.key==pygame.K_DOWN and head[1] - ch[1]>=0:
                        x1,y1=0,cell
            else:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x1,y1=-cell,0
                    elif event.key==pygame.K_UP:
                        x1,y1=-0,-cell
                    elif event.key==pygame.K_RIGHT:
                        x1,y1=cell,0
                    elif event.key==pygame.K_DOWN:
                        x1,y1=0,cell
        x+=x1;y+=y1
        if x>width: #screen boundary condition
            x=20
        if x<0:
            x=width -20
        if y>height:
            y=20
        if y<0:
            y= height-20
        disp.fill(black)
        pygame.draw.rect(disp,red,[food_x,food_y,cell,cell])
        
        for block in body[:blen-1]:
            if block==head:#snake head touches body
                end=1
        if len(body)>blen:#snake movement display
            del body[0]
        for block in body:
            pygame.draw.rect(disp,green,[block[0],block[1],cell,cell])
        score=font_style.render("Score: "+str(blen-1),True,white)
        disp.blit(score,[0,0])

        if key == 1 :
            pygame.draw.rect(disp,blue,[food_bx,food_by,cell,cell])
            if fdc >= 3:
                point = random.randrange(0,3)
                key = 0

        if food_bx == x and food_by == y:
            food_bx=round(random.randrange(0,width-cell)/cell)*cell
            food_by=round(random.randrange(0,height-cell)/cell)*cell
            point = random.randrange(0,4)
            key = 0
            speed = 1

        if speed == 1 and key == 0:
            if time_counter == 0:
                curr_time = time.time()
                tempsnk = snake_speed
                snake_speed += 5
                time_counter = 1
            if time_counter == 1:
                if time.time() - curr_time >= 5:
                    snake_speed = tempsnk
                    time_counter = 0
                    speed = 0

        if key == 0:
            fdc = 0


        if food_x==x and food_y==y:#contact with food
            food_x=round(random.randrange(0,width-cell)/cell)*cell
            food_y=round(random.randrange(0,height-cell)/cell)*cell
            blen+=1#body length increases
            if (blen-1)%5 == point:
                key = 1
            if key == 1:
                fdc += 1
            if snake_speed<30: snake_speed+=0.5;

        clk.tick(snake_speed)#fps
        pygame.display.update()
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
