import numpy as np
import matplotlib.pyplot as plt
kb=0.330   # celui pour laquelle la  condition vaut un en l'infini

def Blasius(k,h=0.01,etalim=10):
    F=[0] # f
    G=[0] # derivee première
    H=[k] # derivee seconde
    N=[0] # n=heta
    while N[-1]<etalim:
        N+=[N[-1]+h]
        f=F[-1]
        F+=[f+h*G[-1]]
        G+=[G[-1]+h*H[-1]]
        H+=[H[-1]-0.5*h*f*H[-1]]
    return N,F,G,H
    
def profilux(k,h=0.01):  # graphique question 5 
    N,F,G,H=Blasius(k,h)
    plt.plot(N,G,'b')
    plt.show()
    return G[-1]-1
         
def dichotomie(E,f,a=0.25,b=0.5): # pour determiner kb
    while((b-a)>E):
        m=(a+b)/2
        if f(a)*f(m)>0:
            a=m
        elif f(m)==0:
            return m
        else:
            b=m
    return a,b,f(m)

def ux(eta):
    N,F,G,H=Blasius(kb,0.01,eta)
    return G[-1]
    

    

