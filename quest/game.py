import sys, random, os
import pygame as pg

from quest import ALTO, ANCHO, C_B
from objetos import Nave 

class Quest:
    """Arranca el juego"""
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("The Quest")
        pg.mixer.init()
        
    def jugar (self):
        """Inicia el bucle principal"""
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            pg.display.flip()
            

