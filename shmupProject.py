import pygame
import random
import math


WIDTH = 500
HEIGHT = 500

easyButton = Actor('easybutton')
easyButton.pos = (WIDTH // 2, 200)
mediumButton = Actor('mediumbutton')
mediumButton.pos = (WIDTH // 2, 250)


player = Actor("player")
player.pos = (WIDTH // 2, 450)
player.xspeed = 0
player.yspeed = 0

boss = Actor("boss")
boss.pos = (WIDTH // 2, 50)
boss.xspeed = 0

playerProjectile = Actor('playerprojectile')
playerProjectile.pos = player.pos
playerProjectile.speed = 0

playerProj = []
bossProj = []

death = 0
t = 0.0
bossHealth = 0
maxHP = 0
phase = 0
difficulty = 0
playerAttack = False
enemyAttack = False

game_state = 'title'


def bossAttackOne(x):


    pass

def on_mouse_down(pos):

    global difficulty
    global game_state
    global bossHealth

    if easyButton.collidepoint(pos):
        difficulty = 'Easy'

        game_state = 'playing'
        bossHealth = 50
        maxHP = bossHealth

    elif mediumButton.collidepoint(pos):
        difficulty = 'Medium'

        game_state = 'playing'
        bossHealth = 100
        maxHP = bossHealth








def update(dt):
    global death
    global t
    global bossHealth
    global phase
    global playerAttack
    global enemyAttack
    global game_state




    if game_state == 'playing':
        t += dt
        player.x += player.xspeed
        player.y += player.yspeed
        playerProjectile.y -= playerProjectile.speed

        if difficulty == 'Easy':
            playerProjectile.speed = 10
        elif difficulty == 'Medium':
            playerProjectile.speed = 8

        if keyboard.space:
            if dt % 2 == 0:
                playerAttack = True

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
            playerProj.append('shoot')
            print(playerProj)

        if playerProjectile.y <= 0:
            playerProj.clear()
            playerProjectile.pos = player.pos
        if playerProjectile.colliderect(boss):
            bossHealth -= 1
            playerProj.clear()
            playerProjectile.pos = player.pos

        if player.colliderect(boss):
            death += 1
            player.pos = (WIDTH // 2, 450)
            boss.pos = (WIDTH // 2, 50)
            bossHealth = maxHP
            print(maxHP)




        boss.x += boss.xspeed
        boss.xspeed = player.xspeed

        if difficulty == 'Easy':
            if bossHealth <= 50 and bossHealth >= 0:
                phase = 1

            if phase == 1:
                pass

        if bossHealth <= 0:
            game_state = 'results'

    elif game_state == 'results':

        game_state = 'title'

def draw():

    if game_state == 'title':
        screen.draw.text( "Select a Difficulty", (175, 150))
        easyButton.draw()
        mediumButton.draw()


    if game_state == 'playing':

        screen.fill((78, 72, 100))
        player.draw()
        boss.draw()

        screen.draw.text('Time: ' + "{:.2f}".format(t), (10, 10))
        screen.draw.text("Attempts: " + str(death), (10, 30))
        screen.draw.text('BossHP: ' + str(bossHealth), (350, 10))

        for n in playerProj:
            playerProjectile.draw()



    elif game_state == 'results':
        pass
