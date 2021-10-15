import pygame
import time
import random
pygame.init()
width,height=800,600#screen
disp=pygame.display.set_mode((width,height))
pygame.display.set_caption("SNEK")
green,red,black,white,yellow=(0,204,153),(255,8,0),(0,0,0),(255,255,255),(255,255,0)
font_style=pygame.font.SysFont(None,30)
def gameloop2():
    end=0
    x,y,x1,y1=width/2,height/2,0,0#x,y->head pos;x1,y1->change in pos
    cell=20
    snake_speed=10
    body,blen=[],1
    clk=pygame.time.Clock()
    food_x=round(random.randrange(0,width-cell)/cell)*cell
    food_y=round(random.randrange(0,height-cell)/cell)*cell
    bari_x1=round(random.randrange(0,width-cell)/cell)*cell
    bari_y1=round(random.randrange(0,height-cell)/cell)*cell
    bari_x2=round(random.randrange(0,width-cell)/cell)*cell
    bari_y2=round(random.randrange(0,height-cell)/cell)*cell
    bari_x3=round(random.randrange(0,width-cell)/cell)*cell
    bari_y3=round(random.randrange(0,height-cell)/cell)*cell
    bari_x4=round(random.randrange(0,width-cell)/cell)*cell
    bari_y4=round(random.randrange(0,height-cell)/cell)*cell
   
    while not end:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=1
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
        if x>width or x<0 or y>height or y<0:#screen boundary condition
            break
        disp.fill(black)
        pygame.draw.rect(disp,red,[food_x,food_y,cell,cell])
        pygame.draw.rect(disp,yellow,[bari_x1,bari_y1,cell,cell])
        pygame.draw.rect(disp,yellow,[bari_x2,bari_y2,cell,cell])
        pygame.draw.rect(disp,yellow,[bari_x3,bari_y3,cell,cell])
        pygame.draw.rect(disp,yellow,[bari_x4,bari_y4,cell,cell])
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
        if (x==bari_x1 and y==bari_y1) or (x==bari_x2 and y==bari_y2) or (x==bari_x3 and y==bari_y3) or (x==bari_x4 and y==bari_y4):
            end=1
        if food_x==x and food_y==y:#contact with food
            food_x=round(random.randrange(0,width-cell)/cell)*cell
            food_y=round(random.randrange(0,height-cell)/cell)*cell
            blen+=1#body length increases
            if snake_speed<30: snake_speed+=0.5;
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

def gameloop():
    end=0
    x,y,x1,y1=width/2,height/2,0,0#x,y->head pos;x1,y1->change in pos
    cell=20
    snake_speed=10
    body,blen=[],1
    clk=pygame.time.Clock()
    food_x=round(random.randrange(0,width-cell)/cell)*cell
    food_y=round(random.randrange(0,height-cell)/cell)*cell
    while not end:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=1
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
        if x>width or x<0 or y>height or y<0:#screen boundary condition
            break
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
        if blen-1 == 10:
            gameloop2()
        disp.blit(score,[0,0])
        pygame.display.update()
        if food_x==x and food_y==y:#contact with food
            food_x=round(random.randrange(0,width-cell)/cell)*cell
            food_y=round(random.randrange(0,height-cell)/cell)*cell
            blen+=1#body length increases
            if snake_speed<30: snake_speed+=0.5;
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
import pygame
import time
import random
pygame.init()
width,height=800,600#screen
disp=pygame.display.set_mode((width,height))
pygame.display.set_caption("SNEK")
green,red,black,white=(0,204,153),(255,8,0),(0,0,0),(255,255,255)
font_style=pygame.font.SysFont(None,30)
def gameloop():
    end=0
    x,y,x1,y1=width/2,height/2,0,0#x,y->head pos;x1,y1->change in pos
    cell=20
    snake_speed=10
    body,blen=[],1
    clk=pygame.time.Clock()
    food_x=round(random.randrange(0,width-cell)/cell)*cell
    food_y=round(random.randrange(0,height-cell)/cell)*cell
    while not end:
        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                end=1
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if x+x1 > x:
                        x1,y1=cell,0
                    else:
                        x1,y1 = -cell,0
                elif event.key==pygame.K_UP:
                    if y+y1 > y:
                        x1,y1=0,cell
                    else:
                        x1,y1 = 0,-cell
                elif event.key==pygame.K_RIGHT:
                    if x-x1 > x:
                        x1,y1=-cell,0
                    else:
                        x1,y1 = cell,0
                elif event.key==pygame.K_DOWN:
                    if y-y1 > y:
                        x1,y1=0,-cell
                    else:
                        x1,y1 = 0,cell

        x+=x1;y+=y1
        if x>width-cell:#screen boundary condition
            x = 0
        elif x<0:
            x = width
        elif y > height-cell:
            y = 0
        elif y < 0:
            y = height

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
        pygame.display.update()
        if food_x==x and food_y==y:#contact with food
            food_x=round(random.randrange(0,width-cell)/cell)*cell
            food_y=round(random.randrange(0,height-cell)/cell)*cell
            blen+=1#body length increases
            if snake_speed<30: snake_speed+=0.5;
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
