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
bossWait = False

Projectiles = pygame.sprite.Group()


def on_mouse_down(pos):

    global difficulty
    global game_state
    global bossHealth
    global playerSpeed
    global bossSpeed

    if easyButton.collidepoint(pos):
        if game_state == 'title':
            difficulty = "Easy"
            game_state = "playing"
            bossHealth = 50
            maxHP = 100
            playerSpeed = 10
            bossSpeed = 3
            #music.play('battle1')

    elif mediumButton.collidepoint(pos):
        if game_state == 'title':
            difficulty = "Medium"
            game_state = "playing"
            bossHealth = 100
            maxHP = 100
            playerSpeed = 8
            bossSpeed = 5
            #music.play('battle1')

    elif hardButton.collidepoint(pos):
        if game_state == 'title':
            difficulty = "Hard"
            game_state = "playing"
            bossHealth = 200
            maxHP = 200
            playerSpeed = 6
            bossSpeed = 8
            #music.play('battle2')


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





def BossAttackOne(x):
    global bossSpeed
    global bossShoot
    if bossShoot:
        bossProj.append(Actor('bossprojectile'))
        bossProj[-1].pos = boss.pos
        bossShoot = False

        clock.schedule(BossShoot, x)

    for proj in bossProj:
            proj.y += bossSpeed
            if proj.y >= HEIGHT:
                bossProj.remove(proj)

def BossAttackTwo(x):
    global bossSpeed
    global bossShoot
    global bossProjHoriz
    bossProjHoriz = 5
    if bossShoot:
        bossProj.append(Actor('bossprojectile'))
        bossProj[-1].pos = boss.pos
        bossProj[-1].xspeed = random.randint(-5, 5)
        bossShoot = False

        clock.schedule(BossShoot, x)

    for proj in bossProj:

            if proj:
                proj.y += bossSpeed

                proj.x += proj.xspeed
                if proj.x >= WIDTH:
                    proj.xspeed *= -1
                elif proj.x <= 0:
                    proj.xspeed *= -1
                if proj.y >= HEIGHT:
                    bossProj.remove(proj)



def BossAttackThree(x):
    global bossSpeed
    global bossShoot
    global bossSpeed
    global bossShoot
    if bossShoot:
        bossProj.append(Actor('bossprojectile'))
        bossProj[-1].pos = boss.pos
        bossShoot = False

        clock.schedule(BossShoot, x)


    for proj in bossProj:
        if proj.x < player.x:
            proj.x += 1
        elif proj.x > player.x:
            proj.x -= 1

        if proj.y < player.y:
            proj.y += 1
        elif proj.y > player.y:
            proj.y -= 1

def BossAttackFour(x):
    global bossSpeed
    global bossShoot
    global bossProjHoriz
    bossProjHoriz = 5
    if bossShoot:
        n = random.randint(4, 9)
        for k in range(n):
            bossProj.append(Actor('bossprojectile'))
            bossProj[-1].pos = boss.pos

            bossProj[-1].xspeed = random.randint(-5, 5)
            bossShoot = False

        clock.schedule(BossShoot, x)

    for proj in bossProj:

            if proj:
                if bossSpeed - abs(proj.xspeed) <= 0:
                    proj.y += 1

                else:
                    proj.y += bossSpeed - abs(proj.xspeed)

                proj.x += proj.xspeed
                if proj.x >= WIDTH:
                    proj.xspeed *= -1
                elif proj.x <= 0:
                    proj.xspeed *= -1
                if proj.y >= HEIGHT:
                    bossProj.remove(proj)





def BackToMenu():
    global game_state
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
    global bossWait
    global bossSpeed

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
            BossShoot()
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
                BossAttackOne(.75)



        if difficulty == "Medium":

            if 70 <= bossHealth <= 100:
                phase = 1
            elif 40 <= bossHealth <= 70:
                phase = 2
            elif 0 < bossHealth <= 40:
                phase = 3

            if bossHealth == 70 or bossHealth == 40:
                bossWait = False

            if bossHealth == 100:
                bossProjHoriz = 0

            if phase == 1:
                boss.x = player.x
                BossAttackOne(.50)
            if phase == 2:
                    boss.x = player.x
                    if bossWait:
                        BossAttackTwo(.75)
                    else:
                        if bossProj == []:
                            bossWait = True
                        else:
                            bossWait = False
                            for proj in bossProj:
                                proj.y += bossSpeed
                                if proj.y >= HEIGHT:
                                    bossProj.remove(proj)
            if phase == 3:
                if boss.x < (WIDTH // 2):
                    boss.x += 1
                elif boss.x > (WIDTH // 2):
                    boss.x -= 1

                if bossWait:
                    BossAttackFour(2.0)
                else:
                    if bossProj == []:
                        bossWait = True
                    else:
                        bossWait = False
                        for proj in bossProj:
                            proj.y += bossSpeed
                            proj.x += proj.xspeed
                            if proj.x >= WIDTH:
                                proj.xspeed *= -1
                            elif proj.x <= 0:
                                proj.xspeed *= -1
                            if proj.y >= HEIGHT:
                                bossProj.remove(proj)


        if difficulty == "Hard":

            if 190 <= bossHealth <= 200:
                phase = 1
            elif 160 <= bossHealth <= 190:
                phase = 2
            elif 110 <= bossHealth <= 160:
                phase = 3
            elif 100 <= bossHealth <= 110:
                phase = 4
            elif 50 <= bossHealth <= 100:
                phase = 5
            elif 20 < bossHealth <= 50:
                phase = 6
            elif 0 < bossHealth <= 20:
                phase = 7

            if bossHealth == 190 or bossHealth == 160 or bossHealth == 190:
                bossWait = False

            if bossHealth == 200:
                bossProjHoriz = 0

            if phase == 1:
                boss.x = player.x
                BossAttackOne(.25)

            if phase == 2:
                if boss.x < (WIDTH // 2):
                    boss.x += 1
                elif boss.x > (WIDTH // 2):
                    boss.x -= 1


                if bossWait:
                    BossAttackFour(.90)
                else:
                    if bossProj == []:
                        bossWait = True
                    else:
                        bossWait = False
                        for proj in bossProj:
                            proj.y += bossSpeed
                            if proj.y >= HEIGHT:
                                bossProj.remove(proj)






            if phase == 3:
                boss.x = (WIDTH // 2)
                if bossWait:
                    BossAttackThree(3.0)
                else:
                    if bossProj == []:
                        bossWait = True
                    else:

                        for proj in bossProj:
                            proj.y += bossSpeed
                            if proj.y >= HEIGHT:
                                bossProj.remove(proj)


        if bossHealth <= 0:
            sounds.bossdeath.play(0)
            game_state = "results"

    if game_state == "results":
        music.fadeout(5.0)


        clock.schedule(BackToMenu, 10.0)


def draw():

    if game_state == "title":
        screen.clear()
        screen.draw.text("Select a Difficulty", (175, 150))
        easyButton.draw()
        mediumButton.draw()
        hardButton.draw()

    if game_state == "playing":
        screen.clear()
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
