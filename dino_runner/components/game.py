from dino_runner.components.you_win import show_you_win
import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.game_over import show_game_over
from dino_runner.components.windows import show_windows 
from dino_runner.utils.constants import BG, ICON, LARGE_CACTUS, SCREEN_HEIGHT, SCREEN_WIDTH, SMALL_CACTUS, TITLE, FPS,BIRD
import random
import time
from pygame.sprite import Sprite

obstacles_images = [SMALL_CACTUS[0], SMALL_CACTUS[1], SMALL_CACTUS[2], LARGE_CACTUS[0], LARGE_CACTUS[1], LARGE_CACTUS[2],BIRD[0],BIRD[1]]


class Obstacle:
    
    def __init__(self, image, x, y, speed_game):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 325
        self.speed = speed_game

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class obstacle_2:

    def __init__(self, image, x, y, speed_game):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 300
        self.speed = speed_game

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class obstacle_3:

    def __init__(self, image, x, y, speed_game):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = random.randint(100,300)
        self.step=0
        self.speed = speed_game

    def update(self):
        self.image=BIRD[0] if self.step<=4 else BIRD[1]
        self.rect.x -= self.speed
        self.step+=1
        if self.step==8:
            self.step=0
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
 
class Game:
    dead=0
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.font = pygame.font.Font(None, 36)
        self.score = 20
        self.player = Dinosaur()
         
        self.time_1 = time.time()
        self.obstacles = []
        self.obstacle_on_screen = False
         

    def run(self):

        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        if self.playing == True:
            time_2 = time.time()
            self.score = int(time_2 - self.time_1)
            if self.score==1000:
                show_you_win(self.screen)
            self.game_speed=20+int(self.score*0.01)#para agregar velocidad al juego
             

            #para crear obstaculos
            if not self.obstacle_on_screen:
                image = random.choice(obstacles_images)
                if image==obstacles_images[0] or image==obstacles_images[1] or image==obstacles_images[2]:
                    obstacle = Obstacle(image, SCREEN_WIDTH, 400, self.game_speed)
                    self.obstacles.append(obstacle)
                    self.obstacle_on_screen = True

                elif image==obstacles_images[3] or image==obstacles_images[4] or image==obstacles_images[5]:
                    obstacle = obstacle_2(image, SCREEN_WIDTH, 400, self.game_speed)
                    self.obstacles.append(obstacle)
                    self.obstacle_on_screen = True
                else:
                    obstacle = obstacle_3(image, SCREEN_WIDTH, 400, self.game_speed)
                    self.obstacles.append(obstacle)
                    self.obstacle_on_screen = True
             
                    


            for obstacle in self.obstacles:
                obstacle.update()
                if obstacle.rect.x < -obstacle.rect.width:
                    self.obstacles.remove(obstacle)
                    self.obstacle_on_screen = False
                    break
                if self.player.dino_rect.colliderect(obstacle.rect) and self.dead<3:
                    show_windows(self.screen)
                    self.obstacles.remove(obstacle)
                    self.obstacle_on_screen = False
                    self.dead+=1
                    break
                elif self.player.dino_rect.colliderect(obstacle.rect) and self.dead==3:
                    time.sleep(1)
                    show_game_over(self.screen)
                     
                    break
                     

            if not self.obstacle_on_screen:
                image = random.choice(obstacles_images)
                if image==obstacles_images[0] or image==obstacles_images[1] or image==obstacles_images[2]:
                    obstacle = Obstacle(image, SCREEN_WIDTH, 400, self.game_speed)
                    self.obstacles.append(obstacle)
                    self.obstacle_on_screen = True

                elif image==obstacles_images[3] or image==obstacles_images[4] or image==obstacles_images[5]:
                    obstacle = obstacle_2(image, SCREEN_WIDTH, 400, self.game_speed)
                    self.obstacles.append(obstacle)
                    self.obstacle_on_screen = True
                else:
                    obstacle = obstacle_3(image, SCREEN_WIDTH, 400, self.game_speed)
                    self.obstacles.append(obstacle)
                    self.obstacle_on_screen = True
                    
 

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)

        
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        
        score_text = self.font.render("Score: " + str(self.score), True, (0, 0, 0))
        self.screen.blit(score_text, (SCREEN_WIDTH-150, 10))
        pygame.display.update()

        font = pygame.font.SysFont("Times New Roman Bold Italic", 33)
        deads_text = font.render("DEADS = " + str(self.dead), True, (100,0,0))
        self.screen.blit(deads_text, (10, 10))
        pygame.display.update()



    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
