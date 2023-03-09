import pygame
import time
from dino_runner.components import game
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

def show_game_over(screen):
    
    popup = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    popup.set_alpha(250)
    popup.fill((225,225,225))

    font = pygame.font.SysFont('Times New Roman Bold Italic', 100)
    message_text = font.render('GAME OVER', True, (100, 0, 0))
    message_rect = message_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    popup.blit(message_text, message_rect)

    font_3 = pygame.font.SysFont('Times New Roman Bold Italic', 50)
    message_text_3 = font_3.render('press anykeyboard for replay', True, (100, 0, 0))
    message_rect_3 = message_text_3.get_rect(center=(SCREEN_WIDTH // 2, 500))
    popup.blit(message_text_3, message_rect_3)

    screen.blit(popup, (0, 0))
    time.sleep(1)
    pygame.display.update()

    


    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            elif event.type == pygame.KEYDOWN:
                new_game = game.Game()
                new_game.run()
        
        
        pygame.display.update()