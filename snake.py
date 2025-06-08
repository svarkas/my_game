import pygame
import sys
import time
import random

pygame.init()
size = width, height = 600, 400

black = (0, 0, 0)
white = (255, 255, 255)
color = (50, 120, 60)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

title = largeFont.render("Snake", True, white)
titleRect = title.get_rect()
titleRect.center = (width  // 2, 50)

running= True
dice_value = ' '

def draw_dice_value( dice, dice_value ) -> pygame.Rect:
    dice_val = pygame.Rect(0, 0, 40, 40)
    dice_val.center = dice.center
    return dice_val

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    screen.blit(title, titleRect)

    dice_button = pygame.Rect(width - 100, height - 100, 80 , 80)
    dice = mediumFont.render(str(dice_value), True, black)
    dice_rect = dice.get_rect()
    dice_rect.center = dice_button.center
    pygame.draw.rect(screen, white, dice_button)
    screen.blit(dice, dice_rect)
    
    click, _, _ = pygame.mouse.get_pressed()
    if click ==1:
        mouse = pygame.mouse.get_pos()
        if dice_button.collidepoint(mouse):
            dice_value = random.randint(1, 6)
            dice_val = draw_dice_value(dice_button, dice_value)
            pygame.draw.rect(dice, color, dice_val)
    pygame.display.flip()


