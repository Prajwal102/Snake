import pygame
from pygame.locals import*
from random import randint
import random,math,time
pygame.init()
width,height=500,400
disp=pygame.display.set_mode((width,height))
RED=(255,0,0)
WHITE=(0,0,0)
GREEN=(0,255,0)
disp.fill(RED)
pygame.display.update()
xspeed,yspeed=0,0
clock=pygame.time.Clock()
class Block:
    P=[]
    total=0
    food_x,food_y=-1,-1
    haseaten=False
    def __init__(self,x,y):
        self.x=x
        self.y=y
       # self.color=color

    def draw(self):
        pygame.draw.rect(disp,GREEN,(self.food_x,self.food_y,10,10))
        for i in range(len(self.P)):
            pygame.draw.rect(disp,WHITE,(self.P[i][0],self.P[i][1],10,10))

    def update(self):
        pygame.display.update()


    def food(self):
        self.food_x=randint(0,width-10)
        self.food_y=randint(0,height-10)
        self.food_x-=(self.food_x%10)
        self.food_y-=(self.food_y%10)

    def death(self):
        for i in self.P:
            dis=math.hypot(abs(self.x-i[0]),abs(self.y-i[1]))
            if dis==0:
                self.total=0
                self.P=[]
    def edges(self):
        if self.x>width-10:
            self.x=0
        if self.x<0:
            self.x=width
        if self.y<0:
            self.y=height-10
        if self.y>height-10:
            self.y=0
    def eat(self):
        dist=math.hypot(abs(self.x-self.food_x),abs(self.y-self.food_y))
        if dist<3:
            self.total+=1
            self.haseaten=True
            self.P.append((self.x,self.y))
            return (self.total)
        else:
            return(0)

b=Block(250,200)
b.food()
run=True
while run:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                xspeed=-10
                yspeed=0
            if event.key==K_RIGHT:
                xspeed=10
                yspeed=0
            if event.key==K_UP:
                yspeed=-10
                xspeed=0
            if event.key==K_DOWN:
                yspeed=10
                xspeed=0
    b.x+=xspeed
    b.y+=yspeed
    pygame.draw.rect(disp,WHITE,(b.x,b.y,10,10))
    b.draw()
    clock.tick(10)
    b.death()
    b.edges()
    b.update()
    b.P=b.P[1:]
    b.eat()
    if b.haseaten:
        b.food()
    b.haseaten=False
    if (b.total>0):

        if b.total==len(b.P):
            for i in range(len(b.P)-1):
                b.P[i]=b.P[i+1]
        b.P.append((b.x,b.y))

    disp.fill(RED)
