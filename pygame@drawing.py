import time
import pygame,sys
from pygame.locals import *
import math
pygame.init()
screenlenth=750
screen=pygame.display.set_mode((screenlenth,screenlenth))
pygame.display.set_caption("Drawing")

a=[(0,0)]
def text_objects(text, font):
    textSurfac = font.render(text, True, (255,255,255))
    return textSurfac, textSurfac.get_rect()

def button(text,x,y,w,h,c1,c2,action=None):
    miceb=pygame.mouse.get_pos()
    clickb=pygame.mouse.get_pressed()
    global color
    global pensize
    global a
    if((x+w>miceb[0]>x) and (y+h>miceb[1]>y)):
        pygame.draw.rect(screen,c2,(x,y,w,h))
        if (clickb[0]==1 and action!=None):
            if(action=="r"):color=(255,0,0)
            if(action=="g"):color=(0,255,0)
            if(action=="v"):color=(98,0,255)
            if(action=="i"):color=(18,255,255)
            if(action=="y"):color=(250,217,5)
            if(action=="o"):color=(234,139,0)
            if(action=="b"):color=(0,0,255)
            if(action=='w'):color=(245,245,245)
            if(action=="E"):color=(0,0,0)
            if(action==">"):pensize=pensize+1
            if(action=="<") and (pensize>0):pensize=pensize-1
            if(action=="ac"):a=[(0,0)]            
    else:pygame.draw.rect(screen,c1,(x,y,w,h))
    buttontext=pygame.font.Font('freesansbold.ttf',20)
    textsurf,textRect=text_objects(text,buttontext)
    textRect.center=( (x+(w/2)), (y+(h/2)) )
    screen.blit(textsurf,textRect)
fonts2=pygame.font.Font('freesansbold.ttf',20)

def sizeboard(lent):
    length=fonts2.render("size: "+str(lent),True,(29, 240, 22))
    screen.blit(length,(10,720))
color=(255,255,255) 
pensize=4  
line_length=250
x=None
running=True
while running:
        
        screen.fill((0,0,0))       
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        mice=pygame.mouse.get_pos() 
        click=pygame.mouse.get_pressed()
        
        button("R",20,10,40,40,(255,0,0),(255,115,119),"r")
        button("G",80,10,40,40,(0,255,0),(128,255,115),"g")
        button("V",140,10,40,40,(98,0,255),(143,85,250),"v")
        button("I",200,10,40,40,(18,255,255),(143,235,99),"i")
        button("Y",260,10,40,40,(250,217,5),(255,235,99),"y")
        button("O",320,10,40,40,(234,139,0),(205,207,102),"o")
        button("ERASER",500,10,90,40,(200,140,55),(60,60,60),"E")
        button("W",440,10,40,40,(245,245,245),(128,128,128),"w")
        button("B",380,10,40,40,(0,0,255),(128,115,255),"b")
        button("<",610,10,20,40,(139,139,139),(200,200,200),"<")
        button(">",645,10,20,40,(139,139,139),(201,201,201),">")
        button("AC",680,10,40,40,(50,50,50),(220,220,220),"ac")
        '''
        if(action=="r"):color=(255,0,0)
        if(action=="g"):color=(0,255,0)
        if(action=="v"):color=(98,0,255)
        if(action=="i"):color=(18,255,255)
        if(action=="y"):color=(250,217,5)
        if(action=="o"):color=(234,139,0)
        if(action=="b"):color=(0,0,255)
        if(action=='w'):color=(245,245,245)
        if(action=="E"):color=(0,0,0)
        '''
        
        if(((a[len(a)-1][0]!=mice[0]) and (a[len(a)-1][1]!=mice[1]) )and (click[0]==1) and (mice[1]>=54)):
           m=[]
           m=[mice[0],mice[1],x,color,pensize]
           a.append(m)
           x=1
        if(click[0]==0):
            x=0
        
        for i in range(2,len(a)):
            if(a[i][2]==1) and (a[i][4]>=1):
              pygame.draw.line(screen,(a[i-1][3]),(int(a[i-1][0]),int(a[i-1][1])),(int(a[i][0]),int(a[i][1])),int(a[i][4]))
        sizeboard(pensize)   
        pygame.display.update()
        