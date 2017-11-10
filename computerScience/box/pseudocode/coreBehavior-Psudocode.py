# recieve a player target
FUNCTION coreControl(core):
    keys <- pygame.key.get_pressed()
    IF not core.isDead:
        IF core.body.__GetLinearVelocity().y <= 0:
            IF core.jet_energy < 100:
                core.jet_energy += 0.2
            ENDIF
        # left
        ENDIF
        IF keys[K_a] = 1:
            core.body.__SetLinearVelocity((core.body.__GetLinearVelocity().x - 10, core.body.__GetLinearVelocity().y))
            core.direction <- 0
        # right
        ENDIF
        IF keys[K_d] = 1:
            core.body.__SetLinearVelocity((core.body.__GetLinearVelocity().x + 10, core.body.__GetLinearVelocity().y))
            core.direction <- 1
        # up
        ENDIF
        IF keys[K_w] = 1:
            IF core.jet_energy > 0:
                core.body.__SetLinearVelocity((core.body.__GetLinearVelocity().x, core.body.__GetLinearVelocity().y + 50))
                core.jet_energy -= 1.2
            ENDIF
        # down
        ENDIF
        IF keys[K_s] = 1:
            IF core.jet_energy > 0:
                core.body.__SetLinearVelocity((core.body.__GetLinearVelocity().x, core.body.__GetLinearVelocity().y - 25))
                core.jet_energy -= 0.3
        ENDIF
            ENDIF
        IF keys[K_LSHIFT] = 1:
            core.body.__SetLinearVelocity((core.body.__GetLinearVelocity().x, core.body.__GetLinearVelocity().y + 100))
        ENDIF
        IF keys[K_f] = 1:
            core.shoot()
        ENDIF
        core.last_fire_time = core.last_fire_time + 1
