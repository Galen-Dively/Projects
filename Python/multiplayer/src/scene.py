from collections import _OrderedDictValuesView
import re
from turtle import window_height
from typing import override
import pygame
import enum
import world

class ID(enum.Enum):
    START_MENU = 0
    GAME = 1

# Scene is in control of what is drawn
class Scene:
    def __init__(self):
       self.assets = {}
       self.font = pygame.font.Font("src/assets/Fonts/Raleway/static/Raleway-Light.ttf", 48)

    def draw(self):
        """Draw logic for the scene goes here"""
        pass

    def update(self):
        """Update logic for the scene goes here"""
        pass

    def handle_events(self, e):
        """Takes a pygame event and handles it"""
        pass


# Scene that uses a player
class GameScene(Scene):
    player = None
    player_two = None
    network = None
    world = None

    def __init__(self, player, player_two, network):
        super().__init__()
        GameScene.player = player
        GameScene.player_two = player_two
        GameScene.network = network
        GameScene.WINDOW_WIDTH = None
        GameScene.WINDOW_HEIGHT = None
        GameScene.world = world.World(100*16, 100*16)

    @override
    def draw(self, screen, camera_offset_x, camera_offset_y, dt):            # calculate offset
        if not GameScene.WINDOW_HEIGHT or not GameScene.WINDOW_WIDTH:
            GameScene.WINDOW_HEIGHT, GameScene.WINDOW_WIDTH = screen.get_size()

        self.world.draw(screen, camera_offset_x, camera_offset_y)

        # Draw all entities
        GameScene.player.draw(screen, camera_offset_x, camera_offset_y, dt)
        GameScene.player_two.draw(screen, camera_offset_x, camera_offset_y, dt)

    @override
    def update(self, dt):
        GameScene.player.move(dt)
        GameScene.network.send_packet(GameScene.player)

        # Receive and process network packets
        try:
            player_update = self.network.recv_packet(self.player)
            if player_update:
                GameScene.player_two.rect.x = player_update.x
                GameScene.player_two.rect.y = player_update.y
        except Exception as e:
            print(f"Network error: {e}")



class StartMenu(Scene):
    def __init__(self, window_width, window_height):
        super().__init__()
        self.blue_button_image = pygame.image.load("src/assets/UI/Blue Button.png")
        self.blue_button_rect = self.blue_button_image.get_rect()

        # Start Button
        self.start_button_image = pygame.transform.scale(self.blue_button_image, (self.blue_button_rect.w//4, self.blue_button_rect.h//4))
        self.start_button_rect = self.start_button_image.get_rect()
        self.start_button_rect.x = window_width // 2 - self.start_button_rect.w // 2
        self.start_button_rect.y = window_height // 2 - self.start_button_rect.h*3

        # Start Text
        self.start_text = self.font.render("Start", True, (0, 0, 0))

        self.start_text_rect = self.start_text.get_rect()
        self.start_text_rect.center = self.start_button_rect.center


    @override
    def draw(self, screen, camera_offset_x, camera_offset_y, dt):
        screen.blit(self.start_button_image, self.start_button_rect)
        screen.blit(self.start_text, self.start_text_rect)

    @override
    def update(self, dt):
        pass

    @override
    def handle_events(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            return ID.GAME 
        return None


class SceneManger:
    def __init__(self, player, player_two, network, window_height, window_width):
        self.currentscene_id = ID.GAME
        self.currentscene = StartMenu(window_height, window_width)
        self.gamescene = GameScene(player, player_two, network)

    def check_scene(self):
        match self.currentscene_id:
            case ID.GAME:
                self.currentscene = self.gamescene
    
    def draw(self, screen, camera_offset_x, camera_offset_y, dt):
        self.currentscene.draw(screen, camera_offset_x, camera_offset_y, dt)

    def update(self, dt):
        self.currentscene.update(dt)

    def handle_events(self, e):
        event = self.currentscene.handle_events(e)
        if event == None:
            pass
        else:
            self.currentscene_id = event