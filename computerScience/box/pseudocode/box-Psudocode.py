# -*- coding: UTF-8 -*-
from Box2D import *
import pygame, sys, math, random
from pygame.locals import *
from picToMap import *
from enemyBehavior import enemyControl
from coreBehavior import coreControl
block_size <- 10
gravity <- 0
# set up pygame-box2d constants
bullet_size <- int(block_size / 2)
player_size_x <- int(block_size * 0.75)
player_size_y <- int(block_size * 1.5)
player_density <- 0.1
pygame_screen_x <- 1400
pygame_screen_y <- 400
camera_scale <- 1
camera_1_x <- pygame_screen_x - pygame_screen_x - 5
camera_1_y <- pygame_screen_y - pygame_screen_y - 5
# set up pygame
pygame.init()
# set up the window
windowSurface <- pygame.display.set_mode((pygame_screen_x, pygame_screen_y), FULLSCREEN)
pygame.display.set_caption("csproject 01 beta 1.0")
mode <- "menu"
# set up the colors
BLACK <- (0, 0, 0)
WHITE <- (255, 255, 255)
RED <- (255, 0, 0)
GREEN <- (100, 200, 0) 
BLUE <- (0, 0, 255)
# setup current stage (menu, game ..)
mode <- "menu"
# set up menu assets
menu_time_delay <- 0
menu_items <- [u"Play ",u"Help ",u"About ",u"Quit "]
menu_focus <- 0
FUNCTION menuDisplay():
    # clean screen
    windowSurface.fill(BLUE)
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' errOR
    y <- 100
    # render text
    for text in menu_items:
        myfont <- pygame.font.SysFont("SimHei", 30)
        IF text = menu_items[menu_focus]:
            myfont <- pygame.font.SysFont("SimHei", 40)
        ENDIF
        label <- myfont.render(text, 1, (255,255,0))
        windowSurface.blit(label, (100, y))
        y <- y + 50
    ENDFOR
    pygame.display.flip()
ENDFUNCTION

FUNCTION menuControl():
    global menu_focus
    global menu_time_delay
    global mode
    IF menu_time_delay >= 20:
        keys <- pygame.key.get_pressed()
        IF keys[K_UP] = 1:
            menu_focus -= 1
            IF menu_focus < 0:
                menu_focus <- len(menu_items) - 1
            ENDIF
            menu_time_delay <- 0
        ENDIF
        IF keys[K_DOWN] = 1:
            menu_focus += 1
            IF menu_focus >= len(menu_items):
                menu_focus <- 0
            ENDIF
            menu_time_delay <- 0
        # IF selected
        ENDIF
          ENDIF
        IF keys[K_RETURN] = 1:
            IF menu_focus = 0:
                mode <- "game"
                core.__init__(100, 200, 100, 10, 100, 1)
                enemy.__init__(1200, 200, 100, 10, 100, 0)
            ENDIF
            IF menu_focus = 3:
                pygame.quit()
                sys.exit(0)
        ENDIF
            ENDIF
        IF keys[K_TAB] = 1:
            mode <- "game"
    ENDIF
        ENDIF
    IF menu_time_delay >= 10000:
        menu_time_delay <- 20
    ENDIF
    menu_time_delay += 1
# menu setup end
# game set up start
# setup game assets
# produce map
ENDFUNCTION

mapArray <- generateMap("map2.bmp")
# setup terrain list
terrainList <- []
# set up  box2d world
world <- b2World()
world.__SetGravity((0, -gravity))
# create player CLASS
                ENDCLASS

