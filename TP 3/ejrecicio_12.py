from tda_cola import Cola
from random import randint
cola1 = Cola()
cola2 = Cola()
cola_final = Cola()

lista1 = [1, 6, 10, 25, 34]
lista2 = [7, 11, 16, 21, 32]

print ('Para cola 1, agregamos: ')
for i in (lista1):
     cola1.arribo(i)
     print (i)


print ()

print ('Para cola 2, agregamos: ')
for i in (lista2):
     cola2.arribo(i)
     print (i)

print()

while (not cola1.cola_vacia() and not cola2.cola_vacia()):
 ### comparamos elemento a elemento desde el frente de cada cola con la otra
     if (cola1.en_frente() < cola2.en_frente()):
         cola_final.arribo(cola1.atencion())
     else:
         cola_final.arribo(cola2.atencion())
 ####si una de las dos colas esta vacia, cargaremos el elemento restante de la otra cola ,a la cola final
     if (cola1.cola_vacia()):
         cola_final.arribo(cola2.atencion())
     if (cola2.cola_vacia()):
         cola_final.arribo(cola1.atencion())
        
print ('Cola final')
cantidad_elemento = 0
while (cantidad_elemento < cola_final.tamanio()):
     dato = cola_final.mover_final ()
     print (dato)
     cantidad_elemento += 1
