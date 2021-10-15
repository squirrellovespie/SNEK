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
    godmode=0    #basically the variable that decides whether or not ure invincible

    level=0
    
    x,y,x1,y1=width/2,height/2,0,0#x,y->head pos;x1,y1->change in pos
    cell=20
    snake_speed=10
    body,blen=[],1
    clk=pygame.time.Clock()

    #ill be staying here to annoy u g
    red_counter=0

    food_x=round(random.randrange(0,width-cell)/cell)*cell
    food_y=round(random.randrange(0,height-cell)/cell)*cell

    white_status,blue_status=0,0
    block_choose=random.choice([0,1])
    if block_choose:white_status=1
    else:blue_status=1
    food_x_white=round(random.randrange(0,width-cell)/cell)*cell
    food_y_white=round(random.randrange(0,height-cell)/cell)*cell
    


    food_x_blue=round(random.randrange(0,width-cell)/cell)*cell
    food_y_blue=round(random.randrange(0,height-cell)/cell)*cell
    

    static_time=time.time()
    death_blocks_x=[];
    death_blocks_y=[];

    levelup=0
    while (not end) or godmode:

        time_passed=int(time.time()-static_time)
        
        #to test new level change score counter =10
        score_counter=10 

        #checks for keyboard inputs....
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
            end=1

        disp.fill(black)
        pygame.draw.rect(disp,red,[food_x,food_y,cell,cell])

        #displays white box only if white status is 1
        if white_status:
             pygame.draw.rect(disp,white,[food_x_white,food_y_white,cell,cell])

        #displays blue box only if blue status is 1
        if blue_status:                        
            pygame.draw.rect(disp,blue,[food_x_blue,food_y_blue,cell,cell])
        
        #green deathboxes cuz they are posion to snakes
        for i in range(len(death_blocks_y)):
            pygame.draw.rect(disp,green,[death_blocks_x[i],death_blocks_y[i],cell,cell])


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
            food_x=round(random.randrange(0,width-cell)/cell)*cell
            food_y=round(random.randrange(0,height-cell)/cell)*cell
            blen+=1#body length increases
            red_counter+=1

            if red_counter%2==0:
                white_status=0
                blue_status=0 #white food dissapears when 2

            if red_counter%5==0:
                white_status=1
                blue_status=1
                food_x_white=round(random.randrange(0,width-cell)/cell)*cell
                food_y_white=round(random.randrange(0,height-cell)/cell)*cell
                food_x_blue=round(random.randrange(0,width-cell)/cell)*cell
                food_y_blue=round(random.randrange(0,height-cell)/cell)*cell
            if snake_speed<30: snake_speed+=0.5;

            if score_counter%10==0 and score_counter!=0:
                levelup=1
            
        

        elif food_x_white==x and food_y_white==y:
            #contact with food whit
            white_status=0
            if score_counter>=3:score_counter-=3#reduces score by 3
            if snake_speed<30: snake_speed-=0.5;#slows the snake down
        
        elif food_x_blue==x and food_y_blue==y:
            #contact with food blue
            blue_status=0
            static_time=time.time()
            
            #sets godmode to 1 invincible
            godmode=1
            if snake_speed<30: snake_speed+=1;#speeds up the snake 

        for i in range(len(death_blocks_y)):
            if(death_blocks_x[i]==x and death_blocks_y[i]==y):end=1

        #waits for 5 secs turns godmode off
        if time_passed==5:
            godmode=0

        #each 10 points level increases and 4 death blocks each level are added
        if(score_counter%10==0 and score_counter!=0 and levelup):
            level+=1
            levelup=0
            death_blocks_x=[round(random.randrange(0,width-cell)/cell)*cell for i in range(level*4)];
            death_blocks_y=[round(random.randrange(0,height-cell)/cell)*cell for i in range(level*4)];

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