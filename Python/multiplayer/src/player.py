from typing import override
import pygame
import entity
import enum

pygame.init()

class AnimationState(enum.Enum):
    WALKING = 0


class Player(entity.Entity):
    def __init__(self, player_id, w, h, x, y, color):
        super().__init__(1, w, h, x, y, color)
        self.speed = .5 * 1000

        # Animation
        self.idle_spritesheet_path = 0
        self.walking_spritesheet = pygame.image.load("src/assets/Characters/Human/WALKING/base_walk_strip8.png")
    

        self.time_since_last_frame = 0
        self.walking_spritesheet_images = self.get_images_from_spritesheet(self.walking_spritesheet)

        self.current_animation_frame = 0
        self.current_animation_images = self.walking_spritesheet_images

        self.rect = self.current_animation_images[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        print(self.rect)

    def move(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= self.speed * dt
        elif keys[pygame.K_s]:
            self.rect.y += self.speed * dt
        elif keys[pygame.K_a]:
            self.rect.x -= self.speed * dt
        elif keys[pygame.K_d]:
            self.rect.x += self.speed * dt

    @override
    def draw(self, screen, camera_offset_x, camera_offset_y, dt):
        screen_x = self.rect.x - camera_offset_x
        screen_y = self.rect.y - camera_offset_y

        self.animate(dt)
        scale_x, scale_y = self.current_animation_images[self.current_animation_frame].get_size()
        scale_factor = 2
        transformed = pygame.transform.scale(self.current_animation_images[self.current_animation_frame], (scale_x*scale_factor, scale_y*scale_factor))
        screen.blit(transformed, (screen_x, screen_y))

    def animate(self, dt):
        self.time_since_last_frame += dt
        if self.time_since_last_frame >= .1:
            self.time_since_last_frame = 0
            self.current_animation_frame = (self.current_animation_frame + 1) % len(self.walking_spritesheet_images)