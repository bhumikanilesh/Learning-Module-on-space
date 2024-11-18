import os, sys, math, pygame, pygame.mixer, random
from pygame.locals import *

def bhgame():
    black = (0,0,0)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    white = (255,255,255)
    run_me = win = True
    
    pygame.init()
    
    screen_size = screen_width, screen_height = 1280,720
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('blackhole')
    
    
    clock = pygame.time.Clock()
    fps_limit = 60
    
    #circle 
    FREE_TRIAL=pygame.font.Font("uncracked.otf",150)
    pixelfont=pygame.font.Font("pixel.ttf",30)
    
    colorcircle = (black)
    rc=60
    posx = 300
    posy = 200
    posxchange=0
    posychange=0
    
    objx = round(random.randrange(0, screen_width - 100) / 10.0) * 10.0
    objy = round(random.randrange(0, screen_height - 100) / 10.0) * 10.0

    ast=pygame.image.load("ast.png").convert_alpha()
    
    def text(msg,height):
        bhinfo=pixelfont.render(msg,1,(255,255,255))
        bhinforect=bhinfo.get_rect()
        bhinforect.center=(screen_width//2,height)
        screen.blit(bhinfo,bhinforect)
        pygame.display.update()
    
    text("Black holes possess the ability to absorb",250)
    text("things into its event horizon making them continuously",270)
    text("grow as they come in contact with matter",290)
    text("Use your arrow keys to move the blackhole to the asteroids",330)
    text("and make it grow without colliding it into the screen frame",350)
    text("to see how an ideal blackhole would increase in size",370)
    
    pygame.time.delay(15000)
    
    while run_me==True and win==True:
        clock.tick(fps_limit) 
    
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_me = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    posxchange = -20
                    posychange = 0
                elif event.key == pygame.K_RIGHT:
                    posxchange = 20
                    posychange = 0
                elif event.key == pygame.K_UP:
                    posychange = -20
                    posxchange = 0
                elif event.key == pygame.K_DOWN:
                    posychange = 20
                    posxchange = 0
                    
        if posx >= screen_width or posx < 0 or posy >= screen_height or posy < 0:
            win=False
            
        posx += posxchange
        posy += posychange
        
        screen.blit(ast,(objx,objy))
        pygame.display.update()
        
        image=pygame.image.load(os.path.join("bg.jpg"))
        image=pygame.transform.scale(image,(1280,720))
        screen.blit(image,(0,0))
        # redraw the circle
        pygame.draw.circle(screen, (10,20,30), (posx, posy), rc+23)
        pygame.draw.circle(screen, (20,0,65), (posx, posy), rc+13)
        pygame.draw.circle(screen, (16,78,139), (posx, posy), rc+9)
        pygame.draw.circle(screen, (0,104,139), (posx, posy), rc+8)
        pygame.draw.circle(screen, (24,116,205), (posx, posy), rc+7)
        pygame.draw.circle(screen, (28,134,238), (posx, posy), rc+6)
        pygame.draw.circle(screen, (0,154,205), (posx, posy), rc+5)
        pygame.draw.circle(screen, (0,178,238), (posx, posy), rc+4)
        pygame.draw.circle(screen, (121,205,205), (posx, posy), rc+3)
        pygame.draw.circle(screen, (250,235,215), (posx, posy), rc+1)
        pygame.draw.circle(screen, colorcircle, (posx, posy), rc)
        pygame.display.update()
        
        if objx-rc <= posx <= objx+rc and objy-rc <= posy <= objy+rc:
                objx = round(random.randrange(0, screen_width - 10) / 10.0) * 10.0
                objy = round(random.randrange(0, screen_height - 10) / 10.0) * 10.0
                rc+=10
                
        clock.tick(30)
        
        if win==False:
            title=FREE_TRIAL.render('you went out of bounds',1,(255,255,255))
            titlerect=title.get_rect()
            titlerect.center=(screen_width//2,150)
            screen.blit(title,titlerect)
            pygame.display.update()
            pygame.time.delay(4000)
            

    