CLASS player:
    # initialize method
    FUNCTION __init__(self, x <- 0, y <- 0, life_value <- 100, power_value <- 0, jet_energy_value <- 100, direction_value <- 1):
                                      ENDIF
        # life set to 100
           ENDIF
         life <- life_value
              ENDIF
         direction <- direction_value
        # jet pack energy set to 100
         jet_energy <- jet_energy_value
        # power set to 10
         power <- power_value
        # record the last fire time to for bullet time delay effect
                                       ENDFOR
         last_fire_time <- 0
        # the body of the player
         body <- create_player_body(x, y)
        # determine IF the player should be rendered OR not
                    ENDIF
         isDead <- False
        # determine IF the player should be drawn red
                    ENDIF
         isHurt <- False
        try:
            for i in  bullet_list:
                world.DestroyBody(i)
            ENDFOR
             bullet_list <- []
        except:
            # list used to store bullets
             bullet_list <- []
    ENDFUNCTION

    FUNCTION shoot(self):
        # fire ammo
        IF  last_fire_time > 10:
            IF  direction = 1:
                 bullet <- create_bullet( body.position[0] + block_size + 1,  body.position[1])
                IF  bullet = None:
                    RETURN
                ENDIF
                 bullet.linearVelocity.x <- 1000 +  body.linearVelocity.x
            ELSEIF  direction = 0:
                 bullet <- create_bullet( body.position[0] - block_size - 1,  body.position[1])
                IF  bullet = None:
                    RETURN
                ENDIF
                 bullet.linearVelocity.x <- -1000 +  body.linearVelocity.x
            # OUTPUT  bullet.linearVelocity.x
            ENDIF
             bullet.userData <- "bullet"
            IF len( bullet_list) <= 100:
                 bullet_list.append( bullet)
            ELSE:
                world.DestroyBody( bullet_list[0])
                 bullet_list <-  bullet_list[1:]
                 bullet_list.append( bullet)
            ENDIF
             last_fire_time <- 0
        ENDIF
    # hited by enemy
    ENDFUNCTION

    FUNCTION hit(self, hitPower=0):
         life -= hitPower
              ENDIF
         isHurt <- True
        IF  life <= 0:
             dead()
        ENDIF
    ENDFUNCTION

    FUNCTION dead(self):
         isDead <- True
        world.DestroyBody( body)
    ENDFUNCTION

# game assets setup end
# function used to create bullets
ENDCLASS

FUNCTION create_bullet(box_x_pos, box_y_pos):
    try:
        body <- world.CreateDynamicBody(position=(box_x_pos, box_y_pos))
        box <- body.CreatePolygonFixture(box=(bullet_size / 2.0, bullet_size / 2.0), density=0.001, friction=1)
        body.linearDamping <- 0
    except:
        RETURN None
    RETURN body
# function used to instantiate enemy
ENDFUNCTION

FUNCTION create_player_body(box_x_pos, box_y_pos):
    body <- world.CreateDynamicBody(position=(box_x_pos, box_y_pos))
    body.fixedRotation <- True
    body.__SetUserData(data="player")
    tex <- body.CreatePolygonFixture(box=(player_size_x / 2.0, player_size_y / 2.0), density=100, friction=0.9)
    tex.fixedRotation <- True
    RETURN body
# game terrain setup
ENDFUNCTION

FUNCTION generateBlockFromMap(map):
    for i in range(0, len(mapArray)):
        for j in range(0, len(mapArray[i])):
            IF mapArray[i][j] != 255:
                block <- world.CreateStaticBody(
                    position=(j * block_size, i * block_size),
                    shapes=b2PolygonShape(box=(block_size / 2, block_size / 2)),
                )
                block.__SetUserData(data="block")
                terrainList.append(block)
            ENDIF
ENDFUNCTION

    ENDFOR
        ENDFOR
generateBlockFromMap(mapArray)
# game terrain setup end
# create main player core
core <- player(100, 200, 100, 10, 100, 1)
# create enemy
enemy <- player(400, 200, 100, 10, 100, 0)
# game setup end
# load image
# load bullet texture
bulletImage <- pygame.image.load("redbox.png").convert()
bulletTex <- pygame.transform.scale(bulletImage, (bullet_size, bullet_size))
                        ENDFOR
# load player texture
playerImage <- pygame.image.load("player.png").convert()
playerHurtImage <- pygame.image.load("playerHurt.png").convert()
playerTex <- pygame.transform.scale(playerImage, (player_size_x, player_size_y))
                        ENDFOR
# load dirt texture
dirtImage <- pygame.image.load("dirt.png").convert()
dirtTex <- pygame.transform.scale(dirtImage, (int(block_size), int(block_size)))
                      ENDFOR
# load grass texture
grassImage <- pygame.image.load("grass.png").convert()
grassTex <- pygame.transform.scale(grassImage, (int(block_size), int(block_size)))
                       ENDFOR
# load rock texture
rockImage <- pygame.image.load("rock.png").convert()
rockTex <- pygame.transform.scale(rockImage, (int(block_size), int(block_size)))
                      ENDFOR
