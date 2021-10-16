import pygame
import time
import random

from pygame.constants import K_DOWN, K_SPACE, KEYDOWN

#fixed new level
pygame.init()
width,height=800,600#screen
green,red,black,white,blue,yellow,pink=(0,204,153),(255,8,0),(0,0,0),(255,255,255),(0,0,255),(255,255,0),(255,182,193)
font_style=pygame.font.SysFont(None,30)
width_menu = 800

disp=pygame.display.set_mode((width_menu,height))
def menu():
    disp=pygame.display.set_mode((width_menu,height))
    disp.fill(black)
    menu_page = pygame.font.SysFont(None,130).render("SNEK",True,green)
    disp.blit(menu_page,[(width_menu/2)-140,(height/3)-150])

    info = [
            "INFO:",
            'Controls are:',
            '   WASD for moving',
            '   SPACEBAR for SHOOTING',
            ' ',
            'Levels:Every 10 levels increases difficulty with pink death boxes',
            '   BLUE== BUFF(godmode)',
            '  WHITE== DEBUFF(slow+(-3)score)',
            '  PARTY== FREE POINTS!!! ',
            ' ',
            'PRESS ANY BUTTON TO START',
            'PRESS Q TO QUIT',
            'ENJOY!!'

            ]
    for i in info:
        info_disp = pygame.font.SysFont(None, 30).render(i,True,white)
        disp.blit(info_disp,[(width_menu/4)-200,(height/3)+(30*info.index(i))])

    pygame.display.set_caption("SNEK")
    pygame.display.update()


