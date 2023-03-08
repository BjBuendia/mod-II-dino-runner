import pygame
import time
from dino_runner.components import game
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

def show_you_win(screen):
    
    popup = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    popup.set_alpha(250)
    popup.fill((225,225,225))
    font = pygame.font.SysFont('Times New Roman Bold Italic', 100)
    message_text = font.render('congretularios', True, (100, 0, 0))
    message_rect = message_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    font_2 = pygame.font.SysFont('Times New Roman Bold Italic', 50)
    message_text_2 = font_2.render('...you win...', True, (100, 0, 0))
    message_rect_2 = message_text_2.get_rect(center=(SCREEN_WIDTH // 2, 500))

    popup.blit(message_text, message_rect)
    popup.blit(message_text_2, message_rect_2)
    screen.blit(popup, (0, 0))
    time.sleep(0.5)#para el juego
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()