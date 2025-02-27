import pygame
from dino_runner.utils.constants import DEAD, RUNNING, DUCKING, JUMPING    
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    X_POS = 90
    Y_POS = 310
    JUMP_VEL = 15
    Y_POS_LIMIT = 150


    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS 
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.dino_dead=False


    def process_event(self, user_input):
        if user_input[pygame.K_DOWN]:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False

        elif user_input[pygame.K_UP] or user_input[pygame.K_SPACE]  :
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        
        

    def update(self, user_input):
        self.process_event(user_input)
        if self.dino_duck:
            self.duck()
        elif self.dino_jump:
            self.jump()
        elif self.dino_dead:
            self.dead()
        else:    
            self.run()

        self.step_index = self.step_index + 1
        if self.step_index == 10:
            self.step_index = 0    



    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS + 33
        self.dino_duck = False
        
    def jump(self):
        self.image = JUMPING
        self.dino_rect.x = self.X_POS
        self.dino_rect.y -= self.JUMP_VEL
        if self.dino_rect.y <= self.Y_POS_LIMIT:
            self.JUMP_VEL*= -1
        if self.dino_rect.y > self.Y_POS:
            self.JUMP_VEL *= -1
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False    
    def dead(self):
        self.image=DEAD
        self.dino_dead=True


        

            







        
        




     
            
            

        
    