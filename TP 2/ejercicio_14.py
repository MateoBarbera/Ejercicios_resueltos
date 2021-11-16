from pila import Pila, apilar,mostrar_elementos, cima, pila_vacia

'''14. Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden orde-
nados de forma creciente. Solo puede utilizar una pila auxiliar como estructura extra –no se
pueden utilizar métodos de ordenamiento–.'''

pila1=Pila()
pila2=Pila()

def main():
    print("1 Aplilar elemento :")
    
main()    
option=input("Elija una opcion: ")

if str(option)=="1":  

    elemento = input(" Introduzca el numero a apilar: ")
    while (not pila_vacia(pila1)):
        if elemento != '':
            print(" Elemento apilado ")
            apilar(pila1 ,elemento)
            mostrar_elementos(pila1)
            main()
        else:
            mostrar_elementos(pila1)    