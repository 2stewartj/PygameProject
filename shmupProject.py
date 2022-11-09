import pygame
from itertools import repeat
import random
import math
import time
from copy import copy


WIDTH = 500
HEIGHT = 500

pygame.time.Clock()

easyButton = Actor("easybutton")
easyButton.pos = (WIDTH // 2, 200)
mediumButton = Actor("mediumbutton")
mediumButton.pos = (WIDTH // 2, 250)
hardButton = Actor("hardbutton")
hardButton.pos = (WIDTH // 2, 300)

pygame.init()

player = Actor("player")
player.pos = (WIDTH // 2, 450)
player.xspeed = 0
player.yspeed = 0

boss = Actor("boss")
boss.pos = (WIDTH // 2, 50)
boss.xspeed = 0

playerProjectile = Actor("playerprojectile")

playerProjectile.speed = 0


bossProjectile = Actor("bossprojectile")

bossProjectile.speed = 0


playerProj = []
bossProj = []

death = 1
t = 0.0
bossHealth = 0
maxHP = 0
print(maxHP)
phase = 0
difficulty = 0

projCount = 0
bossCount = 0

game_state = "title"

playerShoot = False
bossShoot = False
bossAbove = True

Projectiles = pygame.sprite.Group()


def on_mouse_down(pos):

    global difficulty
    global game_state
    global bossHealth

    if easyButton.collidepoint(pos):
        difficulty = "Easy"
        easyButton.x = 5000
        mediumButton.x = 5000
        hardButton.x = 5000
        game_state = "playing"
        bossHealth = 50
        maxHP = 100

    elif mediumButton.collidepoint(pos):
        difficulty = "Medium"
        easyButton.x = 5000
        mediumButton.x = 5000
        hardButton.x = 5000
        game_state = "playing"
        bossHealth = 100
        maxHP = 100

    elif hardButton.collidepoint(pos):
        difficulty = "Hard"
        easyButton.x = 5000
        mediumButton.x = 5000
        hardButton.x = 5000
        game_state = "playing"
        bossHealth = 200
        maxHP = 200


def PlayerShoot():
    playerShoot = True

def PlayerAttack():
    pass

def BossShoot():
    bossShoot = True

def BossAbove():
    if bossAbove == True:
        bossAbove = False
    else:
        bossAbove = True


def EnemyAttackOne():
    global bossProj
    global bossShoot
    if bossShoot == True:
        bossShoot = False
        bossProj.append(bossProjectile)
        print(bossProj)
        clock.schedule(BossShoot, 1)


def BackToMenu():
    game_state = 'title'


def update(dt):
    global playerProj
    global bossProj
    global death
    global t
    global bossAbove
    global bossHealth
    global phase
    global projCount
    global game_state
    global playerShoot

    projCount = playerProj.count("shoot")
    bossCount = bossProj.count("shoot")

    if game_state == "playing":
        t += dt
        player.x += player.xspeed
        player.y += player.yspeed


        if difficulty == "Easy":
            playerProjectile.speed = 10
        elif difficulty == "Medium":
            playerProjectile.speed = 8
        elif difficulty == "Hard":
            playerProjectile.speed = 6

        if playerShoot == False:
            pygame.time.wait(250)
            playerShoot = True

        if player.x > WIDTH:
            player.xspeed = 0
            if keyboard.a:
                player.xspeed = -3

        elif player.x < 0:
            player.xspeed = 0
            if keyboard.d:
                player.xspeed = 3

        else:
            if keyboard.a:
                player.xspeed = -3

            elif keyboard.d:
                player.xspeed = 3

            else:
                player.xspeed = 0

        if player.y > HEIGHT:
            player.yspeed = 0
            if keyboard.w:
                player.yspeed = -3

        elif player.y < 0:
            player.yspeed = 0
            if keyboard.s:
                player.yspeed = 3

        else:
            if keyboard.w:
                player.yspeed = -3

            elif keyboard.s:
                player.yspeed = 3

            else:
                player.yspeed = 0

        if keyboard.space:
            print(projCount)
            print(playerShoot)
            if playerShoot:
                playerProj.append(playerProjectile)
                print(playerProj)
                playerShoot = False
                print(playerShoot)
                clock.schedule(PlayerShoot, 500)

            else:
                print("can't shoot yet")

        if playerProj != 0:

            for proj in playerProj:
                if playerProjectile.y <= 0:
                    if projCount == 0:
                        pass
                    else:
                        for n in playerProjectile.y <= 0:
                            playerProjectile.x = 5000

                if playerProjectile.colliderect(boss):
                    bossHealth -= 1
                    if projCount == 0:
                        pass
                    else:
                        for n in playerProjectile.colliderect(boss):
                            playerProjectile.x = 5000

                playerProjectile.pos = player.pos
                playerProjectile.y -= playerProjectile.speed


        for proj in bossProj:
            bossProjectile.pos = boss.pos
            print(bossProjectile.speed)
            bossProjectile.y -= bossProjectile.speed






        if player.colliderect(boss):
            death += 1
            player.pos = (WIDTH // 2, 450)
            boss.pos = (WIDTH // 2, 50)
            if difficulty == "Easy":
                bossHealth = 50
            if difficulty == "Medium":
                bossHealth = 100
            playerProj = []
            bossProj = []
            playerProjectile.pos = player.pos
        if player.colliderect(bossProjectile):
            death += 1
            player.pos = (WIDTH // 2, 450)
            boss.pos = (WIDTH // 2, 50)
            if difficulty == "Easy":
                bossHealth = 50
            if difficulty == "Medium":
                bossHealth = 100
            if difficulty == "Hard":
                bossHealth = 200
            playerProj = []
            bossProj = []
            playerProjectile.pos = player.pos
        if bossAbove:
            boss.x += boss.xspeed
            boss.xspeed = player.xspeed
            bossProjectile.y += bossProjectile.speed
        else:
            boss.y += boss.xspeed
            boss.yspeed = player.xspeed
            bossProjectile.x += bossProjectile.speed

        if difficulty == "Easy":
            bossProjectile.speed = 3
            if 0 < bossHealth <= 50:

                phase = 1

            if phase == 1:
                if bossShoot:

                    clock.schedule(EnemyAttackOne, 750)
                else:
                    clock.schedule(BossShoot, 750)

        if difficulty == "Medium":
            bossProjectile.speed = 5
            if 70 <= bossHealth <= 100:
                phase = 1
            elif 25 <= bossHealth <= 70:
                phase = 2
            elif 0 < bossHealth <= 25:
                phase = 3

        if difficulty == "Hard":
            bossProjectile.speed = 8
            if 175 <= bossHealth <= 200:
                phase = 1
            elif 130 <= bossHealth <= 175:
                phase = 2
            elif 100 <= bossHealth <= 130:
                phase = 3
            elif 60 <= bossHealth <= 100:
                phase = 4
            elif 20 <= bossHealth <= 60:
                phase = 5
            elif 0 < bossHealth <= 20:
                phase = 6


            if phase == 1:

                clock.schedule(BossAbove, 10000)

        if bossHealth <= 0:

            game_state = "results"

    elif game_state == "results":
        pass
        clock.schedule(BackToMenu, 10.0)


def draw():

    if game_state == "title":
        screen.draw.text("Select a Difficulty", (175, 150))
        easyButton.draw()
        mediumButton.draw()
        hardButton.draw()

    if game_state == "playing":

        if difficulty == "Hard":
            screen.fill((72, 20, 50))
        else:
            screen.fill((78, 72, 100))
        player.draw()
        boss.draw()

        screen.draw.text("Time: " + "{:.2f}".format(t), (10, 10))
        screen.draw.text("Attempts: " + str(death), (10, 30))
        screen.draw.text("BossHP: " + str(bossHealth), (350, 10))

        for n in playerProj:
            playerProjectile.draw()

        for n in bossProj:
            bossProjectile.draw()

    elif game_state == "results":
        screen.clear()
        if difficulty == "Hard":
            screen.fill((72, 20, 50))
        else:
            screen.fill((78, 72, 100))

        screen.draw.text("VICTORY!!", (200, 150))
        screen.draw.text('Difficulty: ' + difficulty, (200, 225))
        screen.draw.text("Time: " + "{:.2f}".format(t), (200, 250))
        screen.draw.text("Attempts: " + str(death), (200, 275))