def gameloop():
    disp=pygame.display.set_mode((width,height))
    end=0
    godmode=0    #basically the variable that decides whether or not ure invincible

    snake_direction=0
    #0-top 1-right 2-bottom 3-left
    level=0

    x,y,x1,y1=width/2,height/2,0,0#x,y->head pos;x1,y1->change in pos
    cell=20
    snake_speed=10
    body,blen=[],1
    clk=pygame.time.Clock()

    #ill be staying here to annoy u g
    red_counter=0

    #recursive function which returns a non snake body cell
    def createnewfood(body):
        y=round(random.randrange(0,height-cell)/cell)*cell
        x=round(random.randrange(0,width-cell)/cell)*cell
        if [x,y] not in body:return [x,y]
        else:return createnewfood(body)

    food_x=round(random.randrange(0,width-cell)/cell)*cell
    food_y=round(random.randrange(0,height-cell)/cell)*cell

    power_status,white_status,blue_status=0,0,0
    block_choose=random.choice([0,1,2])
    #block_choose=2
    #uncomment above to test quickly
    if block_choose==0:white_status=1
    elif block_choose==1:blue_status=1
    elif block_choose==2:power_status=1
    else :pass


    food_x_white=round(random.randrange(0,width-cell)/cell)*cell
    food_y_white=round(random.randrange(0,height-cell)/cell)*cell

    food_x_blue=round(random.randrange(0,width-cell)/cell)*cell
    food_y_blue=round(random.randrange(0,height-cell)/cell)*cell

    #adding powerup
    power_x=round(random.randrange(0,width-cell)/cell)*cell
    power_y=round(random.randrange(0,height-cell)/cell)*cell

    static_time=time.time()
    death_blocks_x=[20];
    death_blocks_y=[20];


    bullet_blocks=[];

    levelup=0
    snake_direction=0

    def removebullets(bullet_blocks):
        if bullet_blocks==[]:return bullet_blocks
        else:
            remains=[]
            for i in bullet_blocks:
                if(0<=i[0]<=900 and 0<=i[1]<=600):
                    remains.append(i)
            return remains


    #adding bonus red blocks
    power_blocks=[];
    #adding dynamic colors
    dyna_color=(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

    power_mode=0
    while (not end) or godmode:

        time_passed=int(time.time()-static_time)

        #to test new level change score counter =10
        score_counter=blen-1

        #checks for keyboard inputs....
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=1
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and snake_direction!=1:
                    snake_direction=3
                    x1,y1=-cell,0
                elif event.key==pygame.K_UP and snake_direction!=2:
                    snake_direction=0
                    x1,y1=-0,-cell
                elif event.key==pygame.K_RIGHT and snake_direction!=3:
                    snake_direction=1
                    x1,y1=cell,0
                elif event.key==pygame.K_DOWN and snake_direction!=0:
                    snake_direction=2
                    x1,y1=0,cell
                elif event.key==pygame.K_SPACE:
                    bullet_blocks.append([x,y,snake_direction])
                    if snake_direction==0:bullet_blocks.append([x,y+5,snake_direction])
                    if snake_direction==1:bullet_blocks.append([x+5,y,snake_direction])
                    if snake_direction==2:bullet_blocks.append([x,y-5,snake_direction])
                    if snake_direction==3:bullet_blocks.append([x-5,y,snake_direction])


        x+=x1;y+=y1


        #fixes snake invisible issue
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

        #displays white box only if white status is 1
        if white_status:
             pygame.draw.rect(disp,white,[food_x_white,food_y_white,cell,cell])

        #displays blue box only if blue status is 1
        if blue_status:
            pygame.draw.rect(disp,blue,[food_x_blue,food_y_blue,cell,cell])

        #displays power only if power status is 1
        if  power_status:
            pygame.draw.rect(disp,dyna_color,[power_x,power_y,cell,cell])

        dyna_color=(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))




        #pink deathboxes cuz they are posion to snakes
        for i in range(len(death_blocks_y)):
            pygame.draw.rect(disp,pink,[death_blocks_x[i],death_blocks_y[i],cell,cell])

        #displays bullets
        for i in bullet_blocks:
            pygame.draw.rect(disp,yellow,[i[0],i[1],cell,cell])

        #displays extra food
        for i in power_blocks:
            pygame.draw.rect(disp,dyna_color,[i[0],i[1],cell,cell])

        #snake logic
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
        score=font_style.render("Score: "+str(score_counter),True,white)
        disp.blit(score,[0,0])
        pygame.display.update()

        if food_x==x and food_y==y:#contact with food red
            food_x,food_y=createnewfood(body)
            blen+=1#body length increases
            red_counter+=1

            if red_counter%2==0:
                white_status=0
                blue_status=0
                power_status=0 #white food dissapears when 2

            if red_counter%5==0:
                #randomizes next block to spawn
                power_status,white_status,blue_status=0,0,0
                block_choose=random.choice([0,1,2])

                #block_choose=2 uncomment this to check
                if block_choose==0:white_status=1
                elif block_choose==1:blue_status=1
                elif block_choose==2:power_status=1
                else :pass

                food_x_white,food_y_white=createnewfood(body)
                food_x_blue,food_y_blue=createnewfood(body)
                power_x,power_y=createnewfood(body)
            if snake_speed<30: snake_speed+=0.5;

            if (score_counter+1)%10==0 and score_counter!=0:
                levelup=1



        elif food_x_white==x and food_y_white==y and white_status:
            #contact with food white
            white_status=0
            if blen>=4:blen-=3
            elif score_counter<3:
                print("check")
                blen=1#reduces score by 3
            if snake_speed>30: snake_speed-=0.5;#slows the snake down

        elif food_x_blue==x and food_y_blue==y and blue_status:
            #contact with food blue
            blue_status=0
            static_time=time.time()

            #sets godmode to 1 invincible
            godmode=1
            if snake_speed<30: snake_speed+=1;#speeds up the snake

        elif power_x==x and power_y==y and power_status:
            power_status=0
            power_mode=1
            snake_speed=10
            static_time=time.time()
            for i in range(20):
                rx,ry=createnewfood(body)
                power_blocks.append([rx,ry])

        elif [x,y] in power_blocks:
                blen+=1
                red_counter+=1
                power_blocks.remove([x,y])

        if power_mode==0:power_blocks=[]

        for i in range(len(death_blocks_y)):
            if(death_blocks_x[i]==x and death_blocks_y[i]==y):end=1

        #waits for 5 secs turns godmode off
        if time_passed==5:
            power_mode=0
            godmode=0

        #fixes godmode
        if godmode:end=0
        #each 10 points level increases and 4 death blocks each level are added
        if(score_counter%10==0 and score_counter!=0 and levelup):
            level+=1
            levelup=0
            for i in range(level*4):
                #even death boxes have better spawns now
                dbx,dby=createnewfood(body)
                death_blocks_x.append(dbx)
                death_blocks_y.append(dby)


        #bullet collision
        for i in bullet_blocks:
            count=0
            while count<len(death_blocks_x):

                #defining hitboxes to fix issue
                if(death_blocks_x[count]-5<=i[0]<=death_blocks_y[count]+5+cell and death_blocks_x[count]-5<=i[1]<=death_blocks_y[count]+5+cell):
                    death_blocks_x.pop(count)
                    death_blocks_y.pop(count)
                    break
                count+=1



        #moves bullets
        for i in bullet_blocks:
            if i[2]==0:
                i[1]-=3*snake_speed
            elif i[2]==1:
                i[0]+=3*snake_speed
            elif i[2]==2:
                i[1]+=3*snake_speed
            elif i[2]==3:
                i[0]-=3*snake_speed

        bullet_blocks=removebullets(bullet_blocks)

        clk.tick(snake_speed)#fps


    clk.tick(snake_speed)

    disp.fill(black)
    m=font_style.render("Game Over",True,red)
    disp.blit(m,[(width/2)-40,height/2])
    f_score=font_style.render("Score: "+str(score_counter),True,white)
    disp.blit(f_score,[(width/2)-30,(height/2)+27])
    pygame.display.update()
    time.sleep(2)
    menu()
menu()

while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q :
                quit()
            else:
                gameloop()
