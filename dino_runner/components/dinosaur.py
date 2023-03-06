import pygame
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING    
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    X_POS = 90
    Y_POS = 310
    JUMP_SPEED = 7.5
    #GRAVITY = 7.5

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS 
        self.step = 2
        self.is_jumping = False
        self.jump_speed = self.JUMP_SPEED
        self.y_vel = 0

    def update(self, user_input):
        if user_input[pygame.K_DOWN]:
            self.duck()
        elif user_input[pygame.K_UP]:
            self.jump()
        else:    
            self.run()

        self.step += 1
        if self.step == 10:
            self.step = 0

        if self.is_jumping:
            self.y_vel += self.JUMP_SPEED
            self.dino_rect.y += self.y_vel
            if self.dino_rect.y >= self.Y_POS:
                self.dino_rect.y = self.Y_POS
                self.is_jumping = False
                self.jump_speed = self.JUMP_SPEED
                self.y_vel = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image = RUNNING[0] if self.step < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def duck(self):
        self.image = DUCKING[0] if self.step < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS + 33
        
    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_speed = self.JUMP_SPEED*4
            self.y_vel = -self.jump_speed
        else:
            self.y_vel -= self.jump_speed*45
            self.jump_speed -= 1






        
        




     
            
            

        
    