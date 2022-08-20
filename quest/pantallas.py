import os

import pygame as pg

from . import ALTO, ANCHO, COLOR_FONDO, COLOR_TEXTO

class Escena:
    def __init__(self, pantalla: pg.Surface):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()
    
    def bucle_principal(self):
        """Método para cada una de las pantallas"""
        pass


class Portada(Escena):   
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)
       # self.texto = #rellenar con ruta del texto
        font_file = os.path.join("resources", "fonts", "SIXTY.TTF")
        self.tipografia = pg.font.Font(font_file)

    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True
                if event.type == pg.QUIT:
                    pg.quit()
            self.pantalla.fill((COLOR_FONDO))

            self.pintar_cabecera()

            pg.display.flip()       

    def pintar_cabecera(self):
        cabecera = "THE QUEST"
        texto = self.tipografia.render(cabecera, True, COLOR_TEXTO)
        ancho_texto = texto.get_width()
        pos_x = (ANCHO - ancho_texto) / 2
        pos_y = ALTO / 3
        self.pantalla.blit(self.texto, (pos_x, pos_y) )

class Partida(Escena):
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)

    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True
                if event.type == pg.QUIT:
                    pg.quit()
            self.pantalla.fill((COLOR_FONDO))

            pg.display.flip()
            


class HallOfFame(Escena):
    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            self.pantalla.fill((11, 11, 11))
            pg.display.flip()

