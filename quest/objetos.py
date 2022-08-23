import os
import pygame as pg

from pygame.sprite import Sprite

class nave(Sprite):
    
    def __init__(self):
        super().__init__()
        image_path = os.path.join("resources", "images", "ship.png")
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect()


    def update(self):
        pass

