#import complejos
import math
import complejos as comp
import numpy as np
import matplotlib.pyplot as plt

def funcion_f(z,c):
    return comp.suma(comp.potencia(z),c)
def esta_en_mandelbrot(c):
    z = [0,0]
    cont = 0
    for i in range(30):
        z = funcion_f(z,c)
        cont += 1
        #print(z)
        if comp.modulo(z) > 2:
            return False,cont
    return True,0


def main():
    plano = np.zeros((400,700))
    for parte_real in range(700):
        for parte_imaginaria in range(400):
            c = [parte_real/200 - 2.5, parte_imaginaria/200 -1]
            pertenece,color = esta_en_mandelbrot(c)
            if pertenece:
                plano[parte_imaginaria][parte_real] = color
            else:
                plano[parte_imaginaria][parte_real] = color
    #v = np.random.randint(0, 3, size=n)
    colores = ["#00cc44",  # Verde
           "#ff7700",  # Naranja
           "#ff0000"   # Rojo
          ]
    plt.figure(figsize = (10,10))
    plt.imshow(plano,'twilight_shifted')
    plt.show()
#def main():
    #print(esta_en_mandelbrot([0,1]))
    #print(funcion_f([1,1],1))

main()
