import pygame
import enum
from startmenu import StartMenu

pygame.init()

class GameState(enum.Enum):
    STARTMENU = 1
    WAITING = 2

class Game:
    def __init__(self):
        self.font = pygame.font.Font("font.ttf", 32)

        self.WIDTH = 800
        self.HEIGHT = 800
        
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.startmenu = StartMenu(self.WIDTH, self.HEIGHT, self.font)

        self.gamestate = GameState.STARTMENU


    def loop(self):
        while True:
            for event in pygame.event.get():
                self.handle_events(event)

            self.screen.fill((1, 1, 111))
            
            self.draw()

            pygame.display.update()


    def draw(self):
        if self.gamestate == GameState.STARTMENU:
            self.startmenu.draw(self.screen)
            
    def handle_events(self, e):
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()

        if self.gamestate == GameState.STARTMENU:
            if self.startmenu.handle_events(e) == 1:
                self.gamestate = GameState.WAITING

Game().loop()