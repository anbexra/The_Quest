import os
import sys

import pygame as pg

from . import ALTO, ANCHO
from quest.pantallas import Portada, Partida, HallOfFame


class Quest:
    """Arranca el juego"""
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("The Quest")
        pg.mixer.init()
        self.pantallas = [
            Portada(self.pantalla),
            Partida(self.pantalla),
            HallOfFame(self.pantalla)
        ]


        
    def jugar(self):
        """Inicia el bucle principal"""
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            pg.display.update()


     """Creado la pantalla,
     proximo paso es hacer que se abran las 3 pantallas diferentes
     """       
            
            

