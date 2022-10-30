import pygame

pygame.mixer.init()

class Player:
    # Hitted bulet event
    PLAYER_HIT = pygame.USEREVENT + 1
    MAX_BULLETS = 1
    ROBOT_BULLET_HIT_SOUND = pygame.mixer.Sound('SPRITES-INTERFACES-EFFECTS/SOUND EFFECTS/ROBOT-laser-effect.wav')
    NINJAS_ZOMBIES_WAVE_HIT_SOUND = pygame.mixer.Sound('SPRITES-INTERFACES-EFFECTS/SOUND EFFECTS/NINJASZOMBIE-wave-effect.wav')
    NINJA_BOY_GIRL_KUNAI_HIT_SOUND = pygame.mixer.Sound('SPRITES-INTERFACES-EFFECTS/SOUND EFFECTS/NINJAS-kunai-effect.wav')

    def __init__(self, coordinate_x, coordinate_y, character, player_type):

        self.index = 0
        self.counter = 0
        self.character = character
        self.player_type = player_type

        # movement animations
        self.animation_idle = []
        self.animation_jump_on = []
        self.animation_jump_off = []
        self.animation_run_right = []
        self.animation_run_left = []
        self.animation_slide = []

        # attack animations
        self.ninja_BG_animation_attack_right = {'ATTACK': [], 'JUMP_ATTACK': [], 'RUN_ATTACK': []}
        self.ninja_BG_animation_attack_left = {'ATTACK': [], 'JUMP_ATTACK': [], 'RUN_ATTACK': []}
        self.robot_animation_attack_right = {'JUMP_ATTACK': [], 'RUN_ATTACK': [], 'ATTACK': []}
        self.robot_animation_attack_left = {'JUMP_ATTACK': [], 'RUN_ATTACK': [], 'ATTACK': []}
        self.zombie_animation_attack_right = []
        self.zombie_animation_attack_left = []

        ninja_character_tag = ""
        image_idle_right = 0
        image_jump_on_right = None
        image_jump_on_left = None
        image_jump_off_right = None
        image_jump_off_left = None
        image_slide_right = None
        image_slide_left = None

        # Loading animation images deending on the selected character
        if self.character == "NINJA-MALE" or self.character == "NINJA-FEMALE":
            if self.character == "NINJA-MALE":
                ninja_character_tag = "NINJA_BOY"
            elif self.character == "NINJA-FEMALE":
                ninja_character_tag = "NINJA_GIRL"

            image_idle_right = pygame.image.load(
                f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/{ninja_character_tag}/sprites/Idle__001.png')
            image_jump_on_right = pygame.image.load(
                f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/{ninja_character_tag}/sprites/Jump__006.png')
            image_jump_off_right = pygame.image.load(
                f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/{ninja_character_tag}/sprites/Glide_006.png')
            image_slide_right = pygame.image.load(
                f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/{ninja_character_tag}/sprites/Slide__000.png')

            # Loading RUN animations
            for image in range(0, 10):
                # images for RUN right and left
                image_run_right = pygame.image.load(
                    f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/{ninja_character_tag}/sprites/Run__00{image}.png')

                image_run_right = pygame.transform.scale(image_run_right, (120, 120))
                image_run_left = pygame.transform.flip(image_run_right, True, False)
                self.animation_run_right.append(image_run_right)
                self.animation_run_left.append(image_run_left)

                # Loading RUN animation into RUNNING_ATTACK due to no existance of this type of animation for NINJA_MALE_FEMALE
                self.ninja_BG_animation_attack_right['RUN_ATTACK'].append(image_run_right)
                self.ninja_BG_animation_attack_left['RUN_ATTACK'].append(image_run_left)

            # Loading ATTACK animations
            for image in range(0, 10):
                # loading ATTACK images
                image_attack_right = pygame.image.load(
                    f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/{ninja_character_tag}/sprites/Attack__00{image}.png')
                # loading JUMP_THROW
                image_jumpThrow_right = pygame.image.load(
                    f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/{ninja_character_tag}/sprites/Jump_Throw__00{image}.png')

                image_attack_right = pygame.transform.scale(image_attack_right, (170, 140))
                image_attack_left = pygame.transform.flip(image_attack_right, True, False)

                image_jumpThrow_right = pygame.transform.scale(image_jumpThrow_right, (120, 120))
                image_jumpThrow_left = pygame.transform.flip(image_jumpThrow_right, True, False)

                self.ninja_BG_animation_attack_right['ATTACK'].append(image_attack_right)
                self.ninja_BG_animation_attack_left['ATTACK'].append(image_attack_left)
                self.ninja_BG_animation_attack_right['JUMP_ATTACK'].append(image_jumpThrow_right)
                self.ninja_BG_animation_attack_left['JUMP_ATTACK'].append(image_jumpThrow_left)

        elif self.character == "ROBOT":
            image_idle_right = pygame.image.load(
                f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/ROBOT/sprites/Idle (1).png')
            image_jump_on_right = pygame.image.load(
                f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/ROBOT/sprites/Jump (2).png')
            image_jump_off_right = pygame.image.load(
                'SPRITES-INTERFACES-EFFECTS/CHARACTERS/ROBOT/sprites/Jump (7).png')
            image_slide_right = pygame.image.load(
                f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/ROBOT/sprites/Slide (1).png')

            # Loading RUN animation
            for image in range(1, 9):
                # images for RUN right and left
                image_run_right = pygame.image.load(
                    f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/ROBOT/sprites/Run ({image}).png')
                image_run_right = pygame.transform.scale(image_run_right, (120, 120))
                image_run_left = pygame.transform.flip(image_run_right, True, False)
                self.animation_run_right.append(image_run_right)
                self.animation_run_left.append(image_run_left)
            # loading ATTACK animations
            # loading JumpShot
            for image in range(1, 6):
                image_jumpShot_right = pygame.image.load(
                    f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/ROBOT/sprites/JumpShoot ({image}).png')
                image_jumpShot_right = pygame.transform.scale(image_jumpShot_right, (120, 120))
                image_jumpShot_left = pygame.transform.flip(image_jumpShot_right, True, False)
                self.robot_animation_attack_right['JUMP_ATTACK'].append(image_jumpShot_right)
                self.robot_animation_attack_left['JUMP_ATTACK'].append(image_jumpShot_left)
            # loading RunShot
            for image in range(1, 10):
                image_runShot_right = pygame.image.load(
                    f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/ROBOT/sprites/RunShoot ({image}).png')
                image_runShot_right = pygame.transform.scale(image_runShot_right, (120, 120))
                image_runShot_left = pygame.transform.flip(image_runShot_right, True, False)
                self.robot_animation_attack_right['RUN_ATTACK'].append(image_runShot_right)
                self.robot_animation_attack_left['RUN_ATTACK'].append(image_runShot_left)
            # loading Shoot
            for image in range(1, 5):
                image_Shoot_right = pygame.image.load(
                    f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/ROBOT/sprites/Shoot ({image}).png')
                image_Shoot_right = pygame.transform.scale(image_Shoot_right, (150, 150))
                image_Shoot_left = pygame.transform.flip(image_Shoot_right, True, False)
                self.robot_animation_attack_right['ATTACK'].append(image_Shoot_right)
                self.robot_animation_attack_left['ATTACK'].append(image_Shoot_left)

        elif self.character == "ZOMBIE-FEMALE":
            image_idle_right = pygame.image.load(
                f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/ZOMBIE/sprites/female/Idle (1).png')
            image_slide_right = pygame.image.load(
                f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/ZOMBIE/sprites/female/Dead (12).png')
            # Loading RUN attack
            for image in range(1, 11):
                # images for RUN right and left
                image_run_right = pygame.image.load(
                    f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/ZOMBIE/sprites/female/Walk ({image}).png')
                image_run_right = pygame.transform.scale(image_run_right, (120, 120))
                image_run_left = pygame.transform.flip(image_run_right, True, False)
                self.animation_run_left.append(image_run_left)
                self.animation_run_right.append(image_run_right)

            # Loading ATTACK animation
            for image in range(1, 9):
                # images for RUN right and left
                image_attack_right = pygame.image.load(
                    f'SPRITES-INTERFACES-EFFECTS/CHARACTERS/ZOMBIE/sprites/female/Attack ({image}).png')
                image_attack_right = pygame.transform.scale(image_attack_right, (120, 120))
                image_attack_left = pygame.transform.flip(image_attack_right, True, False)
                self.zombie_animation_attack_right.append(image_attack_right)
                self.zombie_animation_attack_left.append(image_attack_left)

        # Flipping the orientation
        # idle

        image_idle_right = pygame.transform.scale(image_idle_right, (120, 120))
        image_idle_left = pygame.transform.flip(image_idle_right, True, False)
        # Slide
        image_slide_right = pygame.transform.scale(image_slide_right, (120, 120))
        image_slide_left = pygame.transform.flip(image_slide_right, True, False)

        if self.character != "ZOMBIE-FEMALE":
            image_jump_on_right = pygame.transform.scale(image_jump_on_right, (120, 120))
            image_jump_on_left = pygame.transform.flip(image_jump_on_right, True, False)
            image_jump_off_right = pygame.transform.scale(image_jump_off_right, (120, 120))
            image_jump_off_left = pygame.transform.flip(image_jump_off_right, True, False)

        self.animation_idle = [image_idle_right, image_idle_left]
        self.animation_jump_on = [image_jump_on_right, image_jump_on_left]
        self.animation_jump_off = [image_jump_off_right, image_jump_off_left]
        self.animation_slide = [image_slide_right, image_slide_left]

        self.image = self.animation_idle[0]  # default animation
        self.player_rect = self.image.get_rect()
        self.player_rect.x = coordinate_x
        self.player_rect.y = coordinate_y
        self.spawn_coordinates_X = coordinate_x
        self.spawn_coordinates_Y = coordinate_y
        self.yVelocity = 0
        self.jumped = False
        self.life = 200
        self.status = ""  # indicates whenever the player is RUNNING, SLIDIG, JUMPING OFF
        self.direction = [0, 0]  # [x,y]

        # for Bullets
        self.ninjaBullets = []
        self.robotBullets = []
        self.zombieBullets = []

    def getAnimationIndex(self):
        return self.index

    def getAnimationCounter(self):
        return self.counter

    def getAnimationDirection(self):
        return self.direction

    def getCharacter(self):
        return self.character

    def getPlayerType(self):
        return self.player_type

    def getAnimationList(self, animation, orientation):
        # Animation can possibly be -> IDLE, JUMP, RUN, GLIDE ...
        # Can be added more if we decide
        # Orientation can possibly be -> RIGHT, LEFT
        if animation == "IDLE":
            if orientation == "RIGHT":
                return self.animation_idle[0]
            elif orientation == "LEFT":
                return self.animation_idle[1]
        elif animation == "RUN":
            if orientation == "RIGHT":
                return self.animation_run_right
            elif orientation == "LEFT":
                return self.animation_run_left
        elif animation == "JUMP ON":
            if orientation == "RIGHT":
                return self.animation_jump_on[0]
            elif orientation == "LEFT":
                return self.animation_jump_on[1]
        elif animation == "JUMP OFF":
            if orientation == "RIGHT":
                return self.animation_jump_off[0]
            elif orientation == "LEFT":
                return self.animation_jump_off[1]
            elif orientation == "BOTH":
                return self.animation_jump_off
        elif animation == "SLIDE":
            if orientation == "RIGHT":
                return self.animation_slide[0]
            elif orientation == "LEFT":
                return self.animation_slide[1]
            elif orientation == "BOTH":
                return self.animation_slide

    def getAnimationAttackList(self, animation, orientation):
        # 'ATTACK-LEFT', 'JUMP_ATTACK-LEFT', 'RUN_ATTACK-LEFT'
        if animation in ['ATTACK', 'JUMP_ATTACK', 'RUN_ATTACK']:
            if self.getCharacter() == "NINJA-MALE" or self.getCharacter() == "NINJA-FEMALE":
                if orientation == "RIGHT":
                    return self.ninja_BG_animation_attack_right[animation]
                elif orientation == "LEFT":
                    return self.ninja_BG_animation_attack_left[animation]
            elif self.getCharacter() == "ROBOT":
                if orientation == "RIGHT":
                    return self.robot_animation_attack_right[animation]
                elif orientation == "LEFT":
                    return self.robot_animation_attack_left[animation]
            elif self.getCharacter() == "ZOMBIE-FEMALE":
                if orientation == "RIGHT":
                    return self.zombie_animation_attack_right
                elif orientation == "LEFT":
                    return self.zombie_animation_attack_left

    def getStatus(self):
        return self.status

    def getPlayerImage(self):
        return self.image

    def getPlayerRectangle(self):
        return self.player_rect

    def getCoordinateX(self):
        return self.player_rect.x

    def getCoordinateY(self):
        return self.player_rect.y

    def getSpawnCoordinatesX(self):
        return self.spawn_coordinates_X

    def getSpawnCoordinatesY(self):
        return self.spawn_coordinates_Y

    def getYvelocity(self):
        return self.yVelocity

    def getJumped(self):
        return self.jumped

    def getBullets(self):
        if self.getCharacter() == "NINJA-MALE" or self.getCharacter() == "NINJA-FEMALE":
            return self.ninjaBullets
        elif self.getCharacter() == "ROBOT":
            return self.robotBullets
        elif self.getCharacter() == "ZOMBIE-FEMALE":
            return self.zombieBullets

    def getLife(self):
        return self.life

    def setStatus(self, new_status):
        self.status = new_status

    def setCoordinateX(self, new_coordinate_X):
        self.player_rect.x = new_coordinate_X

    def setCoordinateY(self, new_coordinate_Y):
        self.player_rect.y = new_coordinate_Y

    def setYvelocity(self, new_y_velocity):
        self.yVelocity = new_y_velocity

    def setJumped(self, new_jumped):
        self.jumped = new_jumped

    def setPlayerImage(self, new_image):
        self.image = new_image

    def setAnimationIndex(self, new_index):
        self.index = new_index

    def setAnimationCounter(self, new_counter):
        self.counter = new_counter

    def setAnimationDirection(self, new_direction, axis):
        if axis == 'X':
            self.direction[0] = new_direction
        elif axis == 'Y':
            self.direction[1] = new_direction

    def setLife(self, new_life):
        self.life = new_life

    def isPlayerOutsideBoundaries(self, screen_height):

        if self.getPlayerRectangle().bottom > screen_height:  # Set boundaries just when the player falls
            self.setCoordinateX(self.getSpawnCoordinatesX())
            self.setCoordinateY(self.getSpawnCoordinatesY())

            # setting life
            fallDamage = 30
            currentLife = self.getLife() - fallDamage
            self.setLife(currentLife)

    def createNinjaBullet(self):
        bullet_image = pygame.image.load('SPRITES-INTERFACES-EFFECTS/CHARACTERS/NINJA_BOY/objects/ninjaB_bullet.png')
        kunai_image = pygame.image.load("SPRITES-INTERFACES-EFFECTS/CHARACTERS/NINJA_BOY/sprites/Kunai.png")
        bullet_image = pygame.transform.scale(bullet_image, (50, 50))
        kunai_image = pygame.transform.scale(kunai_image, (80, 17))
        return (bullet_image, kunai_image)

    def createRobotBullet(self):
        bullet_image = pygame.image.load("SPRITES-INTERFACES-EFFECTS/CHARACTERS/ROBOT/sprites/Objects/Bullet_000.png")
        bullet_image = pygame.transform.scale(bullet_image, (50, 50))
        return bullet_image

    def createZombieBullet(self):
        bullet_image = pygame.image.load('SPRITES-INTERFACES-EFFECTS/CHARACTERS/ZOMBIE/sprites/objects/bullet_zombie.png')
        bullet_image = pygame.transform.scale(bullet_image, (50, 50))
        return bullet_image

    def rotateBullet(self, bullet_surface, direction):
        if direction == -1:  # LEFT
            bullet_surface = pygame.transform.rotate(bullet_surface, 180)
        return bullet_surface

    def manageBulletSpeed(self, bulletProperties):
        # type
        if self.getCharacter() == "NINJA-MALE" or self.getCharacter() == "NINJA-FEMALE":
            if bulletProperties[0] == "KUNAI":
                if bulletProperties[3] == -1:  # LEFT
                    bulletProperties[2].x -= 23
                elif bulletProperties[3] == 1:  # RIGHT
                    bulletProperties[2].x += 23
            elif bulletProperties[0] == "SWORD_WAVE":
                if bulletProperties[3] == -1:  # LEFT
                    # 270
                    bulletProperties[2].x -= 23
                elif bulletProperties[3] == 1:  # RIGHT
                    # 90
                    bulletProperties[2].x += 23
        if self.getCharacter() == "ROBOT" or self.getCharacter() == "ZOMBIE-FEMALE":
            if bulletProperties[3] == -1:  # LEFT
                bulletProperties[2].x -= 23
            elif bulletProperties[3] == 1:  # RIGHT
                bulletProperties[2].x += 23
        return bulletProperties

    def handleBulletCreation(self):

        # setting spawn coordinates for bullets
        set_x = 0
        set_y = 0
        if self.getPlayerType() == "WASD":
            set_x = self.getPlayerRectangle().x + 125
            set_y = self.getPlayerRectangle().y + 60
        elif self.getPlayerType() == "ULDR":
            set_x = self.getPlayerRectangle().x - 5
            set_y = self.getPlayerRectangle().y + 60

        if self.getCharacter() == "NINJA-MALE" or self.getCharacter() == "NINJA-FEMALE":
            bullet_type = ""
            if self.getStatus() == "ATTACK-STILL":
                bullet_type = "SWORD_WAVE"
            elif self.getStatus() == "ATTACK-JUMPING" or self.getStatus() == "ATTACK-RUNNING":
                bullet_type = "KUNAI"
            if len(self.getBullets()) < Player.MAX_BULLETS:
                bullet = self.createNinjaBullet()[0]
                kunai = self.createNinjaBullet()[1]
                bullet = self.rotateBullet(bullet, self.getAnimationDirection()[0])
                kunai = self.rotateBullet(kunai, self.getAnimationDirection()[0])

                if bullet_type == "KUNAI":
                    bulletKunai_object_rectangle = kunai.get_rect()
                    bulletKunai_object_rectangle.x = set_x
                    bulletKunai_object_rectangle.y = set_y
                    self.getBullets().append(
                        [bullet_type, kunai, bulletKunai_object_rectangle, self.getAnimationDirection()[0]])
                elif bullet_type == "SWORD_WAVE":  # type       #surface    #rectangle      #direction       #playerRectangle
                    bulletKunai_object_rectangle = bullet.get_rect()
                    bulletKunai_object_rectangle.x = set_x
                    bulletKunai_object_rectangle.y = set_y
                    self.getBullets().append(
                        [bullet_type, bullet, bulletKunai_object_rectangle, self.getAnimationDirection()[0]])
        if self.getCharacter() == "ROBOT":
            if len(self.getBullets()) < Player.MAX_BULLETS:
                bullet = self.createRobotBullet()
                # this will change the direction if it is guided to left, otherwise it will keep the default direction
                bullet = self.rotateBullet(bullet, self.getAnimationDirection()[0])
                robot_object_rectangle = bullet.get_rect()
                robot_object_rectangle.x = set_x
                robot_object_rectangle.y = set_y
                self.getBullets().append(["LASER", bullet, robot_object_rectangle, self.getAnimationDirection()[0]])
        if self.getCharacter() == "ZOMBIE-FEMALE":
            if len(self.getBullets()) < Player.MAX_BULLETS:
                bullet = self.createZombieBullet()
                # this will change the direction if it is guided to left, otherwise it will keep the default direction
                bullet = self.rotateBullet(bullet, self.getAnimationDirection()[0])
                zombie_object_rectangle = bullet.get_rect()
                zombie_object_rectangle.x = set_x
                zombie_object_rectangle.y = set_y
                self.getBullets().append(
                    ["SWORD-WAVE", bullet, zombie_object_rectangle, self.getAnimationDirection()[0]])

    def handleBulletsMovement(self, screen_width, second_player, collisionObjects, ):
        if len(self.getBullets()) != 0:
            for bulletProperties in self.getBullets():
                bulletProperties = self.manageBulletSpeed(bulletProperties)
                if bulletProperties[2].x > screen_width or bulletProperties[2].x < 0:
                    self.getBullets().remove(bulletProperties)
                if bulletProperties[2].colliderect(second_player.getPlayerRectangle()):
                    pygame.event.post(pygame.event.Event(Player.PLAYER_HIT))
                    self.getBullets().remove(bulletProperties)
                    # setting life
                    hitDamage = 20
                    currentLife = second_player.getLife() - hitDamage
                    second_player.setLife(currentLife)
                # checking for collissions with objects
                for collisionObject in collisionObjects:
                    if bulletProperties[2].colliderect(collisionObject):
                        self.getBullets().remove(bulletProperties)

    def drawBullets(self, screen):
        for bulletProperties in self.getBullets():
            screen.blit(bulletProperties[1], bulletProperties[2])
            # pygame.draw.rect(screen, (0,0,0), bulletProperties[2],width=2)

    def drawLife(self, screen, font, color):
        if self.getLife() <= 0:
            self.setLife(0)
        if self.getPlayerType() == "ULDR":
            text = font.render(f'P2:{self.getLife()}%', True, color)
            screen.blit(text, (660, 0))
        if self.getPlayerType() == "WASD":
            text = font.render(f'P1:{self.getLife()}%', True, color)
            screen.blit(text, (300, 0))

    def update(self, screen, screen_width, screen_height, collisions_objects, world, second_player):
        dx = 0
        dy = 0
        walk_cooldown = 2
        auxiliar_y_velocity = 0
        limit_fall_velocity = 0
        gravity = 0

        if world == "FOREST":
            auxiliar_y_velocity = -23
            limit_fall_velocity = 12
            gravity = 1
        elif world == "ICE":
            auxiliar_y_velocity = -30
            limit_fall_velocity = 15
            gravity = 2

        # get keypresses
        key = pygame.key.get_pressed()
        if self.getPlayerType() == "WASD":
            if key[pygame.K_w] and self.getJumped() is False:  # conifgurar condición
                self.setYvelocity(auxiliar_y_velocity)
                self.setJumped(True)
                self.setStatus("JUMPINGON")
            elif self.getJumped() and key[pygame.K_r]:
                self.setStatus("ATTACK-JUMPING")
                new_counter = self.getAnimationCounter()
                new_counter += 1
                self.setAnimationCounter(new_counter)
            elif key[pygame.K_a] and key[pygame.K_r]:
                self.setStatus("ATTACK-RUNNING")
                dx -= 10
                new_counter = self.getAnimationCounter()
                new_counter += 1
                self.setAnimationCounter(new_counter)
                self.setAnimationDirection(-1, 'X')

                if self.getCharacter() == "NINJA-MALE" or self.getCharacter() == "NINJA-FEMALE":
                    self.handleBulletCreation()
                    Player.NINJA_BOY_GIRL_KUNAI_HIT_SOUND.play()
            elif key[pygame.K_a] and key[pygame.K_s]:
                self.setStatus("SLIDE")
                dx -= 10
                new_counter = self.getAnimationCounter()
                new_counter += 1
                self.setAnimationCounter(new_counter)
                self.setAnimationDirection(-1, 'X')
            elif key[pygame.K_a]:
                self.setStatus("RUN")
                dx -= 10
                new_counter = self.getAnimationCounter()
                new_counter += 1
                self.setAnimationCounter(new_counter)
                self.setAnimationDirection(-1, 'X')
            elif key[pygame.K_d] and key[pygame.K_r]:
                self.setStatus("ATTACK-RUNNING")
                dx += 10
                new_counter = self.getAnimationCounter()
                new_counter += 1
                self.setAnimationCounter(new_counter)
                self.setAnimationDirection(1, 'X')
                if self.getCharacter() == "NINJA-MALE" or self.getCharacter() == "NINJA-FEMALE":
                    self.handleBulletCreation()
                    Player.NINJA_BOY_GIRL_KUNAI_HIT_SOUND.play()
            elif key[pygame.K_d] and key[pygame.K_s]:
                self.setStatus("SLIDE")
                dx += 10
                new_counter = self.getAnimationCounter()
                new_counter += 1
                self.setAnimationCounter(new_counter)
                self.setAnimationDirection(1, 'X')
            elif key[pygame.K_d]:
                self.setStatus("RUN")
                dx += 10
                new_counter = self.getAnimationCounter()
                new_counter += 1
                self.setAnimationCounter(new_counter)
                self.setAnimationDirection(1, 'X')
            elif key[pygame.K_r]:
                new_counter = self.getAnimationCounter()
                new_counter += 1
                self.setAnimationCounter(new_counter)
                if key[pygame.K_a] is False and key[pygame.K_d] is False:
                    self.setStatus("ATTACK-STILL")
            elif key[pygame.K_a] is False and key[pygame.K_d] is False:
                self.setAnimationCounter(0)
                self.setAnimationIndex(0)
                if self.getAnimationDirection()[0] == 1:
                    self.setPlayerImage(self.getAnimationList('IDLE', 'RIGHT'))  # IDLE state with right direction
                if self.getAnimationDirection()[0] == -1:
                    self.setPlayerImage(self.getAnimationList('IDLE', 'LEFT'))  # IDLE state with left directio
        if self.getPlayerType() == "ULDR":
            if key[pygame.K_UP] and self.getJumped() is False:  # configurar condición
                self.setYvelocity(auxiliar_y_velocity)
                self.setJumped(True)
                self.setStatus("JUMPINGON")
            elif self.getJumped() and key[pygame.K_p]:
                self.setStatus("ATTACK-JUMPING")
                new_counter = self.getAnimationCounter()
                new_counter += 1
                self.setAnimationCounter(new_counter)
            elif key[pygame.K_LEFT] and key[pygame.K_p]:
                self.setStatus("ATTACK-RUNNING")
                dx -= 10
                new_counter = self.getAnimationCounter()
                new_counter += 1
                self.setAnimationCounter(new_counter)
                self.setAnimationDirection(-1, 'X')
                if self.getCharacter() == "NINJA-MALE" or self.getCharacter() == "NINJA-FEMALE":
                    self.handleBulletCreation()
                    Player.NINJA_BOY_GIRL_KUNAI_HIT_SOUND.play()
            elif key[pygame.K_LEFT] and key[pygame.K_DOWN]:
                self.setStatus("SLIDE")
                dx -= 10
                new_counter = self.getAnimationCounter()
                new_counter += 1
                self.setAnimationCounter(new_counter)
                self.setAnimationDirection(-1, 'X')
            elif key[pygame.K_LEFT]:
                self.setStatus("RUN")
                dx -= 10
                new_counter = self.getAnimationCounter()
                new_counter += 1
                self.setAnimationCounter(new_counter)
                self.setAnimationDirection(-1, 'X')
            elif key[pygame.K_RIGHT] and key[pygame.K_p]:
                self.setStatus("ATTACK-RUNNING")
                dx += 10
                new_counter = self.getAnimationCounter()
                new_counter += 1
                self.setAnimationCounter(new_counter)
                self.setAnimationDirection(1, 'X')
                if self.getCharacter() == "NINJA-MALE" or self.getCharacter() == "NINJA-FEMALE":
                    self.handleBulletCreation()
                    Player.NINJA_BOY_GIRL_KUNAI_HIT_SOUND.play()
            elif key[pygame.K_RIGHT] and key[pygame.K_DOWN]:
                self.setStatus("SLIDE")
                dx += 10
                new_counter = self.getAnimationCounter()
                new_counter += 1
                self.setAnimationCounter(new_counter)
                self.setAnimationDirection(1, 'X')
            elif key[pygame.K_RIGHT]:
                self.setStatus("RUN")
                dx += 10
                new_counter = self.getAnimationCounter()
                new_counter += 1
                self.setAnimationCounter(new_counter)
                self.setAnimationDirection(1, 'X')
            elif key[pygame.K_p]:
                new_counter = self.getAnimationCounter()
                new_counter += 1
                self.setAnimationCounter(new_counter)
                if key[pygame.K_RIGHT] is False and key[pygame.K_LEFT] is False:  # ATTACK
                    self.setStatus("ATTACK-STILL")
            elif key[pygame.K_LEFT] is False and key[pygame.K_RIGHT] is False:
                self.setAnimationCounter(0)
                self.setAnimationIndex(0)
                if self.getAnimationDirection()[0] == 1:
                    self.setPlayerImage(self.getAnimationList('IDLE', 'RIGHT'))  # IDLE state with right direction
                if self.getAnimationDirection()[0] == -1:
                    self.setPlayerImage(self.getAnimationList('IDLE', 'LEFT'))  # IDLE state with left direction

        # handle animation most of the animations
        if self.getAnimationCounter() >= walk_cooldown:
            # Modes 'ATTACK-LEFT', 'JUMP_ATTACK-LEFT', 'RUN_ATTACK-LEFT'
            self.setAnimationCounter(0)
            new_index = self.getAnimationIndex()
            new_index += 1
            self.setAnimationIndex(new_index)
            if self.getStatus() == "RUN":
                # handle RIGHT-LEFT animation
                if self.getAnimationIndex() >= len(self.getAnimationList("RUN", "RIGHT")):
                    self.setAnimationIndex(0)
                if self.getAnimationDirection()[0] == 1:  # Going Right
                    self.setPlayerImage(self.getAnimationList("RUN", "RIGHT")[self.getAnimationIndex()])
                elif self.getAnimationDirection()[0] == -1:  # Going left
                    self.setPlayerImage(self.getAnimationList("RUN", "LEFT")[self.getAnimationIndex()])
            elif self.getStatus() == "SLIDE":
                # if self.getAnimationIndex() >= len(self.getAnimationList("SLIDE", "RIGHT")):
                #     self.setAnimationIndex(0)
                if self.getAnimationDirection()[0] == 1:  # Going Right
                    self.setPlayerImage(self.getAnimationList("SLIDE", "RIGHT"))
                elif self.getAnimationDirection()[0] == -1:  # Going left
                    self.setPlayerImage(self.getAnimationList("SLIDE", "LEFT"))
            if self.getStatus() == "JUMPINGON":
                # if self.getAnimationIndex() >= len(self.getAnimationList("JUMP OFF", "RIGHT")):
                #     self.setAnimationIndex(0)
                if self.getAnimationDirection()[0] == 1:
                    if self.getCharacter() != "ZOMBIE-FEMALE":
                        self.setPlayerImage(
                            self.getAnimationList('JUMP ON', 'RIGHT'))  # IDLE state with right direction
                    else:
                        self.setPlayerImage(self.getAnimationList('IDLE', 'RIGHT'))  # IDLE state with right direction
                if self.getAnimationDirection()[0] == -1:
                    if self.getCharacter() != "ZOMBIE-FEMALE":
                        self.setPlayerImage(self.getAnimationList('JUMP ON', 'LEFT'))  # IDLE state with left direction
                    else:
                        self.setPlayerImage(self.getAnimationList('IDLE', 'LEFT'))  # IDLE state with right direction

            if self.getStatus() == "ATTACK-STILL":
                if self.getAnimationIndex() >= len(self.getAnimationAttackList("ATTACK", "RIGHT")):
                    self.setAnimationIndex(0)
                if self.getAnimationDirection()[0] == 1:  # Going Right
                    self.setPlayerImage(self.getAnimationAttackList("ATTACK", "RIGHT")[self.getAnimationIndex()])
                elif self.getAnimationDirection()[0] == -1:  # Going left
                    self.setPlayerImage(self.getAnimationAttackList("ATTACK", "LEFT")[self.getAnimationIndex()])

                if self.getCharacter() == "NINJA-MALE" or self.getCharacter() == "NINJA-FEMALE":
                    if self.getAnimationIndex() == 5:
                        self.handleBulletCreation()
                        Player.NINJAS_ZOMBIES_WAVE_HIT_SOUND.play()
                elif self.getCharacter() == "ROBOT":
                    if self.getAnimationIndex() == 2:
                        self.handleBulletCreation()
                        Player.ROBOT_BULLET_HIT_SOUND.play()
                elif self.getCharacter() == "ZOMBIE-FEMALE":
                    self.handleBulletCreation()
                    Player.NINJAS_ZOMBIES_WAVE_HIT_SOUND.play()
            if self.getCharacter() != "ZOMBIE-FEMALE":
                if self.getStatus() == "ATTACK-RUNNING":
                    if self.getAnimationIndex() >= len(self.getAnimationAttackList("RUN_ATTACK", "RIGHT")):
                        self.setAnimationIndex(0)
                    if self.getAnimationDirection()[0] == 1:  # Going Right
                        self.setPlayerImage(
                            self.getAnimationAttackList("RUN_ATTACK", "RIGHT")[self.getAnimationIndex()])
                    elif self.getAnimationDirection()[0] == -1:  # Going left
                        self.setPlayerImage(self.getAnimationAttackList("RUN_ATTACK", "LEFT")[self.getAnimationIndex()])

                    if self.getCharacter() == "ROBOT" and self.getAnimationIndex() == 7:
                        self.handleBulletCreation()
                        Player.ROBOT_BULLET_HIT_SOUND.play()
                if self.getStatus() == "ATTACK-JUMPING":
                    if self.getAnimationIndex() >= len(self.getAnimationAttackList("JUMP_ATTACK", "RIGHT")):
                        self.setAnimationIndex(0)
                    if self.getAnimationDirection()[0] == 1:  # Going Right
                        self.setPlayerImage(
                            self.getAnimationAttackList("JUMP_ATTACK", "RIGHT")[self.getAnimationIndex()])
                    elif self.getAnimationDirection()[0] == -1:  # Going left
                        self.setPlayerImage(
                            self.getAnimationAttackList("JUMP_ATTACK", "LEFT")[self.getAnimationIndex()])
                    if self.getCharacter() == "NINJA-MALE" or self.getCharacter() == "NINJA-FEMALE":
                        if self.getAnimationIndex() == 7:
                            self.handleBulletCreation()
                            Player.NINJA_BOY_GIRL_KUNAI_HIT_SOUND.play()
                    elif self.getCharacter() == "ROBOT":
                        if self.getAnimationIndex() == 4:
                            self.handleBulletCreation()
                            Player.ROBOT_BULLET_HIT_SOUND.play()

        # handle bullets creation
        # self.handleBulletCreation()
        self.handleBulletsMovement(screen_width, second_player, collisions_objects)

        # add gravity
        yVelocity = self.getYvelocity()
        yVelocity += gravity
        self.setYvelocity(yVelocity)
        if self.getYvelocity() > limit_fall_velocity:
            self.setYvelocity(limit_fall_velocity)

        dy += self.getYvelocity()

        self.isPlayerOutsideBoundaries(screen_height)

        # check for collision between player and map
        for object in collisions_objects:
            # check for collision in x direction
            if object.colliderect(self.getPlayerRectangle().x + dx, self.getPlayerRectangle().y,
                                  self.getPlayerRectangle().width, self.getPlayerRectangle().height):
                dx = 0
            # check for collision in y direction
            if object.colliderect(self.getPlayerRectangle().x, self.getPlayerRectangle().y + dy,
                                  self.getPlayerRectangle().width, self.getPlayerRectangle().height):
                # check if below the ground i.e. jumping
                if self.getYvelocity() < 0:
                    dy = object.bottom - self.getPlayerRectangle().top
                # check if above the ground i.e. falling
                elif self.getYvelocity() >= 0:
                    dy = object.top - self.getPlayerRectangle().bottom
                    self.setYvelocity(0)
                    self.setJumped(False)
                self.setYvelocity(0)

        # update player coordinates
        new_coordinates_X = self.getCoordinateX()
        new_coordinates_X += dx
        self.setCoordinateX(new_coordinates_X)

        # Jmping off animation, only when the player has jumped and the coords have been changed

        new_coordinates_Y = self.getCoordinateY()
        new_coordinates_Y += dy
        self.setCoordinateY(new_coordinates_Y)

        # draw player onto screen
        screen.blit(self.getPlayerImage(), self.player_rect)
        self.drawBullets(screen)
        # pygame.draw.rect(screen, (0, 0, 0), self.getPlayerRectangle(), width=2)
