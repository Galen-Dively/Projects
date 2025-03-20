import pygame

pygame.init()

class Hangman:
    def __init__(self):
        WIDTH = 600
        self.stage = 0
        shift_x = 40  # Move the body right by half the bar width

        # Base components (Wider base)
        self.base_rects = [
            pygame.Rect(WIDTH//2 - 60, 400, 120, 12),  # Wider base
            pygame.Rect(WIDTH//2 - 5, 270, 10, 130),   # Vertical rod (raised)
            pygame.Rect(WIDTH//2 - 5, 270, 80, 10)     # Horizontal bar (shorter)
        ]

        # Rope & Head (Shifted right)
        self.rope_rect = pygame.Rect(WIDTH//2 + 30 + shift_x, 280, 5, 35)
        self.head_radius = 12
        self.head_pos = (WIDTH//2 + 32 + shift_x, 315)

        # Chest (Shifted right)
        self.chest_rect = pygame.Rect(WIDTH//2 + 20 + shift_x, 327, 25, 45)

        # Arms (Shifted right)
        self.left_arm = pygame.Rect(WIDTH//2 + shift_x, 337, 25, 8)
        self.right_arm = pygame.Rect(WIDTH//2 + 32 + shift_x, 337, 25, 8)

        # Legs (Shifted right)
        self.left_leg = pygame.Rect(WIDTH//2 + 22 + shift_x, 370, 8, 25)
        self.right_leg = pygame.Rect(WIDTH//2 + 35 + shift_x, 370, 8, 25)

    def draw(self, screen):
        for rect in self.base_rects:
            pygame.draw.rect(screen, (255, 255, 255), rect)

        if self.stage >= 1:
            pygame.draw.rect(screen, (255, 255, 255), self.rope_rect)
        if self.stage >= 2:
            pygame.draw.circle(screen, (255, 255, 255), self.head_pos, self.head_radius)
        if self.stage >= 3:
            pygame.draw.rect(screen, (255, 255, 255), self.chest_rect)
        if self.stage >= 4:
            pygame.draw.rect(screen, (255, 255, 255), self.left_arm)
        if self.stage >= 5:
            pygame.draw.rect(screen, (255, 255, 255), self.right_arm)
        if self.stage >= 6:
            pygame.draw.rect(screen, (255, 255, 255), self.left_leg)
        if self.stage >= 7:
            pygame.draw.rect(screen, (255, 255, 255), self.right_leg)