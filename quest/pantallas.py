import os

import pygame as pg

from . import ALTO, ANCHO, COLOR_FONDO, COLOR_TEXTO, COLOR_MENSAJE

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
        font_file = os.path.join("resources", "fonts", "QUARANTINE REGULATIONS.otf")
        font_file1 = os.path.join("resources", "fonts", "Spacesky.otf")
        self.tipografia = pg.font.Font(font_file, 77)
        self.t_instrucciones =pg.font.Font(font_file1, 22)

    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True
                if event.type == pg.QUIT:
                    pg.quit()
            self.pantalla.fill((COLOR_FONDO))
            self.pintar_fondo()
            self.pintar_cabecera()
            self.pintar_texto()
            pg.display.flip()  

    def pintar_fondo(self):
        self.fondo = pg.image.load(os.path.join("resources", "images", "espacio.jpg")).convert()    
        self.pantalla.blit(self.fondo,(0, 0)) 

    def pintar_cabecera(self):
        mensaje = "THE QUEST"
        texto = self.tipografia.render(mensaje, True, COLOR_TEXTO)
        ancho_texto = texto.get_width()
        pos_x = (ANCHO - ancho_texto) / 2
        pos_y = ALTO / 4
        self.pantalla.blit(texto, (pos_x, pos_y) )

    def pintar_texto(self):
        mensaje = "Pulse tecla 'ESPACIO' para comenzar"
        texto = self.t_instrucciones.render(mensaje, True, COLOR_MENSAJE)
        ancho_texto = texto.get_width()
        pos_x = (ANCHO - ancho_texto)/2
        pos_y = ALTO - 75
        self.pantalla.blit(texto, (pos_x, pos_y))



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
            self.pintar_fondo()
            
            pg.display.flip()

    def pintar_fondo(self):
        self.fondo = pg.image.load(os.path.join("resources", "images", "espacio.jpg")).convert()    
        self.pantalla.blit(self.fondo,(0, 0))             


class HallOfFame(Escena):
    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            self.pantalla.fill((11, 11, 11))
            pg.display.flip()

