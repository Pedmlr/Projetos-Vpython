Web VPython 3.2
from vpython import *

G = 6.67e-11
M = 5.97e24
m = 1000
R = 6.37e6

vini = vector(0,2.0e3,0)

Terra = sphere(pos=vector(0,0,0), radius = R, texture=textures.earth)

Terra.m = M
Terra.v = vector(0,5e3,0)
Terra.p = Terra.m*Terra.v

Satelite = sphere(pos=vector(5*R,0,0), radius =0.2*R, color=color.white, make_trail=True)
Satelite.m = m
Satelite.v = vini
Satelite.p = Satelite.m*Satelite.v

t = 0
dt =0.1
tf = 10000.0
omega = 5.0e-2

while t<tf:
    rate(10000)
    
    rv = Satelite.pos - Terra.pos
    
    F = ((-G*Terra.m*Satelite.m)/(mag(rv)**2))*norm(rv)
    
    
    print(rv)
    
    F = ((-G*Terra.m*Satelite.m)/(mag(rv)**2))*norm(rv)
    Satelite.p = Satelite.p +(F*t)
    Satelite.pos = Satelite.pos +(Satelite.p/Satelite.m)*t
    Terra.pos = Terra.pos +(Terra.p/Terra.m)*t
    Terra.rotate(angle=omega*dt, axis=vector(0,1,1))
    t = t+ dt