# load brick texture
brickImage <- pygame.image.load("brick.png").convert()
brickTex <- pygame.transform.scale(brickImage, (int(block_size), int(block_size)))
                       ENDFOR
FUNCTION gameControl():
    global mode
    keys <- pygame.key.get_pressed()
    # exit to menu
    IF keys[K_ESCAPE] = 1:
        mode <- "menu"
    ENDIF
ENDFUNCTION

FUNCTION gamePhysics():
    # get the objects that are colliding
    contactList <- world.__GetContactList_internal()
    # IF there is objects colliding
      ENDIF
    IF contactList != None:
        # colliding object a AND b
        bodyA <- contactList.__GetFixtureA().__GetBody()
        bodyB <- contactList.__GetFixtureB().__GetBody()
        # case that obj a is bullet
        IF bodyA.__GetUserData() = "bullet":
            # destroy bullet
            world.DestroyBody(bodyA)
            # remove bullet from the bullet list in player
            try:
                core.bullet_list.remove(bodyA)
            except:
                enemy.bullet_list.remove(bodyA)
            # IF another object is a player
              ENDIF
            IF bodyB = core.body:
                core.hit(enemy.power)
            ELSEIF bodyB = enemy.body:
                enemy.hit(core.power)
            ENDIF
        # case that obj b is bullet
        ELSEIF bodyB.__GetUserData() = "bullet":
            # destroy bullet
            world.DestroyBody(bodyB)
            # remove bullet from the bullet list in player
            try:
                core.bullet_list.remove(bodyB)
            except:
                enemy.bullet_list.remove(bodyB)
            # IF another object is a player
              ENDIF
            IF bodyA = core.body:
                core.hit(enemy.power)
            ELSEIF bodyA = enemy.body:
                enemy.hit(core.power)
        ENDIF
            ENDIF
    # get the camera coordinates as global variable
    ENDIF
    global camera_1_y
    global camera_1_x
    # add gravity velocity
    IF not core.isDead:
        core.body.__SetLinearVelocity((core.body.__GetLinearVelocity()[0], core.body.__GetLinearVelocity()[1] - 10))
    ENDIF
    IF not enemy.isDead:
        enemy.body.__SetLinearVelocity((enemy.body.__GetLinearVelocity()[0], enemy.body.__GetLinearVelocity()[1] - 10))
    # tick the time to perform physics effect        
    ENDIF
                          ENDFOR
    world.Step(timeStep, vel_iters, pos_iters)
ENDFUNCTION

FUNCTION renderBullet(body, tex, size):
    texBox <- pygame.transform.scale(bulletImage, (int(size), int(size)))
                         ENDFOR
    rotatedTex <- pygame.transform.rotozoom(texBox, math.degrees(body.angle), 1)
                             ENDFOR
    rotatedTex.set_colorkey(0)
    windowSurface.blit(rotatedTex, (((body.position.x - camera_1_x)) - ((size / 2.0)), (pygame_screen_y - (body.position.y) - ((size / 2.0) - camera_1_y))))
ENDFUNCTION

FUNCTION renderPlayer(player):
    # rotate AND draw player core
    IF player.isDead:
        RETURN
    # rotate AND draw bullet
    ENDIF
    for bullet in player.bullet_list:
        renderBullet(bullet, bulletTex, bullet_size)
    # IF hited by bullet, turns red
      ENDIF
    ENDFOR
    IF player.isHurt:
        playerTex <- pygame.transform.scale(playerHurtImage, (player_size_x, player_size_y))
                                ENDFOR
        player.isHurt <- False
    ELSE:
        playerTex <- pygame.transform.scale(playerImage, (player_size_x, player_size_y))
                                ENDFOR
    # find the direction of player
    ENDIF
    IF player.direction = 0:
        renderTex <- pygame.transform.flip(playerTex, True, False)
                                ENDFOR
    ELSE:
        renderTex <- pygame.transform.flip(playerTex, False, False)
                                ENDFOR
    # render player to the screen
    ENDIF
    windowSurface.blit(renderTex, (((player.body.position.x - camera_1_x)) - ((player_size_x / 2.0)), (pygame_screen_y - (player.body.position.y) - ((player_size_y / 2.0) - camera_1_y))))
    # draw player's life bar
                     ENDIF
    pygame.draw.rect(windowSurface, RED, (player.body.position.x - camera_1_x - 10, 460 - bPos2pPos(player.body.position.x, player.body.position.y)[1] + camera_1_y - 10, player.life / 5, 2))
                                                                                                                                                                                  ENDIF
    # draw player's jet bar
    pygame.draw.rect(windowSurface, WHITE, (player.body.position.x - camera_1_x - 10, 460 - bPos2pPos(player.body.position.x, player.body.position.y)[1] + camera_1_y - 13, player.jet_energy / 5, 2))
