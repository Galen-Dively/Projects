import pygame
import player
import entity
import network
import world
import scene

pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("Multiplayer Game")
        self.clock = pygame.time.Clock()

        self.WIDTH = 700
        self.HEIGHT = 700

        self.running = True
        self.fps = 60

        # Initialize players
        self.player = player.Player(1, 50, 50, 50, 50, (0, 0, 55))
        self.player_two_skeleton = player.Player(2, 50, 50, 150, 150, (55, 0, 0))

        self.connected = False

        # Initialize network
        try:
            self.network = network.Client()
            self.network.connect(self.player)
            self.connected = True
        except:
            print("Not connected to server yet")

        self.scene_manager = scene.SceneManger(self.player, self.player_two_skeleton, self.network, self.HEIGHT, self.WIDTH)

    def update(self, dt):
        """Update game state."""
        self.scene_manager.update(dt)

    def draw(self, dt):
        """Draw game objects."""
        self.screen.fill((51, 51, 51))  # Clear screen

        camera_offset_x = scene.GameScene.player.rect.centerx - self.WIDTH // 2
        camera_offset_y = scene.GameScene.player.rect.centery - self.HEIGHT // 2
        # clamp it to the maps boundries
        camera_offset_x = max(0, min(camera_offset_x, scene.GameScene.world.width - self.WIDTH))
        camera_offset_y = max(0, min(camera_offset_y, scene.GameScene.world.height - self.HEIGHT))

        self.scene_manager.draw(self.screen, camera_offset_x, camera_offset_y, dt)

        pygame.display.update()  # Update the display

    def loop(self):
        """Main game loop."""
        while self.running:
            self.scene_manager.check_scene()
            dt = self.clock.tick(self.fps) / 1000  # Delta time in seconds

            # Handle events
            for event in pygame.event.get():
                self.scene_manager.handle_events(event)
                if event.type == pygame.QUIT:
                    self.running = False

            # Update and draw
            self.update(dt)
            self.draw(dt)

        try:
            self.network = network.Client()
            self.network.connect(self.player)
            self.connected = True
        except:
            print("Not connected to server yet")


        # Cleanup
        pygame.quit()
        if self.connected:
            self.network.close()
        print("Game closed.")


if __name__ == "__main__":
    game = Game()
    game.loop()