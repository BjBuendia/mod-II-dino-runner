import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.constants import BG, ICON, LARGE_CACTUS, SCREEN_HEIGHT, SCREEN_WIDTH, SMALL_CACTUS, TITLE, FPS,BIRD
import random
import time

obstacles_images = [SMALL_CACTUS[0], SMALL_CACTUS[1], SMALL_CACTUS[2], LARGE_CACTUS[0], LARGE_CACTUS[1], LARGE_CACTUS[2],BIRD[0]]


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


class Game:
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
        self.score = 0
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
            if not self.obstacle_on_screen:
                image = random.choice(obstacles_images)
                obstacle = Obstacle(image, SCREEN_WIDTH, 400, self.game_speed)
                self.obstacles.append(obstacle)
                self.obstacle_on_screen = True


            for obstacle in self.obstacles:
                obstacle.update()
                if obstacle.rect.x < -obstacle.rect.width:
                    self.obstacles.remove(obstacle)
                    self.obstacle_on_screen = False
                    break
                #if self.player.rect.colliderect(obstacle.rect):
                    #time.sleep(0.5)
                    #self.playing = False


            if not self.obstacle_on_screen:
                image = random.choice(obstacles_images)
                obstacle = Obstacle(image, SCREEN_WIDTH, 400, self.game_speed)
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
        self.screen.blit(score_text, (950, 10))
        pygame.display.update()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