ENDFUNCTION

FUNCTION bPos2pPos(bPos_x, bPos_y):
    RETURN [bPos_x, bPos_y + 70]
ENDFUNCTION

FUNCTION pPos2bPos(pPos_x, pPos_y):
    RETURN [pPos_x, pPos_y - 70]
ENDFUNCTION

FUNCTION renderUI():
    # draw ui
    # draw jet bar
    IF core.isDead:
        # draw gameover IF core died
                        ENDIF
        gameOverFont <- pygame.font.SysFont("consolas", 150)
        gameOverLabel <- gameOverFont.render("PLAYER 2 WINS", int(pygame_screen_x / 2), (255,0,0))
        windowSurface.blit(gameOverLabel, (100, 150))
    ENDIF
    IF enemy.isDead:
        # draw gameover IF core died
                        ENDIF
        gameOverFont <- pygame.font.SysFont("consolas", 150)
        gameOverLabel <- gameOverFont.render("PLAYER 1 WINS", int(pygame_screen_x / 2), (255,0,0))
        windowSurface.blit(gameOverLabel, (100, 150))
    ENDIF
ENDFUNCTION

FUNCTION gameDisplay(playerImage):
    global gunTex_01
    # clean screen
    windowSurface.fill(BLUE)
    # draw ground
    for i in range(0, len(mapArray)):
        for j in range(0, len(mapArray[i])):
            # render grass
            IF mapArray[i][j] = 0:
                windowSurface.blit(grassTex, (bPos2pPos(j * block_size, i * block_size)[0] - 5 - camera_1_x, 465 - bPos2pPos(j * block_size, i * block_size)[1] + camera_1_y))
            # render rock
            ENDIF
            IF mapArray[i][j] = 128:
                windowSurface.blit(rockTex, (bPos2pPos(j * block_size, i * block_size)[0] - 5 - camera_1_x, 465 - bPos2pPos(j * block_size, i * block_size)[1] + camera_1_y))
            # render dirt
            ENDIF
            IF mapArray[i][j] = 192:
                windowSurface.blit(dirtTex, (bPos2pPos(j * block_size, i * block_size)[0] - 5 - camera_1_x, 465 - bPos2pPos(j * block_size, i * block_size)[1] + camera_1_y))
            # render brick
            ENDIF
            IF mapArray[i][j] = 64:
                windowSurface.blit(brickTex, (bPos2pPos(j * block_size, i * block_size)[0] - 5 - camera_1_x, 465 - bPos2pPos(j * block_size, i * block_size)[1] + camera_1_y))
            ENDIF
    ENDFOR
        ENDFOR
    IF not core.isDead:
        renderPlayer(core)
    ENDIF
    IF not enemy.isDead:
        renderPlayer(enemy)
    # draw ui on top
    ENDIF
    renderUI()
    # refresh screen
    pygame.display.flip()
ENDFUNCTION

FUNCTION pyg():
    time_passed <- clock.tick(100)
    IF mode = "game":
        gameControl()
        coreControl(core)
        enemyControl(enemy)
        gameDisplay(playerImage)
    ELSEIF mode = "menu":
        menuControl()
        menuDisplay()
    ENDIF
# Prepare for simulation. Typically we use a time step of 1/100 of a
          ENDFOR
# second (100Hz) AND 6 velocity/2 position iterations. This provides a
# high quality simulation in most game scenarios.
ENDFUNCTION

timeStep <- 1.0 / 100
vel_iters, pos_iters <- 6, 2
# This is our little animation loop.
clock <- pygame.time.Clock()
ev <- pygame.event.poll()
while ev.type != pygame.QUIT:
    ev <- pygame.event.poll()
    pyg()
    IF mode = "game":
        gamePhysics()
    ENDIF
ENDWHILE
pygame.quit()
