# recieve a player target
FUNCTION enemyControl(enemy):
    keys <- pygame.key.get_pressed()
    IF not enemy.isDead:
        IF enemy.body.__GetLinearVelocity().y <= 0:
            IF enemy.jet_energy < 100:
                enemy.jet_energy += 0.2
            ENDIF
        ENDIF
        # left
        IF keys[K_LEFT] = 1:
            enemy.body.__SetLinearVelocity((enemy.body.__GetLinearVelocity().x - 15, enemy.body.__GetLinearVelocity().y))
            enemy.direction <- 0
        ENDIF
        # right
        IF keys[K_RIGHT] = 1:
            enemy.body.__SetLinearVelocity((enemy.body.__GetLinearVelocity().x + 15, enemy.body.__GetLinearVelocity().y))
            enemy.direction <- 1
        ENDIF
        # up
        IF keys[K_UP] = 1:
            IF enemy.jet_energy > 0:
                enemy.body.__SetLinearVelocity((enemy.body.__GetLinearVelocity().x, enemy.body.__GetLinearVelocity().y + 50))
                enemy.jet_energy -= 1.2
            ENDIF
        ENDIF
        # down
        IF keys[K_DOWN] = 1:
            IF enemy.jet_energy > 0:
                enemy.body.__SetLinearVelocity((enemy.body.__GetLinearVelocity().x, enemy.body.__GetLinearVelocity().y - 25))
                enemy.jet_energy -= 0.3
            ENDIF
        ENDIF
        IF keys[K_RSHIFT] = 1:
            enemy.body.__SetLinearVelocity((enemy.body.__GetLinearVelocity().x, enemy.body.__GetLinearVelocity().y + 100))
        ENDIF
        IF keys[K_SLASH] = 1:
            enemy.shoot()
        ENDIF
        enemy.last_fire_time = core.last_fire_time + 1
ENDFUNCTION