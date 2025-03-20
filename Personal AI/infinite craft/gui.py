from re import L
import pygame
import infinite_craft

class Item:
    def __init__(self, name):
        self.name = name

    def draw(self, screen):
        pass


class Window:
    def __init__(self):
        self.screen  = pygame.display.set_mode((500, 500))
        self.running = True

        self.items = [Item("Fire"), Item("Water"), Item("Earth"), Item("Air")]


    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            self.draw()

    def draw(self):
        self.screen.fill((255, 255, 0))
        pygame.display.flip()

    
Window().loop()