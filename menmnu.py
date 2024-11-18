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