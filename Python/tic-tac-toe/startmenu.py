import pygame


class StartMenu:
    def __init__(self, WIDTH, HEIGHT, font):
        # Host Option
        self.host_button = font.render("Host", True, (255, 255, 255), (0, 0, 0))
        self.host_button_rect = self.host_button.get_rect()
        self.host_button_rect.x = WIDTH/2+self.host_button_rect.w/2
        self.host_button_rect.y = HEIGHT/2+self.host_button_rect.h/2

    def draw(self, screen):
        screen.blit(self.host_button, (self.host_button_rect.x, self.host_button_rect.y))

    def handle_events(self, e):
        if e.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if self.host_button_rect.collidepoint(mouse_pos):
                return 1
        return 0
