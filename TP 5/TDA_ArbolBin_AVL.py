from TDA_ColaDin import Cola, arribo, atencion, cola_vacia
from TDA_Archivo import abrir, leer
# No van: 2 3 7 10 13 18 22 24

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


def insertar_nodo(raiz, dato, nrr=None):
    'Agrega elementos a un arbol'
    if raiz is None:
        raiz = Nodo_Arbol(dato, nrr)
    else:
        if raiz.info > dato:
            raiz.izq = insertar_nodo(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar_nodo(raiz.der, dato, nrr)
    raiz = balancear(raiz)
    actualizar_altura(raiz)
    return raiz


def insertar_nodo_sw(raiz, dato, nrr=None):
    'Agrega elementos a un arbol'
    if raiz is None:
        raiz = Nodo_Arbol(dato, nrr)
    else:
        if raiz.info.nombre > dato.nombre:
            raiz.izq = insertar_nodo_sw(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar_nodo_sw(raiz.der, dato, nrr)
    raiz = balancear(raiz)
    actualizar_altura(raiz)
    return raiz


def insertar_nodo_cod(raiz, dato, nrr=None):
    'Agrega elementos a un arbol'
    if raiz is None:
        raiz = Nodo_Arbol(dato, nrr)
    else:
        if raiz.info.codigo > dato.codigo:
            raiz.izq = insertar_nodo_cod(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar_nodo_cod(raiz.der, dato, nrr)
    raiz = balancear(raiz)
    actualizar_altura(raiz)
    return raiz


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
        busqueda_proximidad(raiz.izq, buscado)
        if raiz.info[0:len(buscado)] == buscado:
            return print('Se encontro: ', raiz.info)
        busqueda_proximidad(raiz.der, buscado)


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
    raiz = balancear(raiz)
    actualizar_altura(raiz)
    return raiz, x


def total_nodos(raiz, cont=0):
    if raiz is not None:
        cont = total_nodos(raiz.izq, cont)
        cont += 1
        cont = total_nodos(raiz.der, cont)
    return cont


def arbol_vacio(raiz):
    'Devuelve True si el arbol esta vacio'
    return raiz is None


def inorden(raiz):
    'Barrido de menor a mayor'
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


def postorden(raiz):
    if raiz is not None:
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)


def inorden_sw(raiz):
    'Barrido de menor a mayor'
    if raiz is not None:
        inorden_sw(raiz.izq)
        print(raiz.info.nombre)
        inorden_sw(raiz.der)


def postorden_sw(raiz):
    if raiz is not None:
        postorden_sw(raiz.der)
        print(raiz.info.nombre)
        postorden_sw(raiz.izq)


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


def por_nivel_obi(raiz):
    'Barrido por nivel'
    nivel = 0
    cola = Cola()
    arribo(cola, raiz)
    while not cola_vacia(cola):
        nodo = atencion(cola)
        nivel +=1
        if nodo.info == 'Obi-Wan Kenobi':
            print('Nivel de Obi-Wan Kenobi: ', nivel)
            break
        if nodo.izq is not None:
            arribo(cola, nodo.izq)
        if nodo.der is not None:
            arribo(cola, nodo.der)


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


def inorden_nombrank(raiz, archivo):
    if raiz is not None:
        inorden_nombrank(raiz.izq, archivo)
        jedi = leer(archivo, raiz.nrr)
        if jedi[1]:
            print(raiz.info,'-', jedi[1])
        inorden_nombrank(raiz.der, archivo)


def inorden_jedimaster(raiz, archivo):
    if raiz is not None:
        inorden_jedimaster(raiz.izq, archivo)
        jedi = leer(archivo, raiz.nrr)
        if jedi[1].find('jedi master') > -1:
            print(raiz.info,'-', jedi[1])
        inorden_jedimaster(raiz.der, archivo)


def inorden_lightsaber(raiz, archivo):
    if raiz is not None:
        inorden_lightsaber(raiz.izq, archivo)
        jedi = leer(archivo, raiz.nrr)
        if jedi[4].find('green') > -1:
            print(raiz.info,'-', jedi[4])
        inorden_lightsaber(raiz.der, archivo)


def inorden_especie(raiz, archivo):
    if raiz is not None:
        inorden_especie(raiz.izq, archivo)
        jedi = leer(archivo, raiz.nrr)
        if jedi[2].find('togruta') > -1 or jedi[2].find('cerean') > -1:
            print(raiz.info,'-', jedi[2])
        inorden_especie(raiz.der, archivo)


def inorden_ayguion(raiz, archivo):
    if raiz is not None:
        inorden_ayguion(raiz.izq, archivo)
        jedi = leer(archivo, raiz.nrr)
        if jedi[0][0].find('a') > -1 or jedi[0].find('-') > -1:
            print(raiz.info,'-', jedi[2])
        inorden_ayguion(raiz.der, archivo)


def inorden_name(raiz, archivo, jedis):
    if raiz is not None:
        inorden_name(raiz.izq, archivo, jedis)
        jedi = leer(archivo, raiz.nrr)
        jedis.append(jedi)
        inorden_name(raiz.der, archivo, jedis)


def inorden_personajesw(raiz, archivo):
    if raiz is not None:
        inorden_personajesw(raiz.izq, archivo)
        personaje = leer(archivo, raiz.nrr)
        if personaje[1] and personaje[2] and personaje[3]:
            print(raiz.info,'-', personaje[1], personaje[2], personaje[3])
        inorden_personajesw(raiz.der, archivo)


def cortar_por_nivel(raiz, bosque):
    cola = Cola()
    arribo(cola, raiz)
    while not cola_vacia(cola):
        nodo = atencion(cola)
        if altura(nodo) == 7:
            bosque.append(nodo.izq)
            bosque.append(nodo.der)
        if nodo.izq is not None:
            arribo(cola, nodo.izq)
        if nodo.der is not None:
            arribo(cola, nodo.der)


def contar_nodos(raiz, cantidad):
    if raiz is not None:
        contar_nodos(raiz.izq, cantidad)
        contar_nodos(raiz.der, cantidad)
        cantidad[0] += 1


def inorden_altura(raiz, archivo):
    if raiz is not None:
        inorden_altura(raiz.izq, archivo)
        sw = leer(archivo, raiz.nrr)
        if sw.altura >= 1:
            print(raiz.info,'-', sw.altura)
        inorden_altura(raiz.der, archivo)


def inorden_peso(raiz, archivo):
    if raiz is not None:
        inorden_peso(raiz.izq, archivo)
        sw = leer(archivo, raiz.nrr)
        if sw.peso <= 75:
            print(raiz.info,'-', sw.peso)
        inorden_peso(raiz.der, archivo)


def inorden_tipo(raiz, archivo):
    if raiz is not None:
        inorden_tipo(raiz.izq, archivo)
        poke = leer(archivo, raiz.nrr)
        if poke.tipo.find('agua') > -1 or poke.tipo.find('fuego') > -1 or poke.tipo.find('planta') > -1 or poke.tipo.find('electrico') > -1:
            print(raiz.info,'es de tipo', poke.tipo)
        inorden_tipo(raiz.der, archivo)


def inorden_poke_nombre(raiz, archivo):
    if raiz is not None:
        inorden_poke_nombre(raiz.izq, archivo)
        poke = leer(archivo, raiz.nrr)
        if poke.nombre:
            print(raiz.info,'-', poke.numero)
        inorden_poke_nombre(raiz.der, archivo)


def inorden_poke_numero(raiz, archivo):
    if raiz is not None:
        inorden_poke_numero(raiz.izq, archivo)
        poke = leer(archivo, raiz.nrr)
        if poke.numero:
            print(raiz.info,'-', poke.nombre)
        inorden_poke_numero(raiz.der, archivo)


def inorden_debilidad(raiz, archivo, clave):
    if raiz is not None:
        inorden_debilidad(raiz.izq, archivo, clave)
        poke = leer(archivo, raiz.nrr)
        if poke.debilidad.find(clave) > -1:
            print(raiz.info, 'presenta debilidad al tipo', clave, '-', poke.debilidad)
        inorden_debilidad(raiz.der, archivo, clave)


def busqueda_proximidad_archivo(raiz, buscado, archivo):
    if raiz is not None:
        if raiz.info[0:len(buscado)] == buscado:
            libro = leer(archivo, raiz.nrr)
            print(libro.isbn, libro.cant, libro.titulo, libro.autores)
        busqueda_proximidad_archivo(raiz.izq, buscado, archivo)
        busqueda_proximidad_archivo(raiz.der, buscado, archivo)


def busqueda_archivo(raiz, cantidad, archivo):
    if raiz is not None:
        libro = leer(archivo, raiz.nrr)
        if libro.cant > cantidad:
            print(libro.isbn, libro.cant, libro.titulo, libro.autores)
        busqueda_archivo(raiz.izq, cantidad, archivo)
        busqueda_archivo(raiz.der, cantidad, archivo)