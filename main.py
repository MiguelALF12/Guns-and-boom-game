import pygame as pg
import os
from random import randint

import pygame.mixer

from MAPS.world import *
from MENU.menu import *
from PLAYER.player import *

#TODO: Retocar las animaciones de jump off y slide


pg.font.init()

# CONSTANTS, IMAGES AND GAME VARIABLES

# screen specs for menu

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("GUNS & BOOM")

CLOCK = pg.time.Clock()

SELECTION_FONT = pg.font.SysFont('comicsans', 45)
ITEMS_FONT = pg.font.SysFont('comicsans', 120)
LIFE_FONT = pg.font.SysFont('comicsans', 60)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# MENU IMAGES
INITIAL_INTERFACE = pg.image.load(os.path.join('SPRITES-INTERFACES-EFFECTS/INTERFACES/initial.png'))
MENU_INTERFACE = pg.image.load(os.path.join('SPRITES-INTERFACES-EFFECTS/INTERFACES/menu.png'))
CHOOSE_CHARACTER_INTERFACE = pg.image.load(os.path.join('SPRITES-INTERFACES-EFFECTS/INTERFACES/choose-character.png'))
CHOOSE_MAP_INTERFACE = pg.image.load(os.path.join('SPRITES-INTERFACES-EFFECTS/INTERFACES/choose-map.png'))
HELP_INTERFACE = pg.image.load(os.path.join('SPRITES-INTERFACES-EFFECTS/INTERFACES/help.png'))
CHOOSE_ITEMS_INTERFACE = pg.image.load(os.path.join('SPRITES-INTERFACES-EFFECTS/INTERFACES/choose_items.png'))
PAUSED_GAME_INTERFACE = pg.image.load(os.path.join('SPRITES-INTERFACES-EFFECTS/INTERFACES/gamePaused.png'))

# MAPS IMAGES
FOREST_WORLD_BACKGROUND = pg.image.load(os.path.join('SPRITES-INTERFACES-EFFECTS/MAPAS/MAPA #1/Map#1.png'))
ICE_WORLD_BACKGROUND = pg.image.load(os.path.join('SPRITES-INTERFACES-EFFECTS/MAPAS/MAPA #2/Map#2.png'))

#WIN IMAGES
PLAYER1_WINS = pg.image.load(os.path.join('SPRITES-INTERFACES-EFFECTS/INTERFACES/player1-win.png'))
PLAYER2_WINS = pg.image.load(os.path.join('SPRITES-INTERFACES-EFFECTS/INTERFACES/player2-win.png'))
BOTH_DIED = pg.image.load(os.path.join('SPRITES-INTERFACES-EFFECTS/INTERFACES/draw-win.png'))

#SOUND
controler = randint(0,2)
if controler == 0:
    MAP_SOUND = pygame.mixer.Sound( f'SPRITES-INTERFACES-EFFECTS/SOUND EFFECTS/Boss-Fight.wav' )
elif controler == 1:
    MAP_SOUND = pygame.mixer.Sound( f'SPRITES-INTERFACES-EFFECTS/SOUND EFFECTS/Common-Fight.wav' )
elif controler == 2:
    MAP_SOUND = pygame.mixer.Sound( f'SPRITES-INTERFACES-EFFECTS/SOUND EFFECTS/New-Hope.wav' )


# - FPS
FPS = 60

# PLAYERS, MAP
# CHOSEN PLAYERS
# [P1,P2]
CHOSEN_PLAYERS = [None, None]
MAP = [None, None]
POTIONS = [None, None]



# ------------------------------------------------------------------------------------------------------------------------
# Functions


def drawPlayerChoose(characterSelected, playerSelectionCounter):
    draw_text = SELECTION_FONT.render("PLAYER " + str(playerSelectionCounter), 1, WHITE)

    if characterSelected == "NINJA-MALE":
        SCREEN.blit(draw_text, (64, 558))
    elif characterSelected == "NINJA-FEMALE":
        SCREEN.blit(draw_text, (380, 555))
    elif characterSelected == "ROBOT":
        SCREEN.blit(draw_text, (692, 558))
    elif characterSelected == "ZOMBIE-FEMALE":
        SCREEN.blit(draw_text, (991, 553))

    pg.display.update()


