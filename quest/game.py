import os
import sys

import pygame as pg

from . import ALTO, ANCHO



class Quest:
    """Arranca el juego"""
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("The Quest")
        pg.mixer.init()

        
    def jugar(self):
        """Inicia el bucle principal"""
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            pg.display.update()


            
            
            

