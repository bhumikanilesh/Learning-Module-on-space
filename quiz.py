import pygame,  sys
from buttons import Button

pygame.init()
sunb=merb=venb=earb=marb=jupb=satb=uranb=nepb=True
points=0
BG=pygame.transform.scale(pygame.image.load("Quiz/sp.jpeg"),(1300,700))
hubblebg=pygame.transform.scale(pygame.image.load("Quiz/hubblebg.jpg"),(1300,700))
screen_size = screen_width, screen_height = 1300,700
SCREEN= pygame.display.set_mode(screen_size)

def quiz():
    def option_button(image,pos,text,bc):
        return Button(image=pygame.image.load(image), pos=(pos), 
        text_input=text, font=get_font(50), base_color=bc, hovering_color="White")

    def sunbutton():
        global points
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
    
            SCREEN.blit(hubblebg,(0,0))
            for button in [q1o1,q1o2,q1o3,q1o4]:
                button.changeColor(OPTIONS_MOUSE_POS)
                button.update(SCREEN)
            OPTIONS_TEXT = get_font(50).render("Q.1 The sun's layers are entirely made of", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 120))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if q1o1.checkForInput(OPTIONS_MOUSE_POS):
                        points+=1
                        s_sys()
                    elif q1o2.checkForInput(OPTIONS_MOUSE_POS) or q1o3.checkForInput(OPTIONS_MOUSE_POS) or q1o4.checkForInput(OPTIONS_MOUSE_POS):
                        s_sys()
            pygame.display.update()
    
    def mercurybutton():
        global points
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
    
            SCREEN.blit(hubblebg,(0,0))
            for button in [q2o1,q2o2,q2o3,q2o4]:
                button.changeColor(OPTIONS_MOUSE_POS)
                button.update(SCREEN)
            OPTIONS_TEXT = get_font(50).render("Q.2 How many earth days makes a mercury year?", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 120))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if q2o4.checkForInput(OPTIONS_MOUSE_POS):
                        points+=1
                        s_sys()
                    elif q2o2.checkForInput(OPTIONS_MOUSE_POS) or q2o3.checkForInput(OPTIONS_MOUSE_POS) or q2o1.checkForInput(OPTIONS_MOUSE_POS):
                        s_sys()
            pygame.display.update()
    
    def venusbutton():
        global points
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
    
            SCREEN.blit(hubblebg,(0,0))
            for button in [q3o1,q3o2,q3o3,q3o4]:
                button.changeColor(OPTIONS_MOUSE_POS)
                button.update(SCREEN)
            OPTIONS_TEXT = get_font(50).render("Q.3 What gas is most abundant in Venus’s atmosphere?", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 120))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if q3o3.checkForInput(OPTIONS_MOUSE_POS):
                        points+=1
                        s_sys()
                    elif q3o2.checkForInput(OPTIONS_MOUSE_POS) or q3o4.checkForInput(OPTIONS_MOUSE_POS) or q3o1.checkForInput(OPTIONS_MOUSE_POS):
                        s_sys()
            pygame.display.update()
    
    def earthbutton():
        global points
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
    
            SCREEN.blit(hubblebg,(0,0))
            for button in [q4o1,q4o2,q4o3,q4o4]:
                button.changeColor(OPTIONS_MOUSE_POS)
                button.update(SCREEN)
            OPTIONS_TEXT = get_font(50).render("Q.4 What is the name given to earth's imaginary line at latitude zero?", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 120))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if q4o3.checkForInput(OPTIONS_MOUSE_POS):
                        points+=1
                        s_sys()
                    elif q4o2.checkForInput(OPTIONS_MOUSE_POS) or q4o4.checkForInput(OPTIONS_MOUSE_POS) or q4o1.checkForInput(OPTIONS_MOUSE_POS):
                        s_sys()
            pygame.display.update()
    
    def marsbutton():
        global points
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
    
            SCREEN.blit(hubblebg,(0,0))
            for button in [q5o1,q5o2,q5o3,q5o4]:
                button.changeColor(OPTIONS_MOUSE_POS)
                button.update(SCREEN)
            OPTIONS_TEXT = get_font(50).render("Q.5 A common nickname for Mars is", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 120))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if q5o4.checkForInput(OPTIONS_MOUSE_POS):
                        points+=1
                        s_sys()
                    elif q5o2.checkForInput(OPTIONS_MOUSE_POS) or q5o3.checkForInput(OPTIONS_MOUSE_POS) or q5o1.checkForInput(OPTIONS_MOUSE_POS):
                        s_sys()
            pygame.display.update()
            
    def jupiterbutton():
        global points
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
    
            SCREEN.blit(hubblebg,(0,0))
            for button in [q6o1,q6o2,q6o3,q6o4]:
                button.changeColor(OPTIONS_MOUSE_POS)
                button.update(SCREEN)
            OPTIONS_TEXT = get_font(50).render("Q.6 How many moons does Jupiter have?", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 120))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if q6o1.checkForInput(OPTIONS_MOUSE_POS):
                        points+=1
                        s_sys()
                    elif q6o2.checkForInput(OPTIONS_MOUSE_POS) or q6o3.checkForInput(OPTIONS_MOUSE_POS) or q6o4.checkForInput(OPTIONS_MOUSE_POS):
                        s_sys()
            pygame.display.update()
            
    def saturnbutton():
        global points
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
    
            SCREEN.blit(hubblebg,(0,0))
            for button in [q7o1,q7o2,q7o3,q7o4]:
                button.changeColor(OPTIONS_MOUSE_POS)
                button.update(SCREEN)
            OPTIONS_TEXT = get_font(50).render("Q.7 What is Saturn's rings mainly composed of?", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 120))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if q7o4.checkForInput(OPTIONS_MOUSE_POS):
                        points+=1
                        s_sys()
                    elif q7o2.checkForInput(OPTIONS_MOUSE_POS) or q7o3.checkForInput(OPTIONS_MOUSE_POS) or q7o1.checkForInput(OPTIONS_MOUSE_POS):
                        s_sys()
            pygame.display.update()
    
    
    def get_font(size): 
        return pygame.font.Font("Quiz/exon.otf", size)
    
    def uranusbutton():
        global points
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
    
            SCREEN.blit(hubblebg,(0,0))
            for button in [q8o1,q8o2,q8o3,q8o4]:
                button.changeColor(OPTIONS_MOUSE_POS)
                button.update(SCREEN)
            OPTIONS_TEXT = get_font(50).render("Q.8 Uranus axial tilt is ____________ degrees.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 120))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if q8o4.checkForInput(OPTIONS_MOUSE_POS):
                        points+=1
                        s_sys()
                    elif q8o2.checkForInput(OPTIONS_MOUSE_POS) or q8o3.checkForInput(OPTIONS_MOUSE_POS) or q8o1.checkForInput(OPTIONS_MOUSE_POS):
                        s_sys()
            pygame.display.update()
            
    def neptunebutton():
        global points
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            SCREEN.blit(hubblebg,(0,0))
            for button in [q9o1,q9o2,q9o3,q9o4]:
                button.changeColor(OPTIONS_MOUSE_POS)
                button.update(SCREEN)
            OPTIONS_TEXT = get_font(50).render("Q.9 What makes Neptune appear blue?", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 120))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if q9o2.checkForInput(OPTIONS_MOUSE_POS):
                        points+=1
                        s_sys()
                    elif q9o4.checkForInput(OPTIONS_MOUSE_POS) or q9o3.checkForInput(OPTIONS_MOUSE_POS) or q9o1.checkForInput(OPTIONS_MOUSE_POS):
                        s_sys()
            pygame.display.update()
    
      
    s=pygame.transform.scale(pygame.image.load("Quiz/sun.png"),(200,200))
    hg=pygame.transform.scale(pygame.image.load("Quiz/mercury.png"),(20,20))
    v=pygame.transform.scale(pygame.image.load("Quiz/Venus.png"),(40,40))
    e=pygame.transform.scale(pygame.image.load("Quiz/earth.png"),(40,40))
    m=pygame.transform.scale(pygame.image.load("Quiz/mars.png"),(30,30))
    asb=pygame.transform.scale(pygame.image.load("Quiz/asb.png"),(650,650))
    j=pygame.transform.scale(pygame.image.load("Quiz/Jupiter.png"),(120,120))
    sa=pygame.transform.scale(pygame.image.load("Quiz/saturn.png"),(120,90))
    u=pygame.transform.scale(pygame.image.load("Quiz/uranus.png"),(90,90))
    n=pygame.transform.scale(pygame.image.load("Quiz/neptune.png"),(65,50)) 
    
    
    sun=Button(image=s, pos=(650, 450), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
    HG=Button(image=hg, pos=(790, 450), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
    venus=Button(image=v, pos=(840,500), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
    earth=Button(image=e, pos=(600, 270), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
    mars= Button(image=m, pos=(415, 440), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
    a=Button(image=asb, pos=(650, 450), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
    jup=Button(image=j, pos=(260, 500), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
    sat=Button(image=sa, pos=(230, 110), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
    ur=Button(image=u, pos=(1100, 600), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
    nep=Button(image=n, pos=(1200, 200), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
    
    q1o1=option_button('Quiz/box.png',(640,220),'Hydrogen and Helium',"#CCE5FF")
    q1o2=option_button('Quiz/box.png',(640,340),'Hydrogen and Nitrogen',"#CCE5FF")
    q1o3=option_button('Quiz/box.png',(640,460),'Nitrogen and Helium',"#CCE5FF")
    q1o4=option_button('Quiz/box.png',(640,580),'Nitrogen and Lithium',"#CCE5FF")
    
    q2o1=option_button('Quiz/box.png',(640,220),'58',"#CCE5FF")
    q2o2=option_button('Quiz/box.png',(640,340),'68',"#CCE5FF")
    q2o3=option_button('Quiz/box.png',(640,460),'78',"#CCE5FF")
    q2o4=option_button('Quiz/box.png',(640,580),'88',"#CCE5FF")
    
    q3o1=option_button('Quiz/box.png',(640,220),'Nitrogen',"#CCE5FF")
    q3o2=option_button('Quiz/box.png',(640,340),'Oxygen',"#CCE5FF")
    q3o3=option_button('Quiz/box.png',(640,460),'Carbon dioxide',"#CCE5FF")
    q3o4=option_button('Quiz/box.png',(640,580),'Hydrogen',"#CCE5FF")
    
    q4o1=option_button('Quiz/box.png',(640,220),'Tropic of cancer',"#CCE5FF")
    q4o2=option_button('Quiz/box.png',(640,340),'Tropic of capricorn',"#CCE5FF")
    q4o3=option_button('Quiz/box.png',(640,460),'Equator',"#CCE5FF")
    q4o4=option_button('Quiz/box.png',(640,580),'Prime meridian',"#CCE5FF")
    
    q5o1=option_button('Quiz/box.png',(640,220),'The floating world',"#CCE5FF")
    q5o2=option_button('Quiz/box.png',(640,340),'The fifth element',"#CCE5FF")
    q5o3=option_button('Quiz/box.png',(640,460),'The final frontier',"#CCE5FF")
    q5o4=option_button('Quiz/box.png',(640,580),'The red planet',"#CCE5FF")
    
    q6o1=option_button('Quiz/box.png',(640,220),'79',"#CCE5FF")
    q6o2=option_button('Quiz/box.png',(640,340),'106',"#CCE5FF")
    q6o3=option_button('Quiz/box.png',(640,460),'97',"#CCE5FF")
    q6o4=option_button('Quiz/box.png',(640,580),'69',"#CCE5FF")
    
    q7o1=option_button('Quiz/box.png',(640,220),'Rocks',"#CCE5FF")
    q7o2=option_button('Quiz/box.png',(640,340),'Dust',"#CCE5FF")
    q7o3=option_button('Quiz/box.png',(640,460),'Ice',"#CCE5FF")
    q7o4=option_button('Quiz/box.png',(640,580),'All of the above',"#CCE5FF")
    
    q8o1=option_button('Quiz/box.png',(640,220),'25.6',"#CCE5FF")
    q8o2=option_button('Quiz/box.png',(640,340),'42',"#CCE5FF")
    q8o3=option_button('Quiz/box.png',(640,460),'26.5',"#CCE5FF")
    q8o4=option_button('Quiz/box.png',(640,580),'98',"#CCE5FF")
    
    q9o1=option_button('Quiz/box.png',(640,220),'Hydrogen',"#CCE5FF")
    q9o2=option_button('Quiz/box.png',(640,340),'Methane',"#CCE5FF")
    q9o3=option_button('Quiz/box.png',(640,460),'Distance from sun',"#CCE5FF")
    q9o4=option_button('Quiz/box.png',(640,580),'Rotation',"#CCE5FF")
    #mars= Button(image=pygame.image.load("mars.png"), pos=(640, 550), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
    
    def s_sys():
        global sunb,merb,venb,earb,marb,jupb,satb,uranb,nepb
        while True:
            SCREEN.blit(BG, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            OPTIONS_BACK = Button(image=None, pos=(40,30), 
                            text_input="<--", font=get_font(40), base_color="White", hovering_color="Green")
        
            OPTIONS_BACK.changeColor(MENU_MOUSE_POS)
            OPTIONS_BACK.update(SCREEN)
            for button in [sun,HG, venus,earth,mars,a,jup,sat,ur,nep]:
                button.update(SCREEN)     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if sunb==True and sun.checkForInput(MENU_MOUSE_POS):
                        sunb=False
                        sunbutton()
                    if merb==True and HG.checkForInput(MENU_MOUSE_POS):
                        merb=False
                        mercurybutton()
                    if venb==True and venus.checkForInput(MENU_MOUSE_POS):
                        venb=False
                        venusbutton()
                    if earb==True and earth.checkForInput(MENU_MOUSE_POS):
                        earb=False
                        earthbutton()
                    if marb==True and mars.checkForInput(MENU_MOUSE_POS):
                        marb=False
                        marsbutton()
                    if jupb==True and jup.checkForInput(MENU_MOUSE_POS):
                        jupb=False
                        jupiterbutton()
                    if satb==True and sat.checkForInput(MENU_MOUSE_POS):
                        satb=False
                        saturnbutton()
                    if uranb==True and ur.checkForInput(MENU_MOUSE_POS):
                        uranb=False
                        uranusbutton()
                    if nepb==True and nep.checkForInput(MENU_MOUSE_POS):
                        nepb=False
                        neptunebutton()
                    if OPTIONS_BACK.checkForInput(MENU_MOUSE_POS):
                        main_menu()
            pygame.display.update()
    
    s_sys()
