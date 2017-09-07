# -*- coding: utf-8 -*-
import numpy as np

def dist(p1,p2):
    return np.sqrt((float(p1[0])-float(p2[0]))**2+(float(p1[1])-float(p2[1]))**2)

nA=int(raw_input("Cuantos conductores hay en la linea A?"))
nB=int(raw_input("Cuantos conductores hay en la linea B?"))
rgA=float(raw_input("Cual es el radio geometrico de los conductores de A?"))
rgB=float(raw_input("Cual es el radio geometrico de los conductores de B?"))

def DMGAB(p1,p2,conductor):
    if conductor==True:
        n,rg,con,con2=nA,rgA,"a","b"
    else:
        n,rg,con,con2=nB,rgB,"b","a"
    p=1
    for i in range(nA):
        for j in range(nB):
            print "Distancia entre el "+con+str(i+1)+" y "+con2+str(j+1)+"="+str(dist(p1[i],p2[j]))
            p*=dist(p1[i],p2[j])
    return p**(1/float(nA*nB))

def RMG(p1,conductor):
    if conductor==True:
        n,rg,con=nA,rgA,"a"
    else:
        n,rg,con=nB,rgB,"b"
        print n,rg,rg**n
    p=1
    for i in range(n):
        for j in range(n):
            if i==j:
                print "NO"
                continue
            print "Distancia entre el "+con+str(i+1)+" y "+con+str(j+1)+"="+str(dist(p1[i],p1[j]))
            p*=dist(p1[i],p1[j])
    return ((rg**n)*p)**(1./float(n**2.))

puntosA=([(raw_input("Dame las coordenadas del punto "+str(i+1)+" de la linea A: ")) for i in range(nA)])
puntosB=([(raw_input("Dame las coordenadas del punto "+str(i+1)+" de la linea B: ")) for i in range(nB)])

puntosA=tuple(i.split(",") for i in puntosA)
puntosB=tuple(i.split(",") for i in puntosB)

DMG=DMGAB(puntosA,puntosB,True)
RMGA=RMG(puntosA,True)
RMGB=RMG(puntosB,False)

print "La distancia media geométrica es de: "+str(DMG)
print "El radio medio geométrico de la línea A es de: "+str(RMGA)
print "El radio medio geométrico de la línea B es de: "+str(RMGB)

print "La inductancia de la línea A es de: "+str(2.*10**(-7.)*np.log(DMG/RMGA))
print "La inductancia de la línea B es de: "+str(2.*10**(-7.)*np.log(DMG/RMGB))