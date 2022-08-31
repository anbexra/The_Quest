
import os

import pygame as pg

from pygame.sprite import Sprite
from . import ALTO, ANCHO, COLOR_BALA, COLOR_MENSAJE

class Nave(Sprite):

    margen_inferior = 10
    velocidad = 5
    
    def __init__(self):
        super().__init__()  #Herencia de Sprite
        imagen_nave = os.path.join("resources", "images", "ship.png")
        self.image = pg.image.load(imagen_nave)
        self.rect = self.image.get_rect(midbottom=(ANCHO/2, ALTO - self.margen_inferior))


    def mover_nave(self):
        "para mover la nave por la pantalla"
        tecla = pg.key.get_pressed()
        if tecla[pg.K_RIGHT]:
            self.rect.x += self.velocidad
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO
        if tecla[pg.K_LEFT]:
            self.rect.x -= self.velocidad
            if self.rect.left < 0:
                self.rect.left = 0

    
    def update(self):           
        self.mover_nave()

class Asteroide(Sprite):
    def __init__(self):
        super().__init__()

        asteroide = os.path.join("resources", "images", "asteroide01.png")
        self.image = pg.image.load(asteroide)    
        self.rect = self.image.get_rect()



   
						
class Marcador():
    def __init__(self):
        self.valor = 0
        font_file = os.path.join("resources", "fonts", "SIXTY.TTF")
        self.tipografia = pg.font.Font(font_file, 20)

    def sumar(self, puntos):
        self.valor += puntos
    
    def pintar_marcador(self, pantalla):
        """Muestra el marcador de puntos"""
        mensaje = f"Puntos: {self.valor}"
        texto = self.tipografia.render(mensaje, True, COLOR_MENSAJE)
        pos_x =texto.get_width() - 40
        pos_y = texto.get_height() + 25
        pantalla.blit(texto, (pos_x, pos_y))

class ContadorVidas():
    def __init__(self, vidas_iniciales):
        self.vidas = vidas_iniciales
        font_file = os.path.join("resources", "fonts","SIXTY.TTF" )
        self.tipografia = pg.font.Font(font_file, 20)

    def perder_vidas(self):
        self.vidas -= 1
        return self.vidas < 1

    def pintar_contador(self, pantalla):
        texto_contador = f"Vidas: {self.vidas}"
        mensaje = self.tipografia.render(texto_contador,
        True, COLOR_MENSAJE)
        pos_x = mensaje.get_width() + 650
        pos_y = mensaje.get_height() + 25
        pantalla.blit(mensaje, (pos_x, pos_y))
