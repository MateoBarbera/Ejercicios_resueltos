from TDA_ColaDin import Cola, arribo, atencion, cola_vacia
from TDA_Archivo import abrir, leer
# No van: 2 3 7 10 13 18 22 24



class Arbol(object):
    def __init__(self, info=None, datos=None):
        self.info = info
        self.datos = datos
        self.der = None
        self.izq = None
        self._altura = 0


class Nodo_Arbol():
    def __init__(self, info, nrr=None):
        self.info = info
        self.izq = None
        self.der = None
        self.nrr = nrr
        self.altura = 0     

class Nodo_ArbolHuffman(): 
    def __init__(self, info, valor):
        self.izq = None
        self.der = None
        self.info = info
        self.valor = valor

class Nodo_Clima():
    def __init__(self, info, campo=None, umbral=None):
        self.info = info
        self.izq = None
        self.der = None
        self.altura = 0
        self.campo = campo
        self.umbral = umbral 

class Nodo_Greek():
    def __init__(self, info, madre, descipcion=None):
        self.izq = None
        self.der = None
        self.info = info
        self.madre = madre
        self.descripcion = descipcion

def rotar_simple(raiz, control):
    '''Realiza una rotacion simple de nodos a la derecha o a la izquierda'''
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz
    actualizar_altura(raiz)
    actualizar_altura(aux)
    raiz = aux
    return raiz


