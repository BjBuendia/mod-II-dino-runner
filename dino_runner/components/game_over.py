import pygame
import time
from dino_runner.components import game
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

def show_game_over(screen):
    
    popup = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    popup.set_alpha(250)
    popup.fill((225,225,225))
    font = pygame.font.SysFont('Times New Roman Bold Italic', 80)
    message_text = font.render('GAME OVER', True, (100, 0, 0))
    message_rect = message_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    popup.blit(message_text, message_rect)
    screen.blit(popup, (0, 0))
    time.sleep(0.5)
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()