def drawMapChoose(menuObject):
    menuObject.drawChooseMapInterface(SCREEN)
    mapName = ""
    coordinates = ()
    if MAP[1] == "FOREST":
        mapName = "FOREST"
        coordinates = (185, 509)
    elif MAP[1] == "ICE":
        mapName = "ICE"
        coordinates = (821, 509)
    draw_text = SELECTION_FONT.render(mapName, 1, WHITE)
    SCREEN.blit(draw_text, coordinates)


def drawItemChoose(option):
    global SCREEN

    coordinates = ()

    if option == "DAMAGE":
        coordinates = (254, 274)
    elif option == "LIFE":
        coordinates = (752, 274)

    draw_text_damage_potion = ITEMS_FONT.render('X', 1, BLACK)
    SCREEN.blit(draw_text_damage_potion, coordinates)


def confirmCharacterSelection(characterSelected, selectionsCounter, keys_pressed):
    if keys_pressed[0] and selectionsCounter == 1:  # Player 1 confirms its selection
        CHOSEN_PLAYERS[selectionsCounter - 1] = characterSelected
        return True
    if keys_pressed[1] and selectionsCounter == 2:  # Player 2 confirms its selection
        CHOSEN_PLAYERS[selectionsCounter - 1] = characterSelected
        return True

    return False


def isContinueButtonPressed(coordinate_x, coordinate_y):
    if 970 <= coordinate_x <= 1258 and 631 <= coordinate_y <= 700:
        print("CONTINUAR")
        return True
    else:
        return False


def isPressedGoBackButton(coordinates_x, coordinates_y):
    if 41 <= coordinates_x <= 158 and 34 <= coordinates_y <= 147:
        print("DEVOLVERSE")
        return True
    else:
        return False


def isGamePaused(coordinate_x, coordinate_y, world):
    if world == "FOREST":
        return True if 12 <= coordinate_x <= 71 and 12 <= coordinate_y <= 61 else False
    elif world == "ICE":
        return True if 6 <= coordinate_x <= 69 and 9 <= coordinate_y <= 63 else False


def handlePausedGame():
    global SCREEN
    run = True

    while run:
        SCREEN.blit(PAUSED_GAME_INTERFACE, (SCREEN_WIDTH/2-423, 100))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_y:
                    return False
                elif event.key == pg.K_n:
                    return True


def managePlaySection(menuObject):
    global CHOSEN_PLAYERS
    print("-SELECCIONAR PERSONAJE")
    menuObject.drawChooseCharacterInterface(SCREEN)
    run = True
    selectionsCounter = 1
    characterSelected = 0
    keys_pressed = []
    pageDirection = ""
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                coordinate_x, coordinate_y = event.pos
                if isPressedGoBackButton(coordinate_x, coordinate_y):
                    pageDirection = "MENU"
                    run = False
                else:
                    if isContinueButtonPressed(coordinate_x, coordinate_y):
                        if CHOSEN_PLAYERS[0] is not None and CHOSEN_PLAYERS[1] is not None:
                            pageDirection = "MAP"
                            run = False
                            print("Ya hay personajes seleccionados")
                        else:
                            print("No hay personajes seleccionados")
                        # else que indique que seleccione personaje
                    elif 36 <= coordinate_x <= 1248 and 215 <= coordinate_y <= 592:
                        if selectionsCounter <= 2:
                            # MALE-NINJA CHOSEN
                            if 54 <= coordinate_x <= 310 and 234 <= coordinate_y <= 580:
                                characterSelected = "NINJA-MALE"
                                # FEMALE-NINJA CHOSEN
                            elif 367 <= coordinate_x <= 624 and 238 <= coordinate_y <= 567:
                                characterSelected = "NINJA-FEMALE"
                                # ROBOT CHOSEN
                            elif 685 <= coordinate_x <= 920 and 241 <= coordinate_y <= 571:
                                characterSelected = "ROBOT"
                                # FEMALE-ZOMBIE CHOSEN
                            elif 981 <= coordinate_x <= 1222 and 237 <= coordinate_y <= 575:
                                characterSelected = "ZOMBIE-FEMALE"
            if event.type == pg.KEYDOWN:
                keys_pressed.append(pg.key.get_pressed()[pg.K_LALT])
                keys_pressed.append(pg.key.get_pressed()[pg.K_RALT])
                print(confirmCharacterSelection(characterSelected, selectionsCounter, keys_pressed), selectionsCounter)
                # TODO: Mejorar la forma de sleección,
                # Si presiona nuevamente una tecla cuando ya hay jugadores seleccionados, determinar la tecla presionada y cambiar según la selección
                if confirmCharacterSelection(characterSelected, selectionsCounter, keys_pressed):
                    drawPlayerChoose(characterSelected, selectionsCounter)  # Indica la selección ya confirmada
                    selectionsCounter += 1
                    characterSelected = 0
            keys_pressed = []
        pg.display.update()
    if pageDirection == "MENU":
        manageMenu(menuObject)
    elif pageDirection == "MAP":
        print("CHOSEN_PLAYERS -> ",CHOSEN_PLAYERS)
        manageMapSelection(menuObject)


