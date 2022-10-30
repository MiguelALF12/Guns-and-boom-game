import pygame


class World:

    def __init__(self, background, name):
        self.background = background
        self.collisions_objects_list = []
        self.name = name

    def getBackground(self):
        return self.background

    def getCollisionsObjects(self):
        return self.collisions_objects_list

    def getWorldName(self):
        return self.name

    def setCollisionsObjects(self, newCollisionsObjectsList):
        self.collisions_objects_list = newCollisionsObjectsList

    def drawBackground(self, screen):
        screen.blit(self.getBackground(), (0, 0))

    def draw_collision_objects(self, screen, mapType):
        if mapType == "FOREST":
            FOREST_OBJECT_COLLISION_1 = pygame.Rect(0, 608, 488, 111)
            # pygame.draw.rect(screen, (0, 0, 0), FOREST_OBJECT_COLLISION_1)
            FOREST_OBJECT_COLLISION_2 = pygame.Rect(259, 363, 315, 77)
            # pygame.draw.rect(screen, (0, 0, 0), FOREST_OBJECT_COLLISION_2)
            FOREST_OBJECT_COLLISION_3 = pygame.Rect(646, 563, 108, 156)
            # pygame.draw.rect(screen, (0, 0, 0), FOREST_OBJECT_COLLISION_3)
            FOREST_OBJECT_COLLISION_4 = pygame.Rect(823, 608, 457, 111)
            # pygame.draw.rect(screen, (0, 0, 0), FOREST_OBJECT_COLLISION_4)
            self.setCollisionsObjects([FOREST_OBJECT_COLLISION_1, FOREST_OBJECT_COLLISION_2, FOREST_OBJECT_COLLISION_3,
                                       FOREST_OBJECT_COLLISION_4])
        if mapType == "ICE":
            ICE_OBJECT_COLLISION_1 = pygame.Rect(0, 339, 142, 86)
            # pygame.draw.rect(screen, (0, 0, 0), ICE_OBJECT_COLLISION_1)
            ICE_OBJECT_COLLISION_2 = pygame.Rect(213, 546, 431, 171)
            # pygame.draw.rect(screen, (0, 0, 0), ICE_OBJECT_COLLISION_2)
            ICE_OBJECT_COLLISION_3 = pygame.Rect(752, 362, 150, 149)
            # pygame.draw.rect(screen, (0, 0, 0), ICE_OBJECT_COLLISION_3)
            ICE_OBJECT_COLLISION_4 = pygame.Rect(1015, 443, 263, 275)
            # pygame.draw.rect(screen, (0, 0, 0), ICE_OBJECT_COLLISION_4)
            ICE_OBJECT_COLLISION_5 = pygame.Rect(1153, 183, 126, 74)
            # pygame.draw.rect(screen, (0, 0, 0), ICE_OBJECT_COLLISION_5)
            self.setCollisionsObjects([ICE_OBJECT_COLLISION_1, ICE_OBJECT_COLLISION_2, ICE_OBJECT_COLLISION_3,
                                       ICE_OBJECT_COLLISION_4, ICE_OBJECT_COLLISION_5])


