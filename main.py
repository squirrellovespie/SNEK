import pygame
import time
import random
import tkinter as tk


pygame.init()
pygame.mixer.init()
EAT_SOUND = pygame.mixer.Sound('./add.mp3')
END_SOUND = pygame.mixer.Sound('./end.mp3')
width,height=800,600#screen
c = True

green,red,black,white,grey, brown=(0,204,153),(255,8,0),(0,0,0),(255,255,255), (128, 128, 128), (165, 42, 42)


font_style=pygame.font.SysFont(None,30)
cell=20
bullet = False

def exit():
    pygame.quit()
    quit()
    c = False
brick_x = []
for i in range(0,5):
    brick_x.append(round(random.randrange(0,width-cell)/cell)*cell)
brick_y = []
for i in range(0,5):
    brick_y.append(round(random.randrange(0,height-cell)/cell)*cell)


def get_food_position(width, height, body):
    while True:
        food_x=round(random.randrange(0,width-cell)/cell)*cell
        food_y=round(random.randrange(0,height-cell)/cell)*cell

        if [food_x, food_y] not in body:
            return food_x, food_y







def gameloop():
    bullet = False
    disp=pygame.display.set_mode((width,height))
    pygame.display.set_caption("SNEK")
    end=0
    x,y,x1,y1=width/2,height/2,0,0#x,y->head pos;x1,y1->change in pos
    snake_speed=10
    level = 1
    body,blen=[],1
    vulnerable = 0
    clk=pygame.time.Clock()

    dir = "direction"

    food_x=round(random.randrange(0,width-cell)/cell)*cell
    food_y=round(random.randrange(0,height-cell)/cell)*cell


    white_life = 0
    white_life2 = 0
    white_x = round(random.randrange(0,width-cell)/cell)*cell
    white_y = round(random.randrange(0,width-cell)/cell)*cell
    round1 = 0

    food_x, food_y= get_food_position(width,height, body)

    while not end:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=1
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet_x = x
                    bullet_y = y
                    bullet = True
                    if dir == "right":
                        x2,y2=2*cell,0
                    if dir == "left":
                        x2, y2 = -2*cell,0
                    if dir == "up":
                        x2,y2=-0,-2*cell
                    if dir == "down":
                        x2, y2 = -0, 2*cell


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
        if bullet == True:
            bullet_x+=x2;bullet_y+=y2

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

        for i in range(0,5):
            if blen > 3:
                pygame.draw.rect(disp,grey,[brick_x[i],brick_y[i],cell,cell])

        if bullet == True:
            pygame.draw.rect(disp,brown,[bullet_x,bullet_y,cell,cell])

        if blen - white_life == 3:
            white_x=round(random.randrange(0,width-cell)/cell)*cell
            white_y=round(random.randrange(0,height-cell)/cell)*cell
            white_life = blen

        elif blen - white_life2 > 4:
            pygame.draw.rect(disp,white,[white_x,white_y,cell,cell])
            round1 += 1
            if round1 >100:
                round1 = 0

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
            food_x, food_y= get_food_position(width,height, body)
            blen+=1#body length increases

            if snake_speed<30: snake_speed+=0.5;

        for i in range(0,5):
            if blen>3:
                if brick_x[i] == x and brick_y[i] == y:
                    end =1


        if bullet == True:
            for i in range(0,5):
                if (bullet_x == brick_x[i] or bullet_x-cell == brick_x[i]) and (bullet_y == brick_y[i] or bullet_y-cell == brick_y[i]):
                    brick_x[i] = round(random.randrange(0,width-cell)/cell)*cell
                    brick_y[i] = round(random.randrange(0,height-cell)/cell)*cell
                    bullet = False

        if white_x == x and white_y == y:
            white_x=round(random.randrange(0,width-cell)/cell)*cell
            white_y=round(random.randrange(0,height-cell)/cell)*cell
            white_life = blen
            white_life2 = blen
            vulnerable = 50

        if vulnerable > 0:
            clk.tick(snake_speed-5)#fps
            vulnerable -= 1
        else:
            clk.tick(snake_speed)

        if vulnerable == 48:
            blen = blen - 3
            print(blen)



    clk.tick(snake_speed)
    disp.fill(black)
    m=font_style.render("Game Over",True,red)
    END_SOUND.play()
    disp.blit(m,[(width/2)-40,height/2])
    f = open("score.txt","a")
    f.write(str(blen-1)+"\n")
    f.close()
    with open("score.txt", "r") as f:
        score = f.read() # Read all file in case values are not on a single line
        score_ints = [ int(x) for x in score.split() ] # Convert strings to ints
    highscore = max(score_ints) # sum all elements of the list
    f_score=font_style.render("Score: "+str(blen-1),True,white)
    disp.blit(f_score,[(width/2)-30,(height/2)+27])
    f_hscore=font_style.render("High Score: "+str(highscore),True,white)
    disp.blit(f_hscore,[(width/2)-50,(height/2)+50])
    pygame.display.update()
    time.sleep(2)

while c == True:
    root = tk.Tk()
    root.geometry("600x300")
    b = tk.Button(root, text = "Click here to Start", command=root.destroy)
    var = tk.StringVar()
    var1 = tk.StringVar()
    var2 = tk.StringVar()
    var3 = tk.StringVar()
    var4 = tk.StringVar()
    var5 = tk.StringVar()
    label = tk.Label( root, textvariable=var)
    label1 = tk.Label( root, textvariable=var1)
    label2 = tk.Label( root, textvariable=var2)
    label3 = tk.Label( root, textvariable=var3)
    label4 = tk.Label( root, textvariable=var4)
    label5 = tk.Label( root, textvariable=var5)

    var.set("Rules:")
    var1.set("Press any key to start")
    var2.set("The Blue food makes you invulnerable for 5 seconds and increases your speed")
    var3.set("The WHite food slows you down and reduces your score by 3")
    var4.set("The red food increases your speed by a little")
    var5.set("Once you reach a score of 10 brick appear that you are supposed to dodge")
    label.pack()
    label1.pack()
    label2.pack()
    label3.pack()
    label4.pack()
    label5.pack()
    b.pack()
    root.mainloop()

    gameloop()

    root = tk.Tk()
    root.geometry("300x400")
    r = tk.Button(root, text = "exit", command=exit)
    var = tk.StringVar()
    label = tk.Label( root, textvariable=var)

    var.set("Thanks for playing")
    label.pack()
    r.pack()
    root.mainloop()
