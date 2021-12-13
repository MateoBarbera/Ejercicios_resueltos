from graffo import Grafo 
from tda_cola import Cola

dioses = Grafo(dirigido = False ) #Grafo no dirigido.

dioses.insertar_vertice("Ouranos", data ="") #Escribir descripcion
dioses.insertar_vertice("Gaia", data ="") 
dioses.insertar_vertice("Themis", data ="") 
dioses.insertar_vertice("Minemosyne", data ="")  
dioses.insertar_vertice("Hera", data ="")
dioses.insertar_vertice("Hyperion", data ="") 
dioses.insertar_vertice("Theia", data ="") 
dioses.insertar_vertice("Krios", data ="")
dioses.insertar_vertice("Kronos", data ="")
dioses.insertar_vertice("Rhea", data ="")
dioses.insertar_vertice("Kdios", data ="")
dioses.insertar_vertice("Phoibe", data ="")
dioses.insertar_vertice("Iapetos", data ="")
dioses.insertar_vertice("Okeanos", data ="")
dioses.insertar_vertice("Tethys", data ="")
dioses.insertar_vertice("Helios", data ="")
dioses.insertar_vertice("Eos", data ="")
dioses.insertar_vertice("Selene", data ="")
dioses.insertar_vertice("Prometheus", data ="")
dioses.insertar_vertice("Epimetheus", data ="")
dioses.insertar_vertice("Atlas", data ="")
dioses.insertar_vertice("Plevone", data ="")
dioses.insertar_vertice("Hades", data ="")
dioses.insertar_vertice("Demeter", data ="")
dioses.insertar_vertice("Poseidon", data ="")
dioses.insertar_vertice("Hestia", data ="")
dioses.insertar_vertice("Zeus", data ="")
dioses.insertar_vertice("Leto", data ="")
dioses.insertar_vertice("Semelle", data ="")
dioses.insertar_vertice("Maia", data ="")
dioses.insertar_vertice("Persephone", data ="")
dioses.insertar_vertice("Aphrodite", data ="")
dioses.insertar_vertice("Ares", data ="")
dioses.insertar_vertice("Athena", data ="")
dioses.insertar_vertice("Apollo", data ="")
dioses.insertar_vertice("Artemis", data ="")
dioses.insertar_vertice("Dyonisos", data ="")
dioses.insertar_vertice("Hermes", data ="")
dioses.insertar_vertice("Hephaistos", data ="")
dioses.insertar_vertice("Penelopeia", data ="")
dioses.insertar_vertice("Phobos", data ="")
dioses.insertar_vertice("Deimos", data ="")
dioses.insertar_vertice("Eros", data ="")
dioses.insertar_vertice("Himeros", data ="")
dioses.insertar_vertice("Hermaphrodite", data ="")
dioses.insertar_vertice("Pan", data ="")


