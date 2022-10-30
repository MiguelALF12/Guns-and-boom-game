import time

import pygame


class Menu:
    def __init__(self, initial, menu, choose_character, choose_map, items, help):
        self.initial_interface = initial
        self.menu_interface = menu
        self.choose_character_interface = choose_character
        self.choose_map_interface = choose_map
        self.items_interface = items
        self.help_interface = help

    def getInitialInterface(self):
        return self.initial_interface

    def getMenuInterface(self):
        return self.menu_interface

    def getChooseCharacterInterface(self):
        return self.choose_character_interface

    def getChooseMapInterface(self):
        return self.choose_map_interface

    def getItemsInterface(self):
        return self.items_interface

    def getHelpInterface(self):
        return self.help_interface

    def drawInitialInterface(self, screen):
        screen.blit(self.getInitialInterface(), (0, 0))
        pygame.display.update()
        time.sleep(5)

    def drawMenuInterface(self, screen):
        screen.blit(self.getMenuInterface(), (0, 0))
        pygame.display.update()

    def drawChooseCharacterInterface(self, screen):
        screen.blit(self.getChooseCharacterInterface(), (0, 0))
        pygame.display.update()

    def drawChooseMapInterface(self, screen):
        screen.blit(self.getChooseMapInterface(), (0, 0))
        pygame.display.update()

    def drawItemsInterface(self, screen):
        screen.blit(self.getItemsInterface(), (0, 0))
        pygame.display.update()

    def drawHelpInterface(self, screen):
        screen.blit(self.help_interface, (0, 0))
        pygame.display.update()

