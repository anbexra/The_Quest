import os
import pygame as pg

from pygame.sprite import Sprite
from . import ALTO, ANCHO

class Nave(Sprite):

    margen_inferior = 10
    velocidad = 5
    
    def __init__(self):
        super().__init__()  #Herencia de Sprite
        imagen_nave = os.path.join("resources", "images", "ship.png")
        self.image = pg.image.load(imagen_nave)
        self.rect = self.image.get_rect(midbottom=(ANCHO/2, ALTO - self.margen_inferior))


    def update(self):
        
        tecla = pg.key.get_pressed()
        if tecla[pg.K_RIGHT]:
            self.rect.x += self.velocidad
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO
        if tecla[pg.K_LEFT]:
            self.rect.x -= self.velocidad
            if self.rect.left < 0:
                self.rect.left = 0