#Pareja
dioses.insertar_arista(1,"Ouranos","Gaia", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Ouranos","Themis", data ={'relacion': ['padre', 'hijo']}) #peso, origen, destino
dioses.insertar_arista(1,"Ouranos","Minemosyne", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Hyperion", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Theia", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Krios", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Kronos", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Rhea", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Kdios", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Phoibe", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Iapetos", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Okeanos", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Tethys", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Themis", data ={'relacion': ['padre', 'hijo']}) #peso, origen, destino
#madre/hijo
dioses.insertar_arista(1,"Gaia","Minemosyne", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Hyperion", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Theia", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Krios", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Kronos", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Rhea", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Kdios", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Phoibe", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Iapetos", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Okeanos", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Tethys", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Themis", data ={'relacion': ['madre', 'hijo']}) #peso, origen, destino

#hermanos
dioses.insertar_arista(1,"Themis","Minemosyne", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Hyperion", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Theia", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Krios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Kronos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Rhea", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Kdios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Phoibe", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Hyperion", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Theia", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Krios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Kronos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Rhea", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Kdios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Phoibe", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Theia", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Krios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Kronos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Rhea", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Kdios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Phoibe", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Theia","Krios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Theia","Kronos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Theia","Rhea", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Theia","Kdios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Theia","Phoibe", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Theia","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Theia","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Theia","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Krios","Kronos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Krios","Rhea", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Krios","Kdios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Krios","Phoibe", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Krios","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Krios","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Krios","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Krios","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kronos","Rhea", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kronos","Kdios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kronos","Phoibe", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kronos","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kronos","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kronos","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Rhea","Kdios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Rhea","Phoibe", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Rhea","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Rhea","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Rhea","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kdios","Phoibe", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kdios","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kdios","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kdios","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Phoibe","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Phoibe","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Phoibe","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Iapetos","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Iapetos","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Okeanos","Tethys", data ={'relacion': ['hermanos']})


#Pareja
dioses.insertar_arista(1,"Hyperion","Theia", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Hyperion","Helios", data ={'relacion': ['padre', 'hijo']}) #peso, origen, destino
dioses.insertar_arista(1,"Hyperion","Eos", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Hyperion","Selene", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Theia","Helios", data ={'relacion': ['madre', 'hijo']}) #peso, origen, destino
dioses.insertar_arista(1,"Theia","Eos", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Theia","Selene", data ={'relacion': ['madre', 'hijo']})
#hermanos
dioses.insertar_arista(1,"Helios","Eos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Helios","Selene", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Eos","Selene", data ={'relacion': ['hermanos']})

#pareja
dioses.insertar_arista(1,"Kronos","Rhea", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Kronos","Hades", data ={'relacion': ['padre', 'hijo']}) 
dioses.insertar_arista(1,"Kronos","Demeter", data ={'relacion': ['padre', 'hijo']}) 
dioses.insertar_arista(1,"Kronos","Poseidon", data ={'relacion': ['padre', 'hijo']}) 
dioses.insertar_arista(1,"Kronos","Hestia", data ={'relacion': ['padre', 'hijo']}) 
dioses.insertar_arista(1,"Kronos","Hera", data ={'relacion': ['padre', 'hijo']}) 
dioses.insertar_arista(1,"Kronos","Zeus", data ={'relacion': ['padre', 'hijo']}) 
#madre/hijo
dioses.insertar_arista(1,"Rhea","Hades", data ={'relacion': ['madre', 'hijo']}) 
dioses.insertar_arista(1,"Rhea","Demeter", data ={'relacion': ['madre', 'hijo']}) 
dioses.insertar_arista(1,"Rhea","Poseidon", data ={'relacion': ['madre', 'hijo']}) 
dioses.insertar_arista(1,"Rhea","Hestia", data ={'relacion': ['madre', 'hijo']}) 
dioses.insertar_arista(1,"Rhea","Hera", data ={'relacion': ['madre', 'hijo']}) 
dioses.insertar_arista(1,"Rhea","Zeus", data ={'relacion': ['madre', 'hijo']}) 
#hermanos
dioses.insertar_arista(1,"Hades","Demeter", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hades","Poseidon", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hades","Hestia", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hades","Hera", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hades","Zeus", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Demeter","Poseidon", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Demeter","Hestia", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Demeter","Hera", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Demeter","Zeus", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Poseidon","Hestia", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Poseidon","Hera", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Poseidon","Zeus", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hestia","Hera", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hestia","Zeus", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hera","Zeus", data ={'relacion': ['hermanos']})


#pareja
dioses.insertar_arista(1,"Kdios","Phoibe", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Kdios","Leto", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Phoibe","Leto", data ={'relacion': ['madre', 'hijo']}) 

#padre/hijo
dioses.insertar_arista(1,"Iapetos","Prometheus", data ={'relacion': ['padre', 'hijo']}) 
dioses.insertar_arista(1,"Iapetos","Epimetheus", data ={'relacion': ['padre', 'hijo']}) 
dioses.insertar_arista(1,"Iapetos","Atlas", data ={'relacion': ['padre', 'hijo']}) 
#hermanos
dioses.insertar_arista(1,"Prometheus","Epimetheus", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Prometheus","Atlas", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Epimetheus","Atlas", data ={'relacion': ['hermanos']})

#Pareja
dioses.insertar_arista(1,"Okeanos","Tethys", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Okeanos","Plevone", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Tethys","Plevone", data ={'relacion': ['madre', 'hijo']}) 

#Pareja
dioses.insertar_arista(1,"Atlas","Plevone", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Atlas","Maia", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Plevone","Maia", data ={'relacion': ['madre', 'hijo']}) 

#Pareja
dioses.insertar_arista(1,"Zeus","Hera", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Zeus","Ares", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Zeus","Hephaistos", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Hera","Ares", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Hera","Hephaistos", data ={'relacion': ['madre', 'hijo']})
#hermanos
dioses.insertar_arista(1,"Ares","Hephaistos", data ={'relacion': ['hermanos']})

#Pareja
dioses.insertar_arista(1,"Zeus","Demeter", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Zeus","Persephone", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Demeter","Persephone", data ={'relacion': ['madre', 'hijo']})

#madre/hijo
dioses.insertar_arista(1,"Leto","Apollo", data ={'relacion': ['madre', 'hijo']})#madre/hijo
dioses.insertar_arista(1,"Leto","Artemis", data ={'relacion': ['madre', 'hijo']})
#hermanos
dioses.insertar_arista(1,"Apollo","Artemis", data ={'relacion': ['hermanos']})


#Pareja
dioses.insertar_arista(1,"Zeus","Maia", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Zeus","Hermes", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Maia","Hermes", data ={'relacion': ['madre', 'hijo']})

#madre/hijo
dioses.insertar_arista(1,"Semelle","Dyonisos", data ={'relacion': ['madre', 'hijo']})

#Pareja
dioses.insertar_arista(1,"Ares","Aphrodite", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Ares","Phobos", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ares","Deimos", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ares","Eros", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ares","Himeros", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Aphrodite","Phobos", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Aphrodite","Deimos", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Aphrodite","Eros", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Aphrodite","Himeros", data ={'relacion': ['madre', 'hijo']})
#hermanos
dioses.insertar_arista(1,"Phobos","Deimos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Phobos","Eros", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Phobos","Himeros", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Deimos","Eros", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Deimos","Himeros", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Eros","Himeros", data ={'relacion': ['hermanos']})

#Pareja
dioses.insertar_arista(1,"Hermes","Penelopeia", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Hermes","Pan", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Penelopeia","Pan", data ={'relacion': ['madre', 'hijo']})

#Pareja
dioses.insertar_arista(1,"Hermes","Aphrodite", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Hermes","Hermaphrodite", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Aphrodite","Hermaphrodite", data ={'relacion': ['madre', 'hijo']})


#c. Mostrar los hijos de un dios
buscado = (input("Ingrese el nombre del dios del cual desea saber sus hijos: "))
origen = dioses.buscar_vertice(buscado)
dios = dioses.inicio.obtener_elemento(origen)  ##Inicio es para acceder a las aristas del vertice (aristas = lista)
print('Hijos de ', dios['info'])
dioses.relaciones(buscado,"hijo")


#d. mostrar nombre, padre, madre, hermanos e hijos de un dios
buscado = (input("Ingrese el nombre del dios que desea saber su info: "))
print("El dios es: ",buscado)
print()
print("Su madre es: ")
dioses.relaciones(buscado,"madre")
print()
print("Su padre es: ")
dioses.relaciones(buscado,"padre")
print()
print("Sus hermanos son: ")
dioses.relaciones(buscado,"hermanos")
print()
print("Sus hijos son : ")
dioses.relaciones(buscado,"hijo")
print()


#e. determinar si existe y cual seria la relacion entre dos vertices
buscado1 = (input("Ingrese un vertice para saber si tiene relacion directa con el segundo: "))
origen = dioses.buscar_vertice(buscado1)
buscado2 = (input("Ingrese el segundo nombre: "))
destino = dioses.buscar_vertice(buscado2)

if (dioses.es_adyacente(buscado1,buscado2) == True):
    dios = dioses.inicio.obtener_elemento(origen)
    for j in range(dios['aristas'].tamanio()):
        arista = dios['aristas'].obtener_elemento(j)
        if(arista['destino'] == buscado2):
            print(buscado1," y ",buscado2,' son: ',arista['data']['relacion'])
else:  
    print("No existe relacion directa entre ",buscado1, " y ",buscado2)


#f. encontrar y mostrar camino mas corto entre deos dioses
buscado1 = (input("Ingrese el nombre de un dios para ver el camino mas corto con el segundo: "))
origen = dioses.buscar_vertice(buscado1)
buscado2 = (input("Ingrese el segundo nombre: "))
destino = dioses.buscar_vertice(buscado2)
camino = dioses.dijkstra(origen,destino)

destino = buscado2
costo = None
while(not camino.pila_vacia()):
    dato = camino.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(dato[1][0])
        destino = dato[1][1]
print('el costo total del camino es:', costo)

#g.barrido en profundidad y amplitud
buscado = (input("Ingrese el nombre de un dios para realizar los barridos: "))
origen = dioses.buscar_vertice(buscado)

dioses.barrido_profundidad(origen)
print()
dioses.barrido_amplitud(origen)
print()

#h. barrido mostrando el nombre de cada dios y el de su madre;
dioses.barrido_dios_madre()
print()

#j. nietos de Cronos
lista = []
print("Nietos de Kronos: ")
dioses.relaciones_nietos("Kronos","hijo",lista)


#i. mostrar los ancestros de un dios
buscado = (input("Ingrese el nombre de un dios para ver sus ancestros: "))
print("Ancestros de: ",buscado, ": ")
dioses.ancestro(buscado)

#k. hijos de Tea;
print()
print("Hijos de Theia")
dioses.relaciones("Theia","hijo")