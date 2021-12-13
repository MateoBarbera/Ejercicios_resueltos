from tda_lista import Lista
from random import randint
lista1 = Lista()
lista2 = Lista()
lista_concatenada = Lista()

for i in range(5):
    lista1.insertar(i) 
    lista2.insertar(randint(1,10))

print('lista 1:')
lista1.barrido()
print()

print('lista 2:')
lista2.barrido()
print()

cont_repetidos = 0

#A
for i in range(lista1.tamanio()): 
    numero = (lista2.obtener_elemento(i)) 
    lista1.insertar(numero)


print('listas concatenadas una atras de la ota :')
lista1.barrido()
print()

#B
for i in range(lista1.tamanio()):
    numero = (lista1.obtener_elemento(i)) 
    lista_concatenada.insertar(numero)
lista1.tamanio()
print ('las dos listas concatenada en una sola lista:')
if lista1.obtener_elemento(i) == lista2.obtener_elemento(i):
    cont_repetidos += 1
    lista_concatenada.eliminar(i)
    print()

for i in range(lista2.tamanio()): 
    num = lista2.obtener_elemento(i)
    if(lista2.busqueda(num) == -1):
        lista2.insertar(num)
        cont_repetidos = cont_repetidos +1 #C


                
for i in range(lista1.tamanio()):
	num=lista1.obtener_elemento(i)
	pos = lista1.busqueda(num)
	if (pos != -1):
		cont_repetidos = cont_repetidos + 1

print('la cantidad de elementos repetidos son: ', cont_repetidos)
#D
while(lista1.tamanio()>0):
    numero = (lista1.obtener_elemento(0)) 
    print('numero eliminado: ',numero)
    aux=lista1.eliminar(numero)
    

   

 
