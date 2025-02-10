#!/bin/python3
import pygame
import random
import os, sys
import time
debug = "False"
pygame.init()
width = 800
height = 600
score_value = 0
player_img_name="player.png"
enemy_img_name="enemy.png"
bullet_img_name="bullet.png"
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Galactic Defense | NNOS Games")
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
light_blue = (15, 200, 255)
blue = (0, 0, 255)
assets_dir = "assets"
player_size = (64, 64)
enemy_size = (64, 64)
bullet_size = (40, 40)
def bgm():
    try:
        pygame.mixer.music.load("assets/bgm.mp3")
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(f"Error loading music: {e}")
try:
    icon = pygame.image.load("assets/icon.png")
    pygame.display.set_icon(icon)
except pygame.error as e:
    print(f"Error loading icon: {e}")
try:
    icon_path = os.path.join("assets", "icon.png")
    icon = pygame.image.load(icon_path)
    pygame.display.set_icon(icon)
except pygame.error as e:
    print(f"Error loading icon: {e}")
if "--nobgm" not in sys.argv:
    bgm()
if "--debug" in sys.argv:
    debug = "True"
os.system("clear -xT xterm")
def load_and_scale_image(filename, size):
    filepath = os.path.join(assets_dir, filename)
    try:
        image = pygame.image.load(filepath).convert_alpha()
        return pygame.transform.scale(image, size)
    except FileNotFoundError:
        print(f"Error: Image file '{filename}' not found in '{assets_dir}'")
        pygame.quit()
        exit()
    except pygame.error as e:
        print(f"Error loading image '{filename}': {e}")
        pygame.quit()
        exit()
player_img = load_and_scale_image(player_img_name, player_size)
player_x = width // 2 - player_size[0] // 2
player_y = height - player_size[1]
player_x_change = 0
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
num_enemies = 10
for i in range(num_enemies):
    enemy_img.append(load_and_scale_image(enemy_img_name, enemy_size))
    enemy_x.append(random.randint(0, width - enemy_size[0]))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(1)
bullet_img = load_and_scale_image(bullet_img_name, bullet_size)
bullet_x = 0
bullet_y = player_y + player_size[1] // 2 - bullet_size[1] // 2
bullet_y_change = 5
bullet_state = "ready"
font = pygame.font.Font("freesansbold.ttf", 32)
score_x = 10
score_y = 10
game_over_font = pygame.font.Font("freesansbold.ttf", 64)
block_font = pygame.font.Font("freesansbold.ttf", 64)
def blocktext(text):
    block_text = block_font.render(text, True, light_blue)
    screen.blit(block_text, (width // 2 - 200, height // 2 - 50))
def show_score(x, y):
    if score_value == 100:
        blocktext("Level 2")
    if score_value == 200:
        blocktext("Level 3")
    if score_value == 300:
        blocktext("Level 4")
    if score_value == 400:
        print("Winner")
        time.sleep(1)
        pygame.quit()
        exit()
    score = font.render("Score: " + str(score_value), True, blue)
    screen.blit(score, (x, y))
def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, red)
    screen.blit(game_over_text, (width // 2 - 200, height // 2 - 50))
def player(x, y):
    screen.blit(player_img, (x, y))
def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + bullet_size[0] // 2 - bullet_size[1] // 2, y))
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    enemy_rect = enemy_img[0].get_rect(topleft=(enemy_x, enemy_y))
    bullet_rect = bullet_img.get_rect(topleft=(bullet_x, bullet_y))
    return enemy_rect.colliderect(bullet_rect)
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if debug == "True":
                    print("L")
                player_x_change = -8
            if event.key == pygame.K_RIGHT:
                if debug == "True":
                    print("R")
                player_x_change = 8
            if event.key == pygame.K_SPACE:
                if debug == "True":
                    print("BULLET")
                bullet_x = player_x + player_size[0] // 2 - bullet_size[0] // 2
                fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= width - player_size[0]:
        player_x = width - player_size[0]
    for i in range(num_enemies):
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 1
            enemy_y[i] += 40
        elif enemy_x[i] >= width - enemy_size[0]:
            enemy_x_change[i] = -1
            enemy_y[i] += 40
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            if debug == "True":
                print("BULLET/COLLISION")
            bullet_y = player_y + player_size[1] // 2 - bullet_size[1] // 2
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, width - enemy_size[0])
            enemy_y[i] = random.randint(50, 150)
            enemy_x_change[i] = random.choice([-1, 1])
        if enemy_y[i] > height:
            game_over()
            running = False
            break
    if bullet_state == "fire":
        bullet_y -= bullet_y_change
        fire_bullet(bullet_x, bullet_y)
    if bullet_y <= 0:
        bullet_y = player_y + player_size[1] // 2 - bullet_size[1] // 2
        bullet_state = "ready"
    screen.fill(black)
    player(player_x, player_y)
    for i in range(num_enemies):
        enemy(enemy_x[i], enemy_y[i], i)
    show_score(score_x, score_y)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
