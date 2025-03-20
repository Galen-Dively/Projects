import pygame

class WaitingMenu:
    def __init__(self, WIDTH, HEIGHT, font):
        self.waiting_text = font.render("Waiting...", True, (255, 255, 255))
        self.waiting_text_rect = self.waiting_text.get_rect()
        self.waiting_text_rect.x = 100
        self.waiting_text_rect.y = 100

    def draw(self, screen):
        pass
