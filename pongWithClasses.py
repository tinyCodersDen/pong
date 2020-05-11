
'''
 >> Pong Game with PyGame and Class
 >> Developed by : tinyCoder (Vihan)

'''
import pygame
from pygame.locals import *
import time
import random
import sys
#pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Pong by TinyCoder")
clock = pygame.time.Clock()
rect_x=150
rect_y=300
rect_x2=350
rect_y2=300
orange=(255,159,0)
class Paddle():
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
        self.height=100
        self.width=20
        self.up=False
        self.down=False
        self.speed=10
        self.rect=None
    def draw(self):
        self.rect=pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
        if self.up==True and self.y>0:
            self.y=self.y-self.speed
        if self.down==True and self.y<500:
            self.y=self.y+self.speed
class Ball():
    def __init__(self):
        self.x=300
        self.y=300
        self.color=(0,255,0)
        self.radius=20
        self.xmove=random.choice([-5,-4,-3,-2,-1,1,2,3,4,5])
        self.ymove=random.randint(-5,5)
        self.rect=None
        self.red_score=0
        self.blue_score=0
        self.font=None
        self.win_blue=None
        self.red_win=None
        if self.xmove<0:
            self.hit="blue"
        else:
            self.hit="red"
    def draw(self):
        self.rect=pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
        self.x=self.x-self.xmove
        self.y=self.y+self.ymove
        if self.y>580 or self.y<0:
            self.ymove=-self.ymove
        if self.x<=0:
            self.xmove=-self.xmove
            self.blue_score=self.blue_score+1
            self.hit="red"
            if self.blue_score==3:
                screen.fill((0,0,0))
                self.font=pygame.font.Font("freesansbold.ttf",50)
                self.win_blue=self.font.render("Blue Wins!",True,(0,0,255))
                screen.blit(self.win_blue,(150,300))
                pygame.display.update()
                time.sleep(5)
                pygame.quit()
                sys.exit()
        if self.x>=580:
            self.xmove=-self.xmove
            self.red_score=self.red_score+1
            self.hit="blue"
            if self.red_score==3:
                screen.fill((0,0,0))
                self.font=pygame.font.Font("freesansbold.ttf",50)
                self.red_win=self.font.render("Red Wins!",True,(255,0,0))
                screen.blit(self.red_win,(150,300))
                pygame.display.update()
                time.sleep(5)
                pygame.quit()
                sys.exit()
def controls(list1,list2,list3,list4):
    font=pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(list1[0], False, list1[3])
    screen.blit(text,(list1[1],list1[2]))
    arrowkeyb=pygame.image.load('png/up.png')
    arrowkey=pygame.transform.rotozoom(arrowkeyb,0,0.05)
    screen.blit(arrowkey,(list2[0],list2[1]))
    arrowkey=pygame.transform.rotozoom(arrowkeyb,list2[4],0.05)
    screen.blit(arrowkey,(list2[2],list2[3]))
    text = font.render(list3[0], False, (255,255,255))
    screen.blit(text,(list3[1],list3[2]))
    text = font.render(list4[0], False, (255,255,255))
    screen.blit(text,(list4[1],list4[2]))
def menu():
    while True:
        pygame.draw.rect(screen,(0,255,0),(rect_x,rect_y,110,100))
        pygame.draw.rect(screen,(0,255,0),(rect_x2,rect_y2,110,100))
        font = pygame.font.Font('freesansbold.ttf', 45)
        text = font.render('Play', False, (0,0,0))
        screen.blit(text,(155,320))
        text = font.render('Quit', False, (0,0,0))
        screen.blit(text,(355,320))
        list1=["- Red Player -",30,20,(255,0,0)]
        list2=[25,50,25,100,180]
        list3=["- Up Arrow Key",60,60]
        list4=["- Down Arrow Key",60,100]
        controls(list1,list2,list3,list4)
        list1=["- Blue Player -",350,20,(0,0,255)]
        list2=[350,50,350,100,180]
        list3=['- "W" Key',380,60]
        list4=['- "S" Key',380,100]
        pygame.draw.line(screen,(255,255,255),(0,45),(600,45),2)
        pygame.draw.line(screen,(255,255,255),(300,0),(300,150),2)
        pygame.draw.line(screen,(255,255,255),(0,150),(600,150),2)
        controls(list1,list2,list3,list4)
        pygame.display.update()
        for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if 150<=event.pos[0]<=260 and 300<=event.pos[1]<=400:
                        screen.fill((0,0,0))
                        return
                    if 350<=event.pos[0]<=450 and 300<=event.pos[1]<=400:
                        pygame.quit()
                        exit()           
menu()
def Scoredraw(msg,position,size,color):
    font=pygame.font.Font("freesansbold.ttf",size)
    text=font.render(str(msg),True,color)
    screen.blit(text,(position))
ball=Ball()
paddle1=Paddle(50,300,(255,0,0))
paddle2=Paddle(550,300,(0,0,255))
#pygame.mixer.music.load('Low_Life_High_Life (3).mp3')
#pygame.mixer.music.play(-1)
while True:
    clock.tick(60)
    paddle1.draw()
    paddle2.draw()
    ball.draw()
    Scoredraw("Score:%d"%ball.red_score,(0,0),32,(0,255,0))
    Scoredraw("Score:%d"%ball.blue_score,(480,0),32,(0,255,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==KEYDOWN:
            if event.key==K_UP:
                paddle1.up=True
            if event.key==K_w:
                paddle2.up=True
            if event.key==K_DOWN:
                paddle1.down=True
            if event.key==K_s:
                paddle2.down=True
        elif event.type==KEYUP:
            if event.key==K_UP:
                paddle1.up=False
            if event.key==K_w:
                paddle2.up=False
            if event.key==K_DOWN:
                paddle1.down=False
            if event.key==K_s:
                paddle2.down=False
    if (ball.rect.colliderect(paddle2.rect) and ball.hit=="red"):
        ball.hit="blue"
        ball.xmove=-ball.xmove
        ball.ymove=random.randint(-5,5)
    elif (ball.rect.colliderect(paddle1.rect) and ball.hit=="blue"):
        ball.hit="red"
        ball.xmove=-ball.xmove
        ball.ymove=random.randint(-5,5)
    pygame.display.update()
    screen.fill((0,0,0))
