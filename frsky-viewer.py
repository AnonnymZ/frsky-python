#Author : Elwan Mayencourt
#Version : 1
#Date 07.02.2020


import pygame
import time
import math 



pygame.init()
pygame.display.init()
pygame.joystick.init()
controller = pygame.joystick.Joystick(1) #You may have to change number to find your joystick
controller.init()
name = controller.get_name()

screen = pygame.display.set_mode((800, 800))

#---------------COLOR---------------
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#---------------VAR---------------
x = 0 
y = 1
x1 = 0 
y1 = 0

#---------------FONT---------------
font = pygame.font.Font('freesansbold.ttf', 24) 

def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    screen.fill((255, 255, 255))


    joyLeftX = int(800/3)
    joyRightX = int(800/3*2)
    joyY = 400
    rayon = 100
    sizeJoysite = 10

    pygame.draw.rect(screen, black, (joyLeftX-100,joyY-100,200,200),3)
    pygame.draw.rect(screen, black, (joyRightX-100,joyY-100,200,200),3)
    pygame.draw.circle(screen, black, (joyLeftX, joyY), rayon, 1)
    pygame.draw.circle(screen, black, (joyRightX, joyY),rayon , 1)
    pygame.draw.circle(screen, red, (joyLeftX+int(x1*rayon), joyY-int(y1*rayon)),sizeJoysite , 10)
    pygame.draw.circle(screen, red, (joyRightX+int(x*rayon), joyY-int(y*rayon)),sizeJoysite , 10)

    yaw = font.render("Y:"+str(round(x1,2)), True, black)
    screen.blit(yaw, (joyLeftX, joyY-rayon-40))

    throttle = font.render("T:"+str(round(y1,2)), True, black) 
    screen.blit(throttle, (joyLeftX-rayon-80, joyY))

    roll = font.render("R:"+str(round(x,2)), True, black)
    screen.blit(roll, (joyRightX, joyY-rayon-40))

    pitch = font.render("P:"+str(round(y,2)), True, black) 
    screen.blit(pitch, (joyRightX+rayon+20, joyY))

    nameText = font.render("Controller name : "+name, True, black) 
    screen.blit(nameText, (0, 0))


    pygame.display.flip()	#REFRESH
	


    #0 : Roll
    #1 : Pitch
    #2 : Throttle
    #3 : Button left
    #4 : Button right
    #5 : Yaw


    for k in range(controller.get_numaxes()):

        value = controller.get_axis(k)
        value = str(value)

        #---------------ROLL---------------
        if k == 0:  
        	x = float(value)

        #---------------PITCH---------------
        if k == 1:
            y = float(value)

        #---------------Throttle---------------
        if k == 2:
         	y1 = float(value)

        #---------------Yaw---------------
        if k == 5:
            x1 = float(value)


        # if k == 3:
        # 	print("ButtonLeft("+value+")  ", end = '')
        # if k == 4:
        # 	print("ButtonRight("+value+")  ", end = '')
