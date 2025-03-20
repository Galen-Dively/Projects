from typing import override
import entity
import pygame


class Farmblock(entity.Entity):
    def __init__(self, id, w, h, x, y, color):
        super().__init__(id, w, h, x, y, color)

        images_path = "src/assets/Crops/"
        self.images = [pygame.image.load(f"{images_path}soil_00.png"),
                       pygame.image.load(f"{images_path}soil_01.png"),
                       pygame.image.load(f"{images_path}soil_03.png"),
                       pygame.image.load(f"{images_path}soil_04.png")]
        
        self.current_image = self.images[0]
        
        self.crop = None


    @override
    def draw(self, screen, camera_offset_x, camera_offset_y):
        pass

    def has_crop(self):
        return self.crop

