import os

import pygame as pg

from . import ALTO, ANCHO
from quest.pantallas import Pantalla, Portada, Partida, HallOfFame


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
            HallOfFame(self.pantalla),
        ]
        
    def jugar(self):
        """Inicia el bucle principal"""
        for pantalla in self.pantallas:
            pantalla.bucle_principal()
            
            
            

