import os

import pygame as pg

from . import ALTO, ANCHO, COLOR_FONDO, COLOR_MENSAJE, FPS, VIDAS
from quest.objetos import ContadorVidas, Marcador, Nave

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
       
        font_file = os.path.join(
            "resources", "fonts", "QUARANTINE REGULATIONS.otf")
        font_file1 = os.path.join(
            "resources", "fonts", "space age.ttf")

        self.tipografia = pg.font.Font(font_file, 77)
        self.t_instrucciones = pg.font.Font(font_file1, 22)


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
        self.fondo = pg.image.load(os.path.join(
            "resources", "images", "espacio.jpg")).convert()    
        self.pantalla.blit(self.fondo,(0, 0)) 

    def pintar_cabecera(self):
        mensaje = "THE QUEST"
        texto = self.tipografia.render(mensaje, True, COLOR_MENSAJE)
        ancho_texto = texto.get_width()
        pos_x = (ANCHO - ancho_texto) / 2
        pos_y = ALTO / 5
        self.pantalla.blit(texto, (pos_x, pos_y) )

    def pintar_texto(self):
        mensaje = "Pulse tecla 'ESPACIO' para continuar"
        texto = self.t_instrucciones.render(mensaje, True, COLOR_MENSAJE)
        ancho_texto = texto.get_width()
        pos_x = (ANCHO - ancho_texto)/2
        pos_y = ALTO - 75
        self.pantalla.blit(texto, (pos_x, pos_y))
    


class PantallaInstrucciones(Escena):
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)

        font_file1 = os.path.join("resources", "fonts", "space age.ttf")
        font_file2 = os.path.join("resources", "fonts", "space age.ttf")

        self.t_instrucciones = pg.font.Font(font_file1, 22)        
        self.t_instrucciones1 = pg.font.Font(font_file2, 15 )

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
                self.pintar_instrucciones()
                self.pintar_texto()

                pg.display.flip()

    def pintar_fondo(self):
        self.fondo = pg.image.load(os.path.join(
            "resources", "images", "espacio.jpg")).convert()    
        self.pantalla.blit(self.fondo,(0, 0)) 
    
    def pintar_texto(self):
        mensaje = "Pulse tecla 'ESPACIO' para empezar"
        texto = self.t_instrucciones.render(mensaje, True, COLOR_MENSAJE)
        ancho_texto = texto.get_width()
        pos_x = (ANCHO - ancho_texto)/2
        pos_y = ALTO - 75
        self.pantalla.blit(texto, (pos_x, pos_y))
    
    def pintar_instrucciones(self):

        posicion_mensaje = [150, 200, 250, 300, 350]
        
        mensaje = ["INSTRUCCIONES:", "Las teclas '</>' mueven la nave, 'X' dispara", 
        "Las colisiones restan vidas", "Esquivar obstaculos suma puntos",
        "Llega a un nuevo planeta para ganar la partida"]

        
        pos_x = ANCHO / 25
        contador_posiciones = 0

        for mensaje in mensaje:
            texto = self.t_instrucciones1.render(
                mensaje, True, COLOR_MENSAJE)
            
            self.pantalla.blit(
                texto, (pos_x, posicion_mensaje[contador_posiciones]))
            contador_posiciones += 1

class Partida(Escena):
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)

        self.jugador = Nave()
        self.contador_vidas = ContadorVidas(VIDAS)
        self.marcador = Marcador()
        

    def bucle_principal(self):
        salir = False
        while not salir:
            self.reloj.tick(FPS)
            self.jugador.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True
                if event.type == pg.QUIT:
                    pg.quit()
            self.pantalla.fill((COLOR_FONDO))
            self.jugador.update()
            self.pintar_fondo()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)
            #pintar asteroides

            self.marcador.pintar_marcador(self.pantalla)
            self.contador_vidas.pintar_contador(self.pantalla)
            pg.display.flip()

    def pintar_fondo(self):
        self.fondo = pg.image.load(os.path.join(
            "resources", "images", "espacio.jpg")).convert()    
        self.pantalla.blit(self.fondo,(0, 0))     

    #def pintar_asteroides(self):
        #self.asteroides = []

        #for i in range()
        #pass

class HallOfFame(Escena):

    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            self.pantalla.fill((COLOR_FONDO))
            pg.display.flip()

