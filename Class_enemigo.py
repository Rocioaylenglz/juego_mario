from Configuracion import *
from Class_Personaje import *


class Enemigo:
    def __init__(self, animaciones) -> None:
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, 50, 50)
        self.rectangulo_principal = self.animaciones["izquierda"][0].get_rect()
        self.rectangulo_principal.x = 1200
        self.rectangulo_principal.y = 610

        self.esta_muerto = False
        self.pasos = 0
        self.animacion_actual = self.animaciones["izquierda"]
        self.muriendo = False


    def avanzar(self):
        self.rectangulo_principal.x -= 5

    def animar (self, pantalla):
        largo = len(self.animacion_actual)
        if self.pasos >=  largo:
            self.pasos = 0
        
        pantalla.blit(self.animacion_actual[self.pasos], self.rectangulo_principal)
        self.pasos += 1

    def actualizar(self, pantalla):
        if self.esta_muerto == False:
            self.animar(pantalla)
            self.avanzar()