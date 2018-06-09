
import sys
import random
import pygame
from pygame.locals import *
from Death_Race import *

#Se crea la clase opcion que inicializa algunas variables y crea algunas funciones-------------------------------------------------------------------------------------
class Opcion:

    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (255, 255, 255))
        self.imagen_destacada = fuente.render(titulo, 1, (200, 0, 0))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)
        pygame.mixer.music.load("sonidos/intro.mp3")
        pygame.mixer.music.play()

    def actualizar(self):
        destino_x = 105
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, ventana):
        ventana.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()

#Se crea la clase cursor que inicializa algunas variables y crea algunas funciones-------------------------------------------------------------------------------------
class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load('menu/cursor.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, ventana):
        ventana.blit(self.image, self.rect)

#Representa un menú con opciones para el juego-------------------------------------------------------------------------------------------------------------------------
class Menu:
    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font('menu/dejavu.ttf', 20)
        x = 105
        y = 105
        paridad = 2

        self.cursor = Cursor(x - 30, y, 30)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

#Altera el valor de self.seleccionado con los direccionales.---------------------------------------------------------------------------------------------------------
    def actualizar(self):
        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
#Invoca a la función asociada a la opción------------------------------------------------------------------------------------------------------------------------------
                self.opciones[self.seleccionado].activar()
                
#Procura que el cursor esté entre las opciones permitidas--------------------------------------------------------------------------------------------------------------
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

#Indica si el usuario mantiene pulsada alguna tecla--------------------------------------------------------------------------------------------------------------------
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()
     
        for o in self.opciones:
            o.actualizar()
#Imprime sobre ventana el texto de cada opción del menú.--------------------------------------------------------------------------------------------------------------
    def imprimir(self, ventana):
        

        self.cursor.imprimir(ventana)

        for opcion in self.opciones:
            opcion.imprimir(ventana)
#Registro de nombres---------------------------------------------------------------------------------------------------------------------------------------------------
    
def registrarJugador(nombre):
    archivo=open('registroJugadores.json','a')
    archivo.write('Nombre '+nombre+'\n')
    archivo.close()
#Ve el registro de los nombres-----------------------------------------------------------------------------------------------------------------------------------------    
def verDatos():
    archivo=open('registroJugadores.json','r')
    archivos=archivo.read()
    archivo.close()
    return archivos
#Funciones del menú----------------------------------------------------------------------------------------------------------------------------------------------------
def Un_Jugador():
    print (" Partida 1 jugador.")
    elegirPista1()

def Dos_Jugadores():
    print (" Partida 2 jugadores.")
    elegirPista2()
    
def Registrar_Nombre_de_Usuario():
    print (" Registrar nombre de usuario.")
    entradaTexto()
    
def Ver_Puntajes():
    print (" Ver historial de puntajes.")
    print(verDatos())
    
def Salir_del_Programa():
    print (" Gracias por utilizar este programa.")
    pygame.quit()
    sys.exit()
    salir=True
    return salir

#Función que crea el ingreso de texto en ventana-----------------------------------------------------------------------------------------------------------------------
def entradaTexto():
    font = pygame.font.Font('menu/dejavu.ttf', 25)
    font1=pygame.font.Font('menu/dejavu.ttf',20)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(250, 80, 140, 32)
    color_inactive = pygame.Color('red')
    color_active = pygame.Color('green')
    color = color_inactive
    active = False
    text = ''
    text1=font1.render("Ingrese su nombre: ",0 , (255,255,255))
    done = False
    fondo2=pygame.image.load("menu/fondo2.png")

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si el usuario clickea en la caja de texto.-----------------------------------------------------------------------------------------------------------
                if input_box.collidepoint(event.pos):
                    # Cambiando la variable activa.--------------------------------------------------------------------------------------------------------------------
                    active = not active
                else:
                    active = False
                # Cambia el color de la caja. Indica si se puede escribir.---------------------------------------------------------------------------------------------
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        registrarJugador(text)
                        text = ''
                        done=True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        ventana.fill((30, 30, 30))
        ventana.blit(fondo2,(0,0))
        ventana.blit(text1,(20, 80))
        # Renderiza el texto.------------------------------------------------------------------------------------------------------------------------------------------
        txt_surface = font.render(text, True, color)
        # Reajusta la caja si el texto es muy largo.-------------------------------------------------------------------------------------------------------------------
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Lo muestra en ventana.---------------------------------------------------------------------------------------------------------------------------------------
        ventana.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Muestra en ventana la caja de texto.-------------------------------------------------------------------------------------------------------------------------
        pygame.draw.rect(ventana, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)
#Funcion para elegir la pista del jugador 1----------------------------------------------------------------------------------------------------------------------------
def elegirPista1():
    font = pygame.font.Font('menu/dejavu.ttf', 15)
    font1=pygame.font.Font('menu/dejavu.ttf',20)
    font2=pygame.font.Font('menu/dejavu.ttf',15)
    font3=pygame.font.Font('menu/dejavu.ttf',15)
    font4=pygame.font.Font('menu/dejavu.ttf',15)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(365, 80, 100, 30)
    color_inactive = pygame.Color('red')
    color_active = pygame.Color('green')
    color = color_inactive
    active = False
    text = ''
    text1=font1.render("Escoja una dificultad de pista: ",0 , (255,105,0))
    text2=font2.render("1. Pista chofer principiante: ",0 , (255,105,0))
    text3=font3.render("2. Pista chofer intermedio: ",0 , (255,105,0))
    text4=font4.render("3. Pista chofer profesional: ",0 , (255,105,0))
    done = False
    fondo3=pygame.image.load("menu/fondo3.png")

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si el usuario clickea en la caja de texto.-----------------------------------------------------------------------------------------------------------
                if input_box.collidepoint(event.pos):
                    # Cambiando la variable activa.--------------------------------------------------------------------------------------------------------------------
                    active = not active
                else:
                    active = False
                # Cambia el color de la caja. Indica si se puede escribir.---------------------------------------------------------------------------------------------
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        opcion=text
                        principal1(opcion)
                        text = ''
                        done=True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        ventana.fill((255, 255, 255))
        ventana.blit(fondo3,(0,0))
        ventana.blit(text1,(20, 80))
        ventana.blit(text2,(20, 100))
        ventana.blit(text3,(20, 120))
        ventana.blit(text4,(20, 140))
        # Renderiza el texto.------------------------------------------------------------------------------------------------------------------------------------------
        txt_surface = font.render(text, True, color)
        # Reajusta la caja si el texto es muy largo.-------------------------------------------------------------------------------------------------------------------
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Lo muestra en ventana.---------------------------------------------------------------------------------------------------------------------------------------
        ventana.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Muestra en ventana la caja de texto.-------------------------------------------------------------------------------------------------------------------------
        pygame.draw.rect(ventana, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)
#Funcion para elegir la pista del jugador 2----------------------------------------------------------------------------------------------------------------------------
def elegirPista2():
    font = pygame.font.Font('menu/dejavu.ttf', 15)
    font1=pygame.font.Font('menu/dejavu.ttf',20)
    font2=pygame.font.Font('menu/dejavu.ttf',15)
    font3=pygame.font.Font('menu/dejavu.ttf',15)
    font4=pygame.font.Font('menu/dejavu.ttf',15)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(365, 80, 100, 30)
    color_inactive = pygame.Color('red')
    color_active = pygame.Color('green')
    color = color_inactive
    active = False
    text = ''
    text1=font1.render("Escoja una dificultad de pista: ",0 , (255,105,0))
    text2=font2.render("1. Pista chofer principiante: ",0 , (255,105,0))
    text3=font3.render("2. Pista chofer intermedio: ",0 , (255,105,0))
    text4=font4.render("3. Pista chofer profesional: ",0 , (255,105,0))
    done = False
    fondo3=pygame.image.load("menu/fondo3.png")

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si el usuario clickea en la caja de texto.-----------------------------------------------------------------------------------------------------------
                if input_box.collidepoint(event.pos):
                    # Cambiando la variable activa.--------------------------------------------------------------------------------------------------------------------
                    active = not active
                else:
                    active = False
                # Cambia el color de la caja. Indica si se puede escribir.---------------------------------------------------------------------------------------------
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        opcion=text
                        principal2(opcion)
                        text = ''
                        done=True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        ventana.fill((255, 255, 255))
        ventana.blit(fondo3,(0,0))
        ventana.blit(text1,(20, 80))
        ventana.blit(text2,(20, 100))
        ventana.blit(text3,(20, 120))
        ventana.blit(text4,(20, 140))
        # Renderiza el texto.------------------------------------------------------------------------------------------------------------------------------------------
        txt_surface = font.render(text, True, color)
        # Reajusta la caja si el texto es muy largo.-------------------------------------------------------------------------------------------------------------------
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Lo muestra en ventana.---------------------------------------------------------------------------------------------------------------------------------------
        ventana.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Muestra en ventana la caja de texto.-------------------------------------------------------------------------------------------------------------------------
        pygame.draw.rect(ventana, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)
        
#loop principal--------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    
    salir = False
    opciones = [("1 Jugador", Un_Jugador), ("2 Jugadores", Dos_Jugadores),("Registrar Nombre de Usuario",Registrar_Nombre_de_Usuario), ("Ver Puntajes",Ver_Puntajes),
        ("Salir", Salir_del_Programa)]

    pygame.font.init()
    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Menú Death Race")
    icon=pygame.image.load("Imagenes/log.png")
    pygame.display.set_icon(icon)
    fondo = pygame.image.load("menu/fondo.png").convert()
    menu = Menu(opciones)


    pygame.mixer.music.play(4)
#loop secundario------------------------------------------------------------------------------------------------------------------------------------------------------   
    while not salir:
        #print(pygame.mouse.get_pos())
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
                salir = True

        ventana.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(ventana)

        pygame.display.flip()
        pygame.time.delay(10)

