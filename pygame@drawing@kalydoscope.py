import pygame,sys,random
from pygame.locals import *
import math
from pygame import mixer

pygame.init()
screenlenth=800
screen=pygame.display.set_mode((screenlenth,screenlenth))
line=20
xc=int(screenlenth/2)
yc=int(screenlenth/2)

m=[]

a=[(0,0)]
a2=[(0,0)]

pensize=4

angle=0

def text_objects(text, font):
    textSurfac = font.render(text, True, (255,255,255))
    return textSurfac, textSurfac.get_rect()

def button(x,y,w,h):
    mice=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    
    if((x+w+4>mice[0]>x-4) and (y+h+4>mice[1]>y-4)):
        if click[0]==1:
            clm=mixer.Sound('laser.wav')
            clm.play()
            r= -1
        else:r=1
    else:      
        r=1
    return r

def buttondraw(text,x,y,w,h,c1,c2,r):
    if(r==1):
        pygame.draw.rect(screen,c2,(x,y,w,h))
    else:      
        pygame.draw.rect(screen,c1,(x,y,w,h))
    buttontext=pygame.font.Font('freesansbold.ttf',40)
    textsurf,textRect=text_objects(text,buttontext)
    textRect.center=( (x+(w/2)), (y+(h/2)) )
    screen.blit(textsurf,textRect)
    
    
don=1
d=1
running=True
   
    
while running:
    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
                running=False
        if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
    mice=pygame.mouse.get_pos() 
    click=pygame.mouse.get_pressed()
   
    
    if(((a[len(a)-1][0]!=mice[0]) and (a[len(a)-1][1]!=mice[1]) )and (click[0]==1) and (mice[1]>=54)):
           m=[]
           m=[mice[0]-xc,mice[1]-yc,x,(math.atan2(mice[1]-yc,mice[0]-xc)/math.pi*(180))]
           a.append(m)
           m=[-1*(mice[0]-xc),(mice[1]-yc),x,(math.atan2((mice[1]-yc),-1*(mice[0]-xc))/math.pi*(180))]
           a2.append(m)
           x=1
    if(click[0]==0):
        x=0
    
    for i in range(2,len(a)):
        if(a[i][2]==1):
         l1=((int(a[i][0])**2)+(int(a[i][1])**2))**(.5)
         l2=((int(a[i-1][0])**2)+(int(a[i-1][1])**2))**(.5)
         l12=((int(a2[i][0])**2)+(int(a2[i][1])**2))**(.5)
         l22=((int(a2[i-1][0])**2)+(int(a2[i-1][1])**2))**(.5)
         
         for j in range(0,360,20):
              pygame.draw.line(screen,(int((2*angle)%255),255-int((2*angle)%255),int(0)),(int(l1*math.cos((angle+j+a[i][3])*(math.pi/180)))+xc,int(l1*math.sin((angle+j+a[i][3])*(math.pi/180)))+yc),(int(l2*math.cos((angle+j+a[i-1][3])*(math.pi/180)))+xc,int(l2*math.sin((angle+j+a[i-1][3])*(math.pi/180)))+yc),pensize)
              pygame.draw.line(screen,(int((2*angle)%255),255-int((2*angle)%255),int(0)),(int(l12*math.cos((angle+j+a2[i][3])*(math.pi/180)))+xc,int(l12*math.sin((angle+j+a2[i][3])*(math.pi/180)))+yc),(int(l22*math.cos((angle+j+a2[i-1][3])*(math.pi/180)))+xc,int(l22*math.sin((angle+j+a2[i-1][3])*(math.pi/180)))+yc),pensize)
    d=button(700,10,50,40)
    
    don=don*d
    
    buttondraw("R",700,10,50,50,(255,255,0),(0,255,255),don)
    
    if(don==1):anglep=0
    else:anglep=.4
    angle+=anglep
       
    pygame.display.update()
    