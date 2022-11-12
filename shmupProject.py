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



playerSpeed = 0
bossSpeed = 0
bossProjHoriz = 5

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

playerShoot = True
bossShoot = True
bossAbove = True

Projectiles = pygame.sprite.Group()


def on_mouse_down(pos):

    global difficulty
    global game_state
    global bossHealth
    global playerSpeed
    global bossSpeed

    if easyButton.collidepoint(pos):
        difficulty = "Easy"
        easyButton.x = 5000
        mediumButton.x = 5000
        hardButton.x = 5000
        game_state = "playing"
        bossHealth = 50
        maxHP = 100
        playerSpeed = 10
        bossSpeed = 3

    elif mediumButton.collidepoint(pos):
        difficulty = "Medium"
        easyButton.x = 5000
        mediumButton.x = 5000
        hardButton.x = 5000
        game_state = "playing"
        bossHealth = 100
        maxHP = 100
        playerSpeed = 8
        bossSpeed = 5

    elif hardButton.collidepoint(pos):
        difficulty = "Hard"
        easyButton.x = 5000
        mediumButton.x = 5000
        hardButton.x = 5000
        game_state = "playing"
        bossHealth = 200
        maxHP = 200
        playerSpeed = 6
        bossSpeed = 8


def PlayerShoot():
    global playerShoot
    playerShoot = True

def PlayerAttack():
    pass

def BossShoot():
    global bossShoot
    bossShoot = True

def BossAbove():
    if bossAbove == True:
        bossAbove = False
    else:
        bossAbove = True





def BossAttackOne():
    global bossSpeed
    global bossShoot
    if bossShoot:
        bossProj.append(Actor('bossprojectile'))
        bossProj[-1].pos = boss.pos
        bossShoot = False

        clock.schedule(BossShoot, .75)

    for proj in bossProj:
            proj.y += bossSpeed
            if proj.y >= HEIGHT:
                bossProj.remove(proj)

def BossAttackTwo():
    global bossSpeed
    global bossShoot
    global bossProjHoriz
    bossProjHoriz = 5
    if bossShoot:
        bossProj.append(Actor('bossprojectile'))
        bossProj[-1].pos = boss.pos
        bossShoot = False

        clock.schedule(BossShoot, .75)

    for proj in bossProj:
            proj.y += bossSpeed

            proj.x += bossProjHoriz
            if proj.x >= WIDTH:
                bossProjHoriz = -5
            elif proj.x <= 0:
                bossProjHoriz = 5
            if proj.y >= HEIGHT:
                bossProj.remove(proj)


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
    global bossShoot

    projCount = playerProj.count("shoot")
    bossCount = bossProj.count("shoot")

    if game_state == "playing":
        t += dt
        player.x += player.xspeed
        player.y += player.yspeed






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

            if playerShoot:
                sounds.shoot.play()
                playerProj.append(Actor('playerprojectile'))
                playerProj[-1].pos = player.pos
                playerShoot = False

                clock.schedule(PlayerShoot, .30)

            else:
                print("can't shoot yet")

        for proj in playerProj:
            proj.y -= 10
            if proj.y <= 0:
                playerProj.remove(proj)

        for proj in playerProj:
            if proj.colliderect(boss):
                sounds.hit.play()
                bossHealth -= 1
                playerProj.remove(proj)

        for proj in bossProj:
            if player.colliderect(proj):
                sounds.death.play()
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


        if player.colliderect(boss):
            sounds.death.play()
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







        if player.colliderect(boss):
            death += 1
            player.pos = (WIDTH // 2, 450)
            boss.pos = (WIDTH // 2, 50)
            if difficulty == "Easy":
                bossHealth = 50
            if difficulty == "Medium":
                bossHealth = 100
            if difficulty == "Hard":
                bossHealth == 200
            playerProj = []
            bossProj = []





        if difficulty == "Easy":

            if 0 < bossHealth <= 50:

                phase = 1

            if phase == 1:
                boss.x = player.x
                clock.schedule(BossAttackOne, .75)



        if difficulty == "Medium":

            if 70 <= bossHealth <= 100:
                phase = 1
            elif 25 <= bossHealth <= 70:
                phase = 2
            elif 0 < bossHealth <= 25:
                phase = 3

            if bossHealth == 100:
                bossProjHoriz = 0

            if phase == 1:
                boss.x = player.x
                clock.schedule(BossAttackOne, .50)
            if phase == 2:
                    boss.x = (WIDTH // 2)
                    clock.schedule(BossAttackTwo, .75)
            if Phase == 3:
                boss.x = player.x


        if difficulty == "Hard":

            if 175 <= bossHealth <= 200:
                phase = 1
            elif 140 <= bossHealth <= 175:
                phase = 2
            elif 100 <= bossHealth <= 140:
                phase = 3
            elif 60 <= bossHealth <= 100:
                phase = 4
            elif 20 <= bossHealth <= 60:
                phase = 5
            elif 0 < bossHealth <= 20:
                phase = 6

            if bossHealth == 200:
                bossProjHoriz = 0

            if phase == 1:
                boss.x = player.x
                clock.schedule(BossAttackOne, .35)

            if phase == 2:
                    boss.x = (WIDTH // 2)
                    clock.schedule(BossAttackTwo, .75)


        if bossHealth <= 0:

            game_state = "results"

    if game_state == "results":
        sounds.bossdeath.play(1)

        clock.schedule(BackToMenu, 10.0)


def draw():

    if game_state == "title":
        screen.clear()
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

        for proj in playerProj:
            proj.draw()

        for n in bossProj:
            n.draw()

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
