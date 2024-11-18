import pygame, pygame_gui, sys
from buttons import Button
from ccode import zc
from blackhole import bhgame
from quiz import *
from h import sol_info,able_text
from subprocess import call

class CallPy(object):
    
    def __init__(self,path):
        self.path=path
        
    def call_python_file(self):
        call(['Python','{}'.format(self.path)])
    
if __name__=="__main__":
    c=CallPy(path='brsprjtrial.py')
    c.call_python_file()

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
manager = pygame_gui.UIManager((1280, 720))

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((330, 300), (600, 50)), manager=manager,object_id='#main_text_entry')

clock = pygame.time.Clock()
WIDTH, HEIGHT = 1280, 720


#------------------------------------------------------------------------------
sunb=merb=venb=earb=marb=jupb=satb=uranb=nepb=True
points=0
QBG=pygame.transform.scale(pygame.image.load("Quiz/sp.jpeg"),(1300,700))
hubblebg=pygame.transform.scale(pygame.image.load("Quiz/hubblebg.jpg"),(1300,700))
screen_size = screen_width, screen_height = 1300,700
SCREEN= pygame.display.set_mode(screen_size)



def quiz():
    def option_button(pos,text,bc):
        return Button(image=pygame.image.load('Quiz/box.png'), pos=(pos), 
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
    
    q1o1=option_button((640,220),'Hydrogen and Helium',"#CCE5FF")
    q1o2=option_button((640,340),'Hydrogen and Nitrogen',"#CCE5FF")
    q1o3=option_button((640,460),'Nitrogen and Helium',"#CCE5FF")
    q1o4=option_button((640,580),'Nitrogen and Lithium',"#CCE5FF")
    
    q2o1=option_button((640,220),'58',"#CCE5FF")
    q2o2=option_button((640,340),'68',"#CCE5FF")
    q2o3=option_button((640,460),'78',"#CCE5FF")
    q2o4=option_button((640,580),'88',"#CCE5FF")
    
    q3o1=option_button((640,220),'Nitrogen',"#CCE5FF")
    q3o2=option_button((640,340),'Oxygen',"#CCE5FF")
    q3o3=option_button((640,460),'Carbon dioxide',"#CCE5FF")
    q3o4=option_button((640,580),'Hydrogen',"#CCE5FF")
    
    q4o1=option_button((640,220),'Tropic of cancer',"#CCE5FF")
    q4o2=option_button((640,340),'Tropic of capricorn',"#CCE5FF")
    q4o3=option_button((640,460),'Equator',"#CCE5FF")
    q4o4=option_button((640,580),'Prime meridian',"#CCE5FF")
    
    q5o1=option_button((640,220),'The floating world',"#CCE5FF")
    q5o2=option_button((640,340),'The fifth element',"#CCE5FF")
    q5o3=option_button((640,460),'The final frontier',"#CCE5FF")
    q5o4=option_button((640,580),'The red planet',"#CCE5FF")
    
    q6o1=option_button((640,220),'79',"#CCE5FF")
    q6o2=option_button((640,340),'106',"#CCE5FF")
    q6o3=option_button((640,460),'97',"#CCE5FF")
    q6o4=option_button((640,580),'69',"#CCE5FF")
    
    q7o1=option_button((640,220),'Rocks',"#CCE5FF")
    q7o2=option_button((640,340),'Dust',"#CCE5FF")
    q7o3=option_button((640,460),'Ice',"#CCE5FF")
    q7o4=option_button((640,580),'All of the above',"#CCE5FF")
    
    q8o1=option_button((640,220),'25.6',"#CCE5FF")
    q8o2=option_button((640,340),'42',"#CCE5FF")
    q8o3=option_button((640,460),'26.5',"#CCE5FF")
    q8o4=option_button((640,580),'98',"#CCE5FF")
    
    q9o1=option_button((640,220),'Hydrogen',"#CCE5FF")
    q9o2=option_button((640,340),'Methane',"#CCE5FF")
    q9o3=option_button((640,460),'Distance from sun',"#CCE5FF")
    q9o4=option_button((640,580),'Rotation',"#CCE5FF")
    
    def s_sys():
        global sunb,merb,venb,earb,marb,jupb,satb,uranb,nepb
        while True:
            SCREEN.blit(QBG, (0, 0))
            clock.tick(1)
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            OPTIONS_BACK = Button(image=None, pos=(40,30), 
                            text_input="<--", font=get_font(40), base_color="White", hovering_color="Green")
        
            OPTIONS_BACK.changeColor(MENU_MOUSE_POS)
            OPTIONS_BACK.update(SCREEN)
            
            for button in [sun,HG, venus,earth,mars,a,jup,sat,ur,nep]:
                button.update(SCREEN)  
            OPTIONS_TEXT = get_font(50).render("Score:"+str(points), True, "White")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(1200, 30))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
            pygame.display.update()
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
#------------------------------------------------------------------------------
def show_user_name(user_name):
    while True:
        
        z=zc(user_name)
        
        bg= pygame.image.load("images c/"+z+".jpg")
      
        SCREEN.blit(bg,(0,0))    
        clock.tick(1)
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
      
        OPTIONS_BACK = Button(image=None, pos=(40,30), 
                            text_input="<--", font=get_font(40), base_color="White", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)  

        OPTIONS_TEXT = get_font(70).render(z, True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 400))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        pygame.display.update()
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):    
                    main_menu()
