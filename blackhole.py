#run online with https://create.withcode.uk/
#or use https://repl.it/languages/tkinter
# this program makes a blackhole simulation

from visual import*
from math import*
scene.background=vector(0,0,.1)
us=vector(0,0,0)
r=250   #distancia al planeta
rest=100 #radio de la estrella
re=20 #radio de enana blanca
ran=15  #radio del agujero negro
np=20 #numero de particulas del disco de acrecion
np2=6 # 
d=-(ran-15) #radio del circulo mayor de las partículas
dj=.001 #distancia inicial del jet con respecto al centro
vy=2 #velocidad de las particulas del jet
ñ=15   #parametro del disco de acreción, si ñ=15, solo 2 part


agujero=sphere(pos=vector(0,0,0),radius=ran,color=vector(.01,0,.1))
planeta=sphere(pos=vector(r,0,0),radius=5,color=vector(0,.1,.8)) #planeta
estrella=sphere(pos=vector(0,0,0),radius=rest,color=vector(1,1,1))  #estrella
           
def A(t):
	return estrella.rotate(angle=pi/2,origin=us)
def A2(t):
	return estrella

def C(t):
        return agujero.rotate(angle=pi/2,origin=us)
def C2(t):
        return agujero

                
 #   plano espacio temporal
#for i in range(r+50):
#    curve(pos=vector[(2*(i)-(r+50),0,-(r+50)),(2*(i)-(r+50),0,(r+50))], color=color.cyan)       
#    curve(pos=vector[(-(r+50),0,2*(i)-(r+50)),((r+50),0,2*(i)-(r+50))], color=color.cyan)
##
##
###FUNCION COLAPSO Y CAMBIO DE GIGANTE ROJA A ENANA BLANCA y traslacion
j=1
m=1
t=1
n=1
w=1
y=1
T=0
while 2:   
    rate(50)
    m=m+15
    j=j+.001# j solo afecta  el color del planeta
    y=j-1  # color de las partículas
    #T=T+.1  #tiempo para el jet  
    dj=dj+.01 # la constante mide el ángulo del jet
    A2(t)          #rotacion de la esfera
    A(t)
    C2(t)           #rotación del planeta 
    estrella.radius = estrella.radius-.1         #colapso
    estrella.color=vector(1,2/(j**4),0)        #     (1,20-(j),4-(j**2))sino funciona elant estesi
    planeta.pos.x=r*cos(m*pi/180)        #rotacion
    planeta.pos.z=r*sin(m*pi/180)
        
    if estrella.radius <=re:            #enana blanca   
        estrella.color=vector(10,10,10) #la estrella se vuelve enana blanca
    if estrella.radius<=ran:
        d=d-.4 
        w=w+7
        T=T+.5
        for i in range (np):
                part=sphere(pos=vector(d*cos(i*2*pi/np),0,d*sin(i*2*pi/np)),radius=.9-t/10,color=vector(1,1,1))
                part.pos=vector(d*cos(ñ*((w*180/pi)+(i*2*pi/np))),0,d*sin(ñ*((w*180/pi)+(i*2*pi/np))))
                part.color=vector(1,2/(2*y),2/((y))**10)
                jet1=sphere(pos=vector(dj*cos(i*2*pi/np),0,dj*sin(i*2*pi/np)),radius=.4,color=vector(0,.7,1))
                jet1.pos=vector(dj*cos((T*180/pi)+(i*2*pi/np)),0,dj*sin((T*180/pi)+(i*2*pi/np)))
                jet1.pos.y=vy*T
                jet2=sphere(pos=vector(dj*cos(i*2*pi/np),0,dj*sin(i*2*pi/np)),radius=.4,color=vector(0,.7,1))
                jet2.pos=vector(dj*cos((T*180/pi)+(i*2*pi/np)),0,dj*sin((T*180/pi)+(i*2*pi/np)))
                jet2.pos.y=-vy*T
                
    if estrella.radius <=0:
        estrella.color=vector(0,0,0)
        r=r-5
        #estrella.radius=0
        if r<=0:
                r=0