def manageMapSelection(menuObject):
    global SCREEN,MAP
    print("-SELECCIONAR MAPA")
    menuObject.drawChooseMapInterface(SCREEN)
    run = True
    pageDirection = ""
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                coordinate_x, coordinate_y = event.pos
                if isPressedGoBackButton(coordinate_x, coordinate_y):
                    pageDirection = "CHARACTER"
                    run = False
                else:
                    if isContinueButtonPressed(coordinate_x, coordinate_y):
                        if MAP[0] is not None:
                            pageDirection = "ITEMS"
                            run = False
                        # else que indique que seleccione personaje
                    elif 40 <= coordinate_x <= 1230 and 220 <= coordinate_y <= 547:
                        # FOREST
                        if 40 <= coordinate_x <= 606 and 220 <= coordinate_y <= 547:
                            MAP = [FOREST_WORLD_BACKGROUND, "FOREST"]
                        # ICE
                        elif 664 <= coordinate_x <= 1230 and 220 <= coordinate_y <= 547:
                            MAP = [ICE_WORLD_BACKGROUND, "ICE"]
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RSHIFT and MAP is not None:
                    print("mapa seleccionado")
                    drawMapChoose(menuObject)
        pg.display.update()
    if pageDirection == "ITEMS":
        print("MAP -> ",MAP)
        manageItemsSelection(menuObject)
    elif pageDirection == "CHARACTER":
        managePlaySection(menuObject)


def manageItemsSelection(menuObject):
    global SCREEN, POTIONS
    print("-SELECCIONAR ITEMS")
    menuObject.drawItemsInterface(SCREEN)
    run = True
    pageDirection = ""
    option = ""
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                coordinate_x, coordinate_y = event.pos
                if isPressedGoBackButton(coordinate_x, coordinate_y):
                    pageDirection = "MAPAS"
                    run = False
                else:
                    if isContinueButtonPressed(coordinate_x, coordinate_y):
                        # if POTIONS[0] is not None or POTIONS[1] is not None:
                        print(POTIONS)
                        pageDirection = "PLAY"
                        run = False
                        print("Puede o no haber items seleccionados")
                    else:
                        # DANO
                        if 256 <= coordinate_x <= 489 and 523 <= coordinate_y <= 582:
                            POTIONS[0] = 1
                            option = "DAMAGE"
                        # VIDA
                        elif 749 <= coordinate_x <= 982 and 523 <= coordinate_y <= 582:
                            POTIONS[1] = 1
                            option = "LIFE"
                        # reset
                        elif 521 <= coordinate_x <= 700 and 347 <= coordinate_y <= 406:
                            POTIONS = [None, None]
                            menuObject.drawItemsInterface(SCREEN)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RSHIFT and MAP is not None:
                    print(f"POCION DE {option} SELECCIONADA")
                    drawItemChoose(option)
        pg.display.update()
    if pageDirection == "MAPAS":
        manageMapSelection(menuObject)
    elif pageDirection == "PLAY":
        print("POTIONS -> ",POTIONS)
        launchGame(menuObject)

def winnerExists(player1, player2):
    if player1.getLife() == 0 and player2.getLife() > 0:
        return (True, PLAYER2_WINS)
    elif player1.getLife() > 0  and player2.getLife() == 0:
        return (True, PLAYER1_WINS)
    elif player1.getLife() == 0 and player2.getLife() == 0:
        return (True, BOTH_DIED)
    else:
        return (False, 0)

def drawWinner(winner_image):

    global SCREEN
    run = True

    while run:
        SCREEN.blit(winner_image, (SCREEN_WIDTH / 2 - 423, 100))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_y:
                    return False

