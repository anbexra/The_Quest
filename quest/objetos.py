import pygame, random, os
import pygame as pg

from quest import C_B, ANCHO, ALTO

class Nave(pg.sprite.sprite):
    """Clase para gestionar la nave"""

    def __init__(self):
        super().init()
        self.image = pg.image.load(os.path.join("resources/Images/images/nave.png")).convert()
        self.image.set_colorkey(C_B)
        self.rect = self.rect.image.get_rect()
        self.rect.centerx = ANCHO // 2
        self.rect.bottom = ALTO - 10
        self.velocidad_nave = 5
