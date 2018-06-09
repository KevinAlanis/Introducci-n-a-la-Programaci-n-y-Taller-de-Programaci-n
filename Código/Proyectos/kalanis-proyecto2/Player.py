import pygame, math, random


pygame.init()

#Controla la rotacion de la imagen del carro---------------------------------------------------------------------------------------------------------------------------
def rot_center(image,rect,angle):
    rot_image=pygame.transform.rotate(image, angle)
    rot_rect=rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect

#Se definen las funciones y propiedades que controlan a los vehiculos de los jugadores---------------------------------------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, image, posX, posY):
#Aqui se definen varias propiedades de los jugadores: imagen, velocidad, aceleracion, direccion, la posX y la posY, velocidad maxima/minima velocidad de giro----------
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.image_orig=self.image
        self.speed=0
        self.acceleration=0.1
        self.deacceleration=2
        self.direction=0
        self.max_speed=5
        self.min_speed=-2
        self.posX=posX
        self.posY=posY
        self.steering=10
        self.softening=0.5

#Función de detención suave del vehículo cuando se deja de precionar la tecla de avanzar-------------------------------------------------------------------------------
    def soften(self):
        if self.speed>0:
            self.speed-=self.softening
        if self.speed<0:
            self.speed+=self.softening

#Funcion de la aceleracion del vehículo--------------------------------------------------------------------------------------------------------------------------------
    def accelerate(self):
        if self.speed<self.max_speed:
            self.speed=self.speed+self.acceleration
#Funcion de la desaceleracion del vehículo--------------------------------------------------------------------------------------------------------------------------------
    def deaccelerate(self):
        if self.speed>self.min_speed:
            self.speed=self.speed-self.deacceleration
#Funciones giro a la izquiera y giro a la derecha----------------------------------------------------------------------------------------------------------------------
    def steerleft(self):
        self.direction=self.direction+self.steering
        if self.direction>360:
            self.direction=0
        self.image, self.rect=rot_center(self.image_orig,self.rect,self.direction)
        
    def steerright(self):
        self.direction=self.direction-self.steering
        if self.direction<0:
            self.direction=360
        self.image, self.rect=rot_center(self.image_orig,self.rect,self.direction)

#Modifica las coordenadas del jugador, para controlar la magnitud y direccion del movimiento--------------------------------------------------------------------------- 
    def update(self, last_x,last_y):
        self.posX=self.posX+self.speed*math.cos(math.radians(270-self.direction))
        self.posY=self.posY+self.speed*math.sin(math.radians(270-self.direction))
