
import pygame
import os

pygame.mixer.init() # - SOUNDS
pygame.font.init() 

pygame.init()
screen = pygame.display.set_mode(900,500)

WIDTH  = 900
HEIGHT = 500

BULLET_FIRE = pygame.mixer.sound("Assets/Gun+Silencer.mp3")
BULLET_HIT = pygame.mixer.sound("Assets/Grenade+1.mp3")

HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("arial", 80)

RED = (255,0,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

VEL = 5
BULLET_VEL = 6
MAX_BULLET = 3

SHIP_W = 55
SHIP_H = 40

FPS = 60

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

yellowShip = pygame.image.load("Assets/spaceship_yellow.png")
yellowShip = pygame.transform.scale(yellowShip,(SHIP_W, SHIP_H))
yellowShip = pygame.transform.rotate(yellowShip, 90)

redShip = pygame.image.load("Assets/spaceship_red.png")
redShip = pygame.transform.scale(redShip,(SHIP_W, SHIP_H))
redShip = pygame.transform.rotate(redShip, 270)

while True:
    pass