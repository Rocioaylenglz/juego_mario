import pygame as py
from pygame.locals import *
from Configuracion import *
from os import system
system("cls")
from Class_Personaje import *
from Class_enemigo import *
from MODO import *

def crear_plataforma(visible, tamaño,  x,  y, path=""):
    plataforma = {}
    if visible:
        plataforma["superficie"] = py.image.load(path)
        plataforma["superficie"] = py.transform.scale(plataforma["superficie"], tamaño)
    else:
        plataforma["superficie"] = py.Surface(tamaño)

    plataforma["rectangulo"] = plataforma["superficie"].get_rect()
    plataforma["rectangulo"].x = x
    plataforma["rectangulo"].y = y
    
    return plataforma

#ANCHO W - ALTO H
W,H = 1200, 680
FPS = 18 #Para desacelerar la pantalla

py.init()
RELOJ = py.time.Clock()
PANTALLA = py.display.set_mode((W,H)) # En pixeles
py.display.set_caption("Juego Mario")

#FONDO
fondo = py.image.load(r"Corre/fondo.jpg").convert()
fondo = py.transform.scale(fondo, (W,H))

contador_pasos = 0

diccionario = {}
diccionario["Quieto"] = personaje_quieto
diccionario["Derecha"] = personaje_camina_derecha
diccionario["Izquierda"] = personaje_camina_izquierda
diccionario["Salta"] = personaje_salta

mario = Personaje(diccionario,(70,60),200,550,10)
reescalar_imagenes(diccionario, 80,70)

#PSIO
#piso = py.Rect(0,620,W,20)
piso = crear_plataforma(False, (W,20), 0, 663)
plataforma_caño = crear_plataforma(True, (100,100), 1200, 663, "Corre\Caño(2).png")

plataforma_invisible = crear_plataforma(False, (240, 150), 960, 480, "")


plataformas = [piso, plataforma_caño, plataforma_invisible]

diccionario_animaciones = {"izquierda": enemigo_camina, "aplasta": enemigo_aplasta}
un_enemigo = Enemigo(diccionario_animaciones)

lista_enemigos = [un_enemigo]


#Personaje
x_inicial = W//2 - 400
y_inicial = 560
rectangulo_personaje = personaje_quieto[0].get_rect()
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial

que_hace = "Quieto"

flag = True
while flag:
    RELOJ.tick(FPS)
    for event in py.event.get():
        if event.type == QUIT:
            flag = False
        elif event.type == MOUSEBUTTONDOWN: ### SACAR COORDENADAS PARA PLATAFORMAS INVSIBLES
            print(event.pos)

        elif event.type == KEYDOWN:
            if event.key == K_TAB:
                cambiar_modo()

    teclas = py.key.get_pressed()

    if teclas[py.K_RIGHT]:
        mario.que_hace = "Derecha"
    elif teclas[py.K_LEFT]:
        mario.que_hace = "Izquierda"
    elif(teclas[py.K_SPACE]):
        mario.que_hace = "Salta"

    else:
        mario.que_hace = "Quieto"

    PANTALLA.blit(fondo,(0,0))
    PANTALLA.blit(plataforma_caño["superficie"], plataforma_caño["rectangulo"])


    mario.actualizar(PANTALLA, piso, plataformas)
    un_enemigo.actualizar(PANTALLA)

    mario.verificar_colision_enemigo(lista_enemigos, PANTALLA)

    
    if obtener_modo():
        
        #py.draw.rect(PANTALLA, "yellow", piso, 3)
        py.draw.rect(PANTALLA, "blue", mario.rectangulo_principal, 3)

        for plataforma in plataformas:
            py.draw.rect(PANTALLA, "red", plataforma["rectangulo"], 3)


    py.display.update()

py.quit()