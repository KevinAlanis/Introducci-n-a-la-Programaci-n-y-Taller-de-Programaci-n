import pygame, sys, time, random, math
from pygame.locals import*
from Player import*


#Definición de algunos colores--------------------------------------------------
Azul=(0,33,255)
#Creación de la clase principal-------------------------------------------------
pygame.init()

def principal1(opcionPista):
#Levantamiento de la ventana de juego-------------------------------------------
    ventana=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Death Race")
    icon=pygame.image.load("Imagenes/log.png")
    pygame.display.set_icon(icon)
    fin=False
    reloj=pygame.time.Clock()
    pista1=pygame.image.load("Imagenes/pista1.png")
    pista2=pygame.image.load("Imagenes/pista2.png")
    pista3=pygame.image.load("Imagenes/pista3.png")
    fondo=pygame.image.load("Imagenes/fondo.png")
#Instancias---------------------------------------------------------------------
    player1=Player("Imagenes/carro1-up.png",25,20)    
#---------------------------------------------------------------------------------    
    salir = False  
    ventana.blit(fondo,(0,0))
    
    if opcionPista=='1':
        ventana.blit(pista1,(25,20))
    elif opcionPista=='2':
        ventana.blit(pista2,(25,20))
    else:
        ventana.blit(pista3,(25,20))

    #print(pygame.mouse.get_pos())
    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
                salir = True
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                player1.steerleft()
            if keys[K_RIGHT]:
                player1.steerright()
            if keys[K_UP]:
                player1.accelerate()
            else:
                player1.soften()
            if keys[K_DOWN]:
                player1.deaccelerate()
        player1.update(player1.posX, player1.posY)
        pygame.display.update()
        ventana.blit(player1.image,(player1.posX,player1.posY))
        pygame.display.flip()
            

def principal2(opcionPista):
#Levantamiento de la ventana de juego-------------------------------------------
    ventana=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Death Race")
    icon=pygame.image.load("Imagenes/log.png")
    pygame.display.set_icon(icon)
    fin=False
    reloj=pygame.time.Clock()
    pista1=pygame.image.load("Imagenes/pista1.png")
    pista2=pygame.image.load("Imagenes/pista2.png")
    pista3=pygame.image.load("Imagenes/pista3.png")
    fondo=pygame.image.load("Imagenes/fondo.png")
#Instancias---------------------------------------------------------------------
    player1=Player("Imagenes/carro1-up.png",25,20) 
    player2=Player("Imagenes/carro2-up.png",50,40) 
             
#Pinta en pantalla los objetos--------------------------------------------------    
    salir = False  
    ventana.blit(fondo,(0,0))

    if opcionPista=='1':
        ventana.blit(pista1,(25,20))
    elif opcionPista=='2':
        ventana.blit(pista2,(25,20))
    else:
        ventana.blit(pista3,(25,20))
        
    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
                salir = True
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                player1.steerleft()
            if keys[K_RIGHT]:
                player1.steerright()
            if keys[K_UP]:
                player1.accelerate()
            else:
                player1.soften()
            if keys[K_DOWN]:
                player1.deaccelerate()

            if keys[K_a]:
                player1.steerleft()
            if keys[K_d]:
                player1.steerright()
            if keys[K_w]:
                player1.accelerate()
            else:
                player1.soften()
            if keys[K_s]:
                player1.deaccelerate()
        player1.update(player1.posX, player1.posY)
        player2.update(player2.posX, player2.posY)
        pygame.display.update()
        ventana.blit(player1.image,(player1.posX,player1.posY))
        ventana.blit(player2.image,(player2.posX,player2.posY))
        pygame.display.flip()
