import pygame
import time
import random
pygame.init()
width,height=800,600#screen
disp=pygame.display.set_mode((width,height))
pygame.display.set_caption("SNEK")
green,red,black,white, blue = (0,204,153),(255,8,0),(0,0,0),(255,255,255), (0, 0, 255)
font_style=pygame.font.SysFont(None,30)


def gameloop():
    end=0
    invulnerable = 0
    x,y,x1,y1=width/2,height/2,0,0#x,y->head pos;x1,y1->change in pos
    cell=20
    round1 = 0
    snake_speed=10
    body,blen=[],1
    blue_life = 0
    blue_life2 = 0
    clk=pygame.time.Clock()
    food_x=round(random.randrange(0,width-cell)/cell)*cell
    food_y=round(random.randrange(0,height-cell)/cell)*cell
    blue_x = round(random.randrange(0,width-cell)/cell)*cell
    blue_y = round(random.randrange(0,width-cell)/cell)*cell
    blue_timer = random.randint(4,7)
    timer = True
    round1 = 0

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
            if x > width:
                x = 0
            if x < 0:
                x = width
            if y > height:
                y = 0
            if y < 0:
                y = height

        disp.fill(black)
        pygame.draw.rect(disp,red,[food_x,food_y,cell,cell])
        if blen - blue_life == 3:
            blue_x=round(random.randrange(0,width-cell)/cell)*cell
            blue_y=round(random.randrange(0,height-cell)/cell)*cell
            blue_life = blen

        elif blen - blue_life2 > 4:
            pygame.draw.rect(disp,blue,[blue_x,blue_y,cell,cell])
            round1 += 1
            if round1 >100:
                round = 0
                blue_life2 = blen


        head=[]
        head.append(x);head.append(y)
        body.append(head)#append new head to body
        for block in body[:blen-1]:
            if not(invulnerable > 0):
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

        #blue
        if blue_x == x and blue_y == y:
            blue_x=round(random.randrange(0,width-cell)/cell)*cell
            blue_y=round(random.randrange(0,height-cell)/cell)*cell
            blue_life = blen
            blue_life2 = blen
            invulnerable = 200

        if invulnerable > 0:
            clk.tick(snake_speed+10)#fps
            invulnerable -= 1
        else:
            clk.tick(snake_speed)



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
