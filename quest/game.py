import os

import pygame as pg

from . import ALTO, ANCHO
from quest.escenas import Portada, Partida, HallOfFame


class Quest:
    """Arranca el juego"""
    def __init__(self):
        pg.init()
        self.display = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("The Quest")
        #pg.mixer.init()

        self.escenas = [
            Portada(self.display),
            Partida(self.display),
            HallOfFame(self.display)
        ]
        
    def jugar(self):
        """Inicia el bucle principal"""
        for escena in self.escenas:
            escena.bucle_principal()

"""Creado la pantalla,
     proximo paso es hacer que se abran las 3 pantallas diferentes

     no reconoce bucle principal
"""       
            
            

