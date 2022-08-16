import sys

import pygame as pg

class Pantalla:
    def __init__(self, pantalla: pg.surface):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()
    
    def bucle_principal(self):
        """Método para cada una de las pantallas, dependiendo de su función """
        pass


class Portada(Pantalla):
    def __init__(self, pantalla: pg.surface):
        super().__init__(pantalla)


    def bucle_principal(self):
        
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
            self.pantalla.fill((255,255,255))
            pg.display.flip()
            pg.display.update()


class Partida(Pantalla):
    def __init__(self, pantalla: pg.surface):
        super().__init__(pantalla)

    def bucle_principal(self):
        
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.pantalla.fill((99, 99, 99))
            pg.display.flip()
            pg.display.update()


class HallOfFame(Pantalla):
    def __init__(self, pantalla: pg.surface):
        super().__init__(pantalla)

    def bucle_principal(self):
    
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.pantalla.fill((0, 99, 0))
            pg.display.flip()
            pg.display.update()

