import pygame
import sys
import time
import random
import os

pygame.joystick.init()

os.chdir(os.path.abspath(__file__)[:-7])

class BUSCOPAN():
    def __init__(self, y=0, sand=1):
        
        self.color = sand
        if self.color==2:
            self.foto = buscopanlaranja
        elif self.color == 3:
            self.foto = buscopanroxo
        else : self.foto = buscopanverde
        self.x = -100
        self.y = y
        self.rect = self.foto.get_rect()
        
    def movimento(self):
        self.rect.topleft = (self.x,self.y)
        self.x += 5


class PILULADODIASEGUINTE():
    def __init__(self, y):
        self.foto = pygame.image.load("piluladodiaseguinte.png").convert_alpha()
        self.rect = self.foto.get_rect()
        self.rect.y = y
        self.x = -300
        self.y = y
    def movimento(self):
        self.rect.topleft = (self.x,self.y)
        self.x += 5
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]


pygame.mixer.init()
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)


bomb = pygame.mixer.music.load("bomb.mp3")
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menstruação")




icon = pygame.image.load("blood.png").convert_alpha()
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

buscopanverde = pygame.image.load("buscopanfacil.png").convert_alpha()
buscopanlaranja = pygame.image.load("buscopanmedio.png").convert_alpha()
buscopanroxo = pygame.image.load("buscopandificil.png").convert_alpha()



cenario = pygame.image.load("vagina.png").convert()
gameoverscreen = pygame.image.load("gameoverscreen.png").convert()
player_icon = pygame.image.load("player.png").convert_alpha()
player_icon = pygame.transform.scale(player_icon, (player_icon.get_width() * 4, player_icon.get_height() * 4))
player_rect = player_icon.get_rect()

telinhado69 = pygame.image.load("sexosexosexo.png").convert()

player_rect.x, player_rect.y = 640, 360
xspeed, yspeed = 0, 0
speed = 7
friction = 0.25





hp = 15

inimigos = []
pilulas = []


tic = 0
def spawnbitches():
    global tic
    inimigos.append(BUSCOPAN(random.randint(0,621), random.randint(1,3)))
    tic = time.time()
    pilulas.append(PILULADODIASEGUINTE(random.randint(0,665)))
spawnbitches()








bottaoerre = my_font.render("clique R/Start para jogar de novo", False, (0, 0, 0))

pontos = 69
ready = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        keys = pygame.key.get_pressed()
    if ready:
        xspeed = (keys[pygame.K_RIGHT] or keys[pygame.K_d]) * speed - (keys[pygame.K_LEFT] or keys[pygame.K_a]) * speed
        yspeed = (keys[pygame.K_DOWN] or keys[pygame.K_s]) * speed - (keys[pygame.K_UP] or keys[pygame.K_w]) * speed

    


        text_surface = my_font.render(f"{hp}/15   Pontos : {pontos}", False, (0, 0, 0))

        player_rect.x += xspeed
        player_rect.y += yspeed

        if player_rect.x > 1152: player_rect.x -= 7
        if player_rect.x < 0: player_rect.x += 7
        if player_rect.y < 0: player_rect.y += 7
        if player_rect.y > 592: player_rect.y -= 7

        player_rect.x+=joysticks[0].get_axis(3)*7
        player_rect.y+=joysticks[0].get_axis(4)*7
        player_rect.x+=joysticks[0].get_axis(0)*7
        player_rect.y+=joysticks[0].get_axis(1)*7

        if xspeed > 0:
            xspeed = max(0, xspeed - friction)
        elif xspeed < 0:
            xspeed = min(0, xspeed + friction)
        
        if yspeed > 0:
            yspeed = max(0, yspeed - friction)
        elif yspeed < 0:
            yspeed = min(0, yspeed + friction)
            



        screen.blit(cenario, (0, 0))
        screen.blit(player_icon, player_rect)
        screen.blit(text_surface, (0,0))
        for i in inimigos:
            i.movimento()
            screen.blit(i.foto, i.rect)
            if i.x > 1280: inimigos.remove(i)
            if player_rect.colliderect(i):
                inimigos.remove(i)
                hp -= i.color
                #pygame.mixer.music.play()

        for i in pilulas:
            i.movimento()
            screen.blit(i.foto, i.rect)
            if i.rect.x > 1280: pilulas.remove(i)
            if player_rect.colliderect(i): pilulas.remove(i); pontos += 1 




        pygame.display.flip()
        if time.time() - tic > 2:
            spawnbitches() 

    if hp <= 0:
        ready = False     
        screen.blit(gameoverscreen, (0,0))
        screen.blit(bottaoerre, (10, 640))
        pygame.display.flip()

        if keys[pygame.K_r] or joysticks[0].get_button(9):
            pontos = 0
            hp = 15
            ready = True
            player_rect.x = 640
            player_rect.y = 360
    if pontos >= 69:
        ready = False 
        screen.blit(telinhado69, (0,0))
        screen.blit(bottaoerre, (10, 640))
        pygame.display.flip()
        if keys[pygame.K_r] or joysticks[0].get_button(9):
            pontos = 0
            hp = 15
            ready = True
            player_rect.x = 640
            player_rect.y = 360
    clock.tick(60)