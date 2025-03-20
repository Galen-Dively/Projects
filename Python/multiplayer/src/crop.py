import pygame
import entity


class Crop(entity.Entity):
    def __init__(self, id, w, h, x, y, color, stages_amt, grow_time):
        super().__init__(id, w, h, x, y, color)
        self.stage = 0
        self.stages_amt = stages_amt
        self.grow_time = grow_time
    
    

