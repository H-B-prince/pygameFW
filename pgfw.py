#��, ��� ������ ���� �� ������� ������, �� ������������ �� pygame, � ���� ������ �� ������� ��������(((
from tkinter import CENTER
import pygame
import sys
pygame.init()
pygame.font.init()
count = 0
speed = 5
mode = "menu"
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Для перезапуска нажмите пробел', False, (0, 0, 0))
count_text = my_font.render(str(count), False, (255, 255, 255))
screen = pygame.display.set_mode((600,300))
clock = pygame.time.Clock()
game_over = 0
pygame.display.set_caption("runner")
fon = pygame.image.load("img\\fon.jpg")

alien = pygame.image.load("img\\alien.png")
alien_rect = alien.get_rect()
alien_rect.x = 50
alien_rect.y = 200

box = pygame.image.load("img\\box.png")
box_rect = box.get_rect()
box_rect.x = 550
box_rect.y = 240


bee = pygame.image.load("img\\bee.png")
bee_rect = bee.get_rect()
bee_rect.x = 850
bee_rect.y = 155

play = pygame.image.load("img\\play.png")
play_rect = play.get_rect()
play_rect.x = 200
play_rect.y = 100

go = pygame.image.load("img\\GO.jpg")



def G_O(but):
    global game_over, count, speed
    if game_over == 1 and but == pygame.K_SPACE:
        game_over = 0
        bee_rect.x = 850
        box_rect.x = 550
        alien_rect.x = 50
        count = 0
        speed = 5

def collisions(pos = (0,0)):
    global game_over, mode
    if alien_rect.colliderect(box_rect) or alien_rect.colliderect(bee_rect):
        game_over = 1
    elif play_rect.collidepoint(pos):
        mode= "game"


def enemy_move():
    global count, count_text, box, speed
    if mode != "menu":
        box_rect.x -= speed
        if box_rect.x <=-20:
            box_rect.x = 620
            count+=1
            speed +=1
        bee_rect.x -= speed
        if bee_rect.x <=-20:
            bee_rect.x = 620
            count+=1
            speed +=1
        count_text = my_font.render(str(count), False, (255, 255, 255))



def on_button_down(button):
    global alien_rect
    if button== pygame.K_SPACE or button == pygame.K_w or button == pygame.K_UP:
        alien_rect.y = 60
        while True:
            alien_rect.y += 4
            draw()
            on_button_pressed()
            if alien_rect.y == 200:
                break
            


def on_button_pressed():
    if mode != "menu":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT or pygame.K_a]:
            alien_rect.x -= 5
        elif keys[pygame.K_RIGHT or pygame.K_d]:
            alien_rect.x += 5
        elif keys[pygame.K_DOWN or pygame.K_s]:
            alien_rect.y = 205
        elif not keys[pygame.K_DOWN or pygame.K_s] and alien_rect.y == 205: 
            alien_rect.y = 200




def draw():
    if mode == "game":
        screen.blit(fon,(0,0))
        screen.blit(alien,alien_rect)
        screen.blit(bee,bee_rect)
        screen.blit(box,box_rect)
        screen.blit(count_text, (20,20))
        if game_over == 1:
            screen.blit(go,(0,0))
            screen.blit(text_surface, (70,50))
    elif mode == 'menu':
        screen.blit(fon,(0,0))
        screen.blit(play,play_rect)
    pygame.display.flip()

def update():
    global angle
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key== pygame.K_SPACE or event.key == pygame.K_w:
                    alien_rect.y = 60
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                G_O(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                collisions(pos)
            
        if alien_rect.y <200:
            alien_rect.y += 4
        on_button_pressed()
        enemy_move()
        draw()
        collisions()
        clock.tick(30)
    
#def but_push(but):
#    if but == 


      
update()