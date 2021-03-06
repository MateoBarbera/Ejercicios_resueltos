class Nodo_Cola():
    '''Crea una variable nodo cola'''
    def __init__(self):
        self.info = None
        self.sig = None


class Cola():
    '''Crea un objeto cola'''
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0


def arribo(cola, dato):
    '''Inserta un elemento al final de la cola'''
    nodo = Nodo_Cola()
    nodo.info = dato
    if cola.final is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1


def atencion(cola):
    '''Quita un elemento desde el frente de la cola'''
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = cola.frente
    cola.tamanio -= 1
    return dato


def cola_vacia(cola):
    '''Devuelve True si la cola esta vacia'''
    return cola.tamanio == 0


def tamanio_cola(cola):
    '''Tamanio de la cola'''
    return cola.tamanio


def barrido_cola(cola):
    '''Muestra los elementos de una cola'''
    if tamanio_cola(cola) > 0:
        nodo = cola.frente
        while nodo:
            print(nodo.info)
            nodo = nodo.sig


def en_frente(cola):
    '''Muestra el dato que esta al frente en la cola'''
    if tamanio_cola(cola) > 0:
        return cola.frente.info


def mover_final(cola):
    '''Quita el elemento del frente y lo mueve al final'''
    if cola.tamanio > 0:
        dato = atencion(cola)
        arribo(cola, dato)
        return dato