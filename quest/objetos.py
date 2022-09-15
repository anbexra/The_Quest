
import os

import pygame as pg
import random

from pygame.sprite import Sprite

from . import ALTO, ANCHO, COLOR_BALA, COLOR_FONDO, COLOR_MENSAJE

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

        imagen_asteroide = os.path.join("resources", "images", "asteroide01.png")
        self.imag_aleatoria = random.randrange(3)
        if self.imag_aleatoria == 0:
            self.image = pg.transform.scale(pg.image.load(imagen_asteroide),(100, 100))
        if self.imag_aleatoria == 1:
            self.image = pg.transform.scale(pg.image.load(imagen_asteroide),(50, 50))
        if self.imag_aleatoria == 2:
            self.image = pg.transform.scale(pg.image.load(imagen_asteroide),(25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.velocidad_y = random.randrange(1, 10)
        self.velocidad_x = random.randrange(-5, 5)



    def update(self):
        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x
        if self.rect.top > ALTO + 10 or self.rect.left < -25 or self.rect.right > ANCHO + 25:
            self.rect.x = random.randrange(ANCHO - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.velocidad_y = random.randrange(1, 10)



  
        


    



   
						
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
