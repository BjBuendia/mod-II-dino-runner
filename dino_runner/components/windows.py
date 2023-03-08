import pygame
from dino_runner.components import game
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

def show_windows(screen):
    #game.dead+=1
    popup = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    popup.set_alpha(250)
    popup.fill((225,225,225))
    font = pygame.font.SysFont('Times New Roman Bold Italic', 50)

    # Agregar contador
    time_left = 3
    start_time = pygame.time.get_ticks()
    while time_left >= 0:
        popup.fill((225,225,225))
        count_text = font.render('Or wait  ... ' +str(time_left)+' for revive', True, (100, 0, 0))
        count_rect = count_text.get_rect(center=(SCREEN_WIDTH // 2, 500))
        popup.blit(count_text, count_rect)
        
        message_text = font.render('YOU HAS DEAD, PRESS ANY KEY FOR LEAVE', True, (100, 0, 0))
        message_rect = message_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        popup.blit(message_text, message_rect)
        
        screen.blit(popup, (0, 0))
        pygame.display.update()

        current_time = pygame.time.get_ticks()
        time_left = 3 - int((current_time - start_time) / 1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or time_left==0:
                
                playing=True
            if event.type == pygame.KEYDOWN:
                    pygame.quit()
                