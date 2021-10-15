import pygame
import time
import random

pygame.init()
width,height=800,600#screen
width1 = 1000
font_style=pygame.font.SysFont(None,30)
disp=pygame.display.set_mode((width1,height))
green,red,black,white=(0,204,153),(255,8,0),(0,0,0),(255,255,255)

def menu():
    disp=pygame.display.set_mode((width1,height))
    disp.fill(black)
    menu_page = pygame.font.SysFont(None,130).render("SNEK",True,green)
    disp.blit(menu_page,[(width1/2)-140,(height/3)-150])

    rules = [
        "Rules:",
        "1.When the snake moving in one direction is made to move in the opposite direction, the game",
        "   ends.",
        "2.When the snake touches the edges of the screen, it will continue moving from the opposite",
        "   side.",
        "3.The blue food will make the snake move very quickly and make it invulnerable to ",
        "everything for 5 seconds.",
        "4.The white food will make the snake move slowly and decrease the score by 3.",
        "5.When the score reaches 10, the snake will enter into a new level which has barricades. If it ",
        "   comes in contact with any of these barricades, the snake will die.",
        "6.Press Q to quit and any other key to continue.",
            ]
    for rule in rules:
        rules_disp = pygame.font.SysFont(None, 30).render(rule,True,white)
        disp.blit(rules_disp,[(width1/4)-200,(height/3)+(30*rules.index(rule))])

    pygame.display.set_caption("SNEK")
    pygame.display.update()

def gameloop():
    disp=pygame.display.set_mode((width,height))
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
    menu()

menu()

while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                quit()
            else:
                gameloop()
                

