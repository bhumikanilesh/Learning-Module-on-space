
import time
import turtle
import pygame
import math
import os
import sys
import winsound

def intro():
    t=turtle.Turtle()
    s=turtle.Screen()
    s.bgcolor("black")
    s.screensize(1280,720)
    s.setup(width=1280,height=720,startx=0,starty=0)
    t.pencolor("white")
    t.pensize(3)
    winsound.PlaySound('tm.wav',winsound.SND_ASYNC)
    
    
    
    def func():
        #setting the position of the turtle cursor
        t.penup()
        x=-200
        y=100
        t.goto(x,y)
        t.pendown()
       
        #creates the S
        t.forward(50)
        t.back(50)
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.right(90)
        t.forward(50) 
        t.right(90)
        t.forward(50)
        t.back(50)
        t.right(180)
        
        #moving to write the next character
        t.penup()
        t.forward(25)
        t.pendown()
        
        #creates the letter P
        t.left(90)
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.left(90)
        
        #cursor moves to write the next character
        t.penup()
        t.forward(75)
        t.pendown()
        
        #creates A
        t.left(90)
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.back(50)
        t.left(90)
        t.forward(50)
        
        #moving to write the next character
        t.left(90)
        t.penup()
        t.forward(25) 
        t.pendown()
        
        #creates C
        t.left(90)
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.back(50)
        t.left(90)
        t.back(100)
        t.right(90)
        t.forward(50)
        
        #moving to write the next character
        t.penup()
        t.forward(25)
        t.pendown()
        
        #creates E
        t.left(90)
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.back(50)
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.back(50)
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(100)
        
        
        #making the box
        t.left(90)
        t.forward(125)
        t.left(90)
        t.forward(450)
        t.left(90)
        
        t.forward(150)
        t.left(90)
        t.forward(450)
        t.right(90)
        t.forward(44.5)
        t.right(90)
        t.forward(450)
        t.right(90)
        t.forward(44.5)
    
        t.back(40)
        t.right(90)
            
    func()
    
    second_count=0

    #stopwatch
    def layout():  
        
        t.write("The infinite beyond and depths of space in",font=40)
        t.penup()
        t.forward(380)
        t.pendown()
        
    def quit():
        global running
        running=False
    s.onkeypress(quit)    
    
    def seconds(second_count):    
        second_count=6
        running=True
        while running:
            #reduces the value by 1 for display purpose
            second_count-=1
            
            #actual time module reduces the value by only 1
            time.sleep(1)
            
            #erases the old time value to print the new one
            t.undo()
            t.write(second_count,font=25)
            if second_count==0:
                s.bye()
                running=False
            else:
                pass
            
    layout() 
    seconds(second_count)      
    
    
    
    
    pygame.init()
    WIDTH,HEIGHT=1280,720
    WIN=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("introduction")
    
    #images
    images=[]
    for j in range (1,1362):
        image=pygame.image.load(os.path.join('images/1 ('+str(j)+").jpg"))
        image=pygame.transform.scale(image, (1280,720))
        images.append(image)
        
    FPS=60
    WHITE=(255,255,255)
    #INITIALIZES THE CLOCK-makes the execution uniform 
    clock=pygame.time.Clock()
    
    draw1con=True
    i=0
    while draw1con==True:
      while i<1360:
          WIN.fill(WHITE)
          WIN.blit(images[i],(0,0))
          pygame.display.update()
          events = pygame.event.get()
          i+=1
          pygame.time.delay(28)
      draw1con=False
    if draw1con==False:
        pygame.quit()
      
  
intro()

