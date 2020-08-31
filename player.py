import pygame

main_char = pygame.image.load('images/mainChar.bmp')
main_char_rect = main_char.get_rect()
main_char_x, main_char_y = windowSize[1] / 2, windowSize[0] / 2
main_char_height, main_char_width = main_char_rect.height, main_char_rect.width

# Draw main char to screen.
# screen.blit(main_char, main_char_rect)
pygame.draw.rect(gameWin, main_char_rect, (main_char_x, main_char_y, main_char_height, main_char_width)) 