def get_date():
    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                
                
                show_user_name(event.text)
                
                
            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)

        

        manager.draw_ui(SCREEN)
        
        pygame.display.update()
        

def get_font(size): 
    return pygame.font.Font("assets/sfont.otf", size)

def solar_info():
    pygame.quit()
    sol_info() 
    main_menu()

def solar_quiz():
    global points
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))
        
        PLAY_TEXT = get_font(70).render("Quiz", True, "#B0E0E6")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        
        OPTIONS_TEXT = get_font(40).render("Please wait for the external window to show up", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 300))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(40,30), 
                            text_input="<--", font=get_font(40), base_color="White", hovering_color="Green")
        
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pygame.display.update()
        
        quiz()


def solarsystem():
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))
        
        INFO_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 500), 
                            text_input="Information and simulation", font=get_font(33), base_color="#68838B", hovering_color="White")
        QUIZ_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 300), 
                            text_input="Quiz", font=get_font(50), base_color="#68838B", hovering_color="White")        
        PLAY_TEXT = get_font(70).render("Solar system", True, "#B0E0E6")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(40, 30), 
                            text_input="<--", font=get_font(40), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        for button in [INFO_BUTTON, QUIZ_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(MOUSE_POS):
                    main_menu()
                if INFO_BUTTON.checkForInput(MOUSE_POS):
                    solar_info()
                if QUIZ_BUTTON.checkForInput(MOUSE_POS):
                    solar_quiz()

        pygame.display.update()
    
def blackhole():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))
        
        PLAY_TEXT = get_font(70).render("Black Hole", True, "#B0E0E6")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        
        OPTIONS_TEXT = get_font(40).render("Please wait for the external window to show up", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 300))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(40,30), 
                            text_input="<--", font=get_font(40), base_color="White", hovering_color="Green")
        
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pygame.display.update()
        
        bhgame()
        
        
        main_menu()
def constellations():
    
    while True:
        SCREEN.fill("#09051c")      
        OPTIONS_TEXT = get_font(40).render("Enter date of birth (Eg: july 04 , may 26, etc):", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        pygame.display.update()
        get_date()
        
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("SPACE", True, "#B0E0E6")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        SOLAR_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 550), 
                            text_input="Solar system", font=get_font(50), base_color="#68838B", hovering_color="White")
        BLACK_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 250), 
                            text_input="Black Holes", font=get_font(50), base_color="#68838B", hovering_color="White")
        CON_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="Constellations", font=get_font(50), base_color="#68838B", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [SOLAR_BUTTON, BLACK_BUTTON, CON_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SOLAR_BUTTON.checkForInput(MENU_MOUSE_POS):
                    solarsystem()
                if BLACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    blackhole()
                if CON_BUTTON.checkForInput(MENU_MOUSE_POS):
                    constellations()

        pygame.display.update()


main_menu()