def launchGame(menuObject):
    global SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, CHOSEN_PLAYERS, MAP, POTIONS

    print("-CARGANDO PARTIDA")

    # creating player

    player1 = Player(0, 360, CHOSEN_PLAYERS[0], "WASD")
    player2 = Player(1200, 360, CHOSEN_PLAYERS[1], "ULDR")  # Up, Left,Down,Right

    # Creating worlds
    print(MAP)
    chosen_map = World(MAP[0], MAP[1])

    # test
    # forest_world = World(FOREST_WORLD_BACKGROUND,"FOREST")
    # ice_world = World(ICE_WORLD_BACKGROUND,"ICE")

    run = True
    wantGoMenu = False
    pygame.mixer.Sound.play(MAP_SOUND)
    while run:
        CLOCK.tick(FPS)
        chosen_map.drawBackground(SCREEN)
        chosen_map.draw_collision_objects(SCREEN, chosen_map.getWorldName())
        # player1.update(SCREEN, SCREEN_WIDTH,SCREEN_HEIGHT, chosen_map.getCollisionsObjects(), chosen_map.getWorldName(), player2.getPlayerRectangle(), player2.getCharacter())
        # player2.update(SCREEN,SCREEN_WIDTH,SCREEN_HEIGHT , chosen_map.getCollisionsObjects(), chosen_map.getWorldName(), player1.getPlayerRectangle(), player1.getCharacter())
        player1.update(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, chosen_map.getCollisionsObjects(),
                       chosen_map.getWorldName(), player2)
        player2.update(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, chosen_map.getCollisionsObjects(),
                       chosen_map.getWorldName(), player1)
        player1.drawLife(SCREEN, LIFE_FONT, WHITE)
        player2.drawLife(SCREEN, LIFE_FONT, WHITE)

        # test
        # forest_world.drawBackground(SCREEN)
        # forest_world.draw_collision_objects(SCREEN, "FOREST")
        # ice_world.drawBackground(SCREEN)
        # ice_world.draw_collision_objects(SCREEN, "ICE")

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                coordinate_x, coordinate_y = event.pos
                if isGamePaused(coordinate_x, coordinate_y, chosen_map.getWorldName()):
                    print("LA PARTIDA SE HA PAUSADO")
                    run = handlePausedGame()
                    wantGoMenu = not run

        winner = winnerExists(player1, player2)
        if winner[0]:
            run = drawWinner(winner[1])
            wantGoMenu = not run

        pg.display.set_caption(str(int(CLOCK.get_fps())))
        pg.display.update()

        # drawWinner(player1,player2)

    if wantGoMenu:
        POTIONS = [None,None]
        CHOSEN_PLAYERS = [None, None]
        MAP = [None,None]
        pygame.mixer.Sound.stop(MAP_SOUND)
        manageMenu(menuObject)


def manageHelp(menuObject):
    print("AYUDA")
    menuObject.drawHelpInterface(SCREEN)
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                coordinate_x, coordinate_y = event.pos
                if isPressedGoBackButton(coordinate_x, coordinate_y):
                    menu.drawMenuInterface(SCREEN)
                    run = False
        pg.display.update()


def manageMenu(menuObject):
    menuObject.drawMenuInterface(SCREEN)
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                coordinate_x, coordinate_y = event.pos
                if 55 <= coordinate_x <= 387 and 176 <= coordinate_y <= 359:
                    print("SELECCIONAR PERSONAJE y MAPA")
                    managePlaySection(menuObject)
                elif 474 <= coordinate_x <= 808 and 303 <= coordinate_y <= 488:
                    manageHelp(menuObject)
                elif 879 <= coordinate_x <= 1204 and 494 <= coordinate_y <= 667:
                    print("SALIENDO")
                    exit()
        pg.display.update()


# ------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    menu = Menu(INITIAL_INTERFACE, MENU_INTERFACE, CHOOSE_CHARACTER_INTERFACE, CHOOSE_MAP_INTERFACE,
                CHOOSE_ITEMS_INTERFACE, HELP_INTERFACE)
    run = True

    menu.drawInitialInterface(SCREEN)
    menu.drawMenuInterface(SCREEN)

    while run:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
            manageMenu(menu)
            # launchGame(menu)

        pg.display.update()