def rotar_doble(raiz, control):
    '''Realiza una rotacion doble de nodos a la derecha o a la izquierda'''
    if control:
        raiz.izq = rotar_simple(raiz.izq, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.der = rotar_simple(raiz.der, True)
        raiz = rotar_simple(raiz, False)
    return raiz

def balancear(raiz):
    '''Determina que rotacion hay que hacer para balancear el arbol'''
    if raiz is not None:
        if altura(raiz.izq)-altura(raiz.der) == 2:
            if altura(raiz.izq.izq) >= altura(raiz.izq.der):
                raiz = rotar_simple(raiz, True)
            else:
                raiz = rotar_doble(raiz, True)
        elif altura(raiz.der)-altura(raiz.izq) == 2:
            if altura(raiz.der.der) >= altura(raiz.der.izq):
                raiz = rotar_simple(raiz, False)
            else:
                raiz = rotar_doble(raiz, False)
    return raiz

def insertar_nodo(raiz, dato, nrr=None):
    'Agrega elementos a un arbol'
    if raiz is None:
        raiz = Nodo_Arbol(dato, nrr)
    else:
        if raiz.info != dato:
            raiz.izq = insertar_nodo(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar_nodo(raiz.der, dato, nrr)
        raiz = balancear(raiz)
        actualizar_altura(raiz)
    return raiz


def insertar_nodo_morse(raiz, dato):
    if raiz is None:
        raiz = Nodo_Arbol(dato)
    else:
        if raiz.info[0] > dato[0]:
            raiz.izq = insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = insertar_nodo(raiz.der, dato)
    return raiz


def insertar_nodo_clima(raiz, dato, campo=None, umbral=None):
    if raiz is None:
        raiz = Nodo_Clima(dato, campo, umbral)
    else:
        if raiz.info[0] > dato[0]:
            raiz.izq = insertar_nodo_clima(raiz.izq, dato, campo, umbral)
        else:
            raiz.der = insertar_nodo_clima(raiz.der, dato, campo, umbral)
    return raiz


def insertar_nario(padre, hijo):
    if padre.izq is None:
        #print('insertar hijo de', padre.info)
        padre.izq = hijo
    else:
        aux = padre.izq
        while aux.der is not None:
            aux = aux.der
        #print('insertar hno de', aux.info)
        aux.der = hijo


def busqueda_arbol(raiz, buscado):
    'Busca un elemento en un arbol'
    if raiz is not None:
        if raiz.info == buscado:
            return raiz
        else:
            if buscado < raiz.info:
                return busqueda_arbol(raiz.izq, buscado)
            else:
                return busqueda_arbol(raiz.der, buscado)


def busqueda_proximidad(raiz, buscado):
    if raiz is not None:
        if raiz.info[0:len(buscado)] == buscado:
            print('Se encontro:', raiz.info)
        busqueda_proximidad(raiz.izq, buscado)
        busqueda_proximidad(raiz.der, buscado)


def busqueda_nario(raiz, buscado, pos):
    if raiz is not None:
        if raiz.info == buscado:
            pos.append(raiz)
            return
        busqueda_nario(raiz.izq, buscado, pos)
        busqueda_nario(raiz.der, buscado, pos)


def reemplazar(raiz):
    aux = None
    if raiz.der is None:
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = reemplazar(raiz.der)
    return raiz, aux


def eliminar_nodo(raiz, clave):
    'Elimina un elemento de un arbol'
    x = None   # x elemento a eliminar
    if raiz is not None:
        if clave < raiz.info:
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif clave > raiz.info:
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if raiz.izq is None:
                raiz = raiz.der
            elif raiz.der is None:
                x = raiz.info
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x


def arbol_vacio(raiz):
    'Devuelve True si el arbol esta vacio'
    return raiz is None


def inorden(raiz):
    'Barrido de menor a mayor'
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


def inorden_descendente(self):
        if(self.info is not None):
            if(self.der is not None):
                self.der.inorden_descendente() 
            print(self.info, self.datos)    
            if(self.izq is not None):
                self.izq.inorden_descendente()    

def postorden(raiz):
    if raiz is not None:
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)


def preorden(raiz):
    'Barrido que muestra la raiz en primer lugar'
    if raiz is not None:
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def por_nivel(raiz):
    'Barrido por nivel'
    cola = Cola()
    arribo(cola, raiz)
    while not cola_vacia(cola):
        nodo = atencion(cola)
        print(nodo.info)
        if nodo.izq is not None:
            arribo(cola, nodo.izq)
        if nodo.der is not None:
            arribo(cola, nodo.der)


def por_nivel_meteorolgico(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while not cola_vacia(cola):
        nodo = atencion(cola)
        if nodo.campo is None or nodo.umbral is None:
            print(nodo.info)
        else:
            print(nodo.info, nodo.campo, nodo.umbral)
        if nodo.izq is not None:
            arribo(cola, nodo.izq)
        if nodo.der is not None:
            arribo(cola, nodo.der)


def por_nivel_nario(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while not cola_vacia(cola):
        nodo = atencion(cola)
        print(nodo.info)
        if nodo.izq is not None:
            arribo(cola, nodo.izq)
        hno = nodo.der
        while hno is not None:
            print(hno.info)
            if hno.izq is not None:
                arribo(cola, hno.izq)
            hno = hno.der


def generar_bosque(arbol, arbol_superheroes, arbol_villanos):
    if arbol is not None:
        arbol_superheroes, arbol_villanos = generar_bosque(arbol.izq, arbol_superheroes, arbol_villanos)
        if arbol.nrr is True:
            arbol_superheroes = insertar_nodo(arbol_superheroes, arbol.info)
        else:
            arbol_villanos = insertar_nodo(arbol_villanos, arbol.info)
        arbol_superheroes, arbol_villanos = generar_bosque(arbol.der, arbol_superheroes, arbol_villanos)
    return arbol_superheroes, arbol_villanos


def cantidad_nodos(raiz, cont=0):
    'Devuelve la cantidad de nodos de un arbol'
    if raiz is not None:
        cont = cantidad_nodos(raiz.izq, cont)
        cont += 1
        cont = cantidad_nodos(raiz.der, cont)
    return cont


def cantidad_hojas(raiz, cont=0):
    'Devuelve la cantidad de hojas de un arbol'
    if raiz is not None:
        if raiz.izq is None and raiz.der is None:
            cont += 1
            print(raiz.info, 'es una hoja')
        cont = cantidad_hojas(raiz.izq, cont)
        cont = cantidad_hojas(raiz.der, cont)
    return cont


def altura(raiz):
    '''Devuelve la altura de un nodo'''
    if raiz is None:
        return -1
    else:
        return raiz.altura


def actualizar_altura(raiz):
    if raiz is not None:
        alt_izq = altura(raiz.izq)
        alt_der = altura(raiz.der)
        raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) + 1


def hijo_der(arbol):
    if arbol.der is None:
        print(arbol.der)
    else:
        print(arbol.der.info)


def hijo_izq(arbol):
    if arbol.izq is None:
        print(arbol.izq)
    else:
        print(arbol.izq.info)


def padre(raiz, buscado):
    '''Determina el padre de un nodo'''
    if raiz is not None:
        if raiz.der is not None and raiz.der.info == buscado or raiz.izq is not None and raiz.izq.info == buscado:
            print('El padre de buscado es', raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def nodo_minimo(raiz):
    '''Obtiene el nodo minimo de un arbol'''
    if raiz.izq is not None:
        raiz = nodo_minimo(raiz.izq)
    return raiz


def nodo_maximo(raiz):
    '''Obtiene el nodo maximo de un arbol'''
    if raiz.der is not None:
        raiz = nodo_maximo(raiz.der)
    return raiz

def contar_nodos(raiz, cantidad):
    if raiz is not None:
        contar_nodos(raiz.izq, cantidad)
        contar_nodos(raiz.der, cantidad)
        cantidad += 1

def decodificar_morse(raiz, cadena):
    cadena_deco = ''
    raiz_aux = raiz
    pos = 0
    while pos < len(cadena):
        if cadena[pos] == '.':
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
    if raiz_aux is not None:
        cadena_deco += raiz_aux.info[1]
    raiz_aux = raiz
    return cadena_deco


def descifrar_morse(arbol, morse, mensaje):
    for palabra in morse.split('/'):
        x = ''
        for letra in palabra.split(' '):
            x += decodificar_morse(arbol, letra)
        mensaje += x
        mensaje += ' '
    return mensaje

def dos_arboles(self,arbol_superheroes, arbol_villanos):
        if(self.info is not None):
                if(self.datos['heroe'] == True):
                    arbol_superheroes = arbol_superheroes.insertar_nodo(self.info, self.datos)
                else:
                    arbol_villanos = arbol_villanos.insertar_nodo(self.info, self.datos)
                if(self.izq is not None):
                    self.izq.dos_arboles(arbol_superheroes, arbol_villanos)
                if(self.der is not None):
                    self.der.dos_arboles(arbol_superheroes, arbol_villanos)

def inorden_criaturas(raiz):
    'Barrido de menor a mayor'
    if raiz is not None:
        inorden_criaturas(raiz.izq)
        print(raiz.info, '/', raiz.nrr)
        inorden_criaturas(raiz.der)