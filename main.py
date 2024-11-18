import pygame, pygame_gui, sys
from buttons import Button
from ccode import zc
from blackhole import bhgame
from quiz import *

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
manager = pygame_gui.UIManager((1280, 720))

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((330, 300), (600, 50)), manager=manager,object_id='#main_text_entry')

clock = pygame.time.Clock()
WIDTH, HEIGHT = 1280, 720

def show_user_name(user_name):
    while True:
        z=zc(user_name)
        
        bg= pygame.image.load("images c/"+z+".jpg")
        
        
        SCREEN.blit(bg,(0,0))
        pygame.display.flip()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        
        
        
        OPTIONS_BACK = Button(image=None, pos=(40,30), 
                            text_input="<--", font=get_font(40), base_color="White", hovering_color="Green")
        
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        
        OPTIONS_BACK.update(SCREEN)
        
        OPTIONS_TEXT = get_font(70).render(z, True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 400))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    
                    
                    main_menu()
                    
        
        pygame.display.update()

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
    print('hi')
    
def solar_quiz():
    s_sys()
    main_menu()


def solarsystem():
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))
        
        INFO_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 300), 
                            text_input="Information and simulation", font=get_font(33), base_color="#68838B", hovering_color="White")
        QUIZ_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 500), 
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
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("#09051c")
        
        OPTIONS_TEXT = get_font(40).render("Enter date of birth (Eg: july 04 , may 26, etc..):", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        OPTIONS_BACK = Button(image=None, pos=(40,30), 
                            text_input="<--", font=get_font(40), base_color="White", hovering_color="Green")
        
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        
        OPTIONS_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                    
                
        
        pygame.display.update()
        get_date()
        
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("SPACE", True, "#B0E0E6")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        SOLAR_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 250), 
                            text_input="Solar system", font=get_font(50), base_color="#68838B", hovering_color="White")
        BLACK_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="Black Holes", font=get_font(50), base_color="#68838B", hovering_color="White")
        CON_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 550), 
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