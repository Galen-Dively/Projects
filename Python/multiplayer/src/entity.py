import pygame

class Entity:
    all_entities = []
    def __init__(self, id, w, h, x, y, color):
        self.id = id
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, w, h)


    def draw(self, screen, camera_offset_x, camera_offset_y):
        x = self.rect.x - camera_offset_x
        y = self.rect.y - camera_offset_y
        pygame.draw.rect(screen, self.color, (x, y, self.rect.w, self.rect.h))


    def update(self):
        pass

    def get_images_from_spritesheet(self, spritesheet):
        sprites = []
        columns = 8
        rows = 1

        # Get the dimensions of the spritesheet
        sheet_width, sheet_height = self.walking_spritesheet.get_size()

        # Calculate the width and height of each sprite
        sprite_width = sheet_width // columns
        sprite_height = sheet_height // rows
        # Extract sprites from the spritesheet
        for row in range(rows):
            for col in range(columns):
                # Define the area to crop (left, top, width, height)
                area = pygame.Rect(col * sprite_width, row * sprite_height, sprite_width, sprite_height)
                # Crop the sprite and add it to the list
                sprite = spritesheet.subsurface(area)
                sprites.append(sprite)

        return sprites
