import pygame
import sys
import time
import random
import copy

pygame.init()
size = width, height = 1024, 768 

black = (0, 0, 0)
white = (255, 255, 255)
dice_dots_rgb = (227, 39, 14)
odd_rgb = (47, 156, 168)
even_rgb = (106, 168, 47)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)


running= True
dice_value = ' '

def draw_dice_value( dice, dice_value ) -> list[pygame.Rect]:
    dots = []
    dice_val = pygame.Rect(0, 0, 15, 15)
    dice_val.center = (dice.topleft[0]+20, dice.topleft[1]+20)
    if dice_value == 1:
        dice_val.center = dice.center
        dots.append(dice_val)
    elif dice_value == 2:
        dice_val.center = (dice.topleft[0]+20, dice.topleft[1]+20)
        dots.append(copy.deepcopy(dice_val))
        dice_val.center = (dice.bottomright[0]-20, dice.bottomright[1]-20)
        dots.append(copy.deepcopy(dice_val))
    elif dice_value == 3:
        dice_val.center = (dice.topleft[0]+20, dice.topleft[1]+20)
        dots.append(copy.deepcopy(dice_val))
        dice_val.center = dice.center
        dots.append(copy.deepcopy(dice_val))
        dice_val.center = (dice.bottomright[0]-20, dice.bottomright[1]-20)
        dots.append(copy.deepcopy(dice_val))
    elif dice_value == 4:
        dice_val.center = (dice.topleft[0]+20, dice.topleft[1]+20)
        dots.append(copy.deepcopy(dice_val))
        dice_val.center = (dice.topright[0]-20, dice.topright[1]+20)
        dots.append(copy.deepcopy(dice_val))
        dice_val.center = (dice.bottomleft[0]+20, dice.bottomleft[1]-20)
        dots.append(copy.deepcopy(dice_val))
        dice_val.center = (dice.bottomright[0]-20, dice.bottomright[1]-20)
        dots.append(copy.deepcopy(dice_val))
    elif dice_value == 5:
        dice_val.center = (dice.topleft[0]+20, dice.topleft[1]+20)
        dots.append(copy.deepcopy(dice_val))
        dice_val.center = (dice.topright[0]-20, dice.topright[1]+20)
        dots.append(copy.deepcopy(dice_val))
        dice_val.center = dice.center
        dots.append(copy.deepcopy(dice_val))
        dice_val.center = (dice.bottomleft[0]+20, dice.bottomleft[1]-20)
        dots.append(copy.deepcopy(dice_val))
        dice_val.center = (dice.bottomright[0]-20, dice.bottomright[1]-20)
        dots.append(copy.deepcopy(dice_val))
    elif dice_value == 6:
        dice_val.center = (dice.topleft[0]+20, dice.topleft[1]+20)
        dots.append(copy.deepcopy(dice_val))
        dice_val.center = (dice.topleft[0]+40, dice.topleft[1]+20)
        dots.append(copy.deepcopy(dice_val))
        dice_val.center = (dice.topright[0]-20, dice.topright[1]+20)
        dots.append(copy.deepcopy(dice_val))
        dice_val.center = (dice.bottomleft[0]+20, dice.bottomleft[1]-20)
        dots.append(copy.deepcopy(dice_val))
        dice_val.center = (dice.bottomleft[0]+40, dice.bottomleft[1]-20)
        dots.append(copy.deepcopy(dice_val))
        dice_val.center = (dice.bottomright[0]-20, dice.bottomright[1]-20)
        dots.append(copy.deepcopy(dice_val))
    return dots 

title = largeFont.render("Snake", True, white)
titleRect = title.get_rect()
titleRect.center = (width  // 2, 50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

    screen.fill(black)
    screen.blit(title, titleRect)

    # Exit Button
    exit_button = pygame.Rect(0, height - 40, 80, 40)   
    exit_label = mediumFont.render('EXIT', True, black)
    exit_label_rect = exit_label.get_rect(center=exit_button.center)
    pygame.draw.rect(screen, white, exit_label_rect)
    screen.blit(exit_label, exit_label_rect)  
    
    dice_button = pygame.Rect(width - 100, height - 100, 80 , 80)
    dice = mediumFont.render(str(dice_value), True, black)
    dice_rect = dice.get_rect()
    dice_rect.center = dice_button.center
    pygame.draw.rect(screen, white, dice_button)
    
    click, _, _ = pygame.mouse.get_pressed()
    if click ==1:
        mouse = pygame.mouse.get_pos()
        if exit_button.collidepoint(mouse):
            running = False
        elif dice_button.collidepoint(mouse):
            dice_value = random.randint(1, 6)
    dice_dots = draw_dice_value(dice_button, dice_value)
    for dot in dice_dots:
        pygame.draw.rect(screen, dice_dots_rgb, dot)
    
    for i in range(1, 10, 1):
        path_rect = pygame.Rect(0*(1+i), 80, 80, 80)
        pygame.draw.rect(screen, odd_rgb, path_rect)
    #path_rect = pygame.Rect (80, 80, 80, 80)
    #pygame.draw.rect(screen, even_rgb, path_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()

