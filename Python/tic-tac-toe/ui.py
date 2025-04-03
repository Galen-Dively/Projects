import pygame


class Menu:
    def __init__(self, width, height, font):
        self.w = width
        self.h = height
        self.font = font


class StartMenu:
    def __init__(self, w, h, font):
        super.__init__(w, h, font)
        # Host Option
        self.host_button = self.font.render("Host", True, (255, 255, 255), (0, 0, 0))
        self.host_button_rect = self.host_button.get_rect()
        self.host_button_rect.x = self.w/2+self.host_button_rect.w/2
        self.host_button_rect.y = self.h/2+self.host_button_rect.h/2

    def draw(self, screen):
        screen.blit(self.host_button, (self.host_button_rect.x, self.host_button_rect.y))

    def handle_events(self, e):
        if e.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if self.host_button_rect.collidepoint(mouse_pos):
                return 1
        return 0


class HostMenu:
    def __init__(self, w, h, f):
        super().__init__(w, h, f)
        self.port_text()
        pass

class WaitingMenu:
    def __init__(self, WIDTH, HEIGHT, font):
        self.waiting_text = font.render("Waiting...", True, (255, 255, 255))
        self.waiting_text_rect = self.waiting_text.get_rect()
        self.waiting_text_rect.x = 100
        self.waiting_text_rect.y = 100

    def draw(self, screen):
        pass
