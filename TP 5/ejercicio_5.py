from TDA_ArbolBin import insertar_nodo, inorden, postorden, busqueda_proximidad, dos_arboles, cantidad_nodos

def inorden_personajes(raiz):
    if raiz is not None:
        inorden_personajes(raiz.izq)
        if raiz.nrr is True:
            print(raiz.info,'- Surperheroe')
        else:
            print(raiz.info,'- Villano')
        inorden_personajes(raiz.der)

def inorden_villanos(raiz):
    if raiz is not None:
        inorden_villanos(raiz.izq)
        if raiz.nrr is False:
            print(raiz.info)
        inorden_villanos(raiz.der)

def superheroes_c(raiz):
    if raiz is not None:
        superheroes_c(raiz.izq)
        if raiz.nrr is True and raiz.info[0] == 'C':
            print(raiz.info)
        superheroes_c(raiz.der)

def superheroes_total(raiz,total):
    if raiz is not None:
        total = superheroes_total(raiz.izq, total)
        if raiz.nrr is True:
            total += 1
        total = superheroes_total(raiz.der, total)
    return total

def postorden_superheroes(raiz):
    if raiz is not None:
        postorden_superheroes(raiz.der)
        if raiz.nrr == True:
            print(raiz.info)
        postorden_superheroes(raiz.izq)

def generar_bosque(arbol, arbol_superheroes, arbol_villanos):
    if arbol is not None:
        arbol_superheroes, arbol_villanos = generar_bosque(arbol.izq, arbol_superheroes, arbol_villanos)
        if arbol.nrr is True:
            arbol_superheroes = insertar_nodo(arbol_superheroes, arbol.info)
        else:
            arbol_villanos = insertar_nodo(arbol_villanos, arbol.info)
        arbol_superheroes, arbol_villanos = generar_bosque(arbol.der, arbol_superheroes, arbol_villanos)
    return arbol_superheroes, arbol_villanos


arbol = None
arbol_superheroes = None
arbol_villanos = None

arbol = insertar_nodo(arbol, 'Batman', True)
arbol = insertar_nodo(arbol, 'Joker', False)
arbol = insertar_nodo(arbol, 'Iron Man', True)
arbol = insertar_nodo(arbol, 'Lex Luthor', False)
arbol = insertar_nodo(arbol, 'Dr Strage', True)
arbol = insertar_nodo(arbol, 'Magneto', False)
arbol = insertar_nodo(arbol, 'Capitán America', True)
arbol = insertar_nodo(arbol, 'Thanos', False)

inorden_personajes(arbol)
print()

#b
print('Lista de villanos: ')
inorden_villanos(arbol)
print()

#c
print('Lista de superheroes que empiezan con "C": ')
superheroes_c(arbol)
print()

#d
print('Total de superheroes: ', superheroes_total(arbol,0))
print()

#e
pos = busqueda_proximidad(arbol, 'Dr Str')
if pos is not None:
    print('Se encontro: ', pos.info)

#f
print('Superheroes ordenados de manera descendente: ')
postorden_superheroes(arbol)
print()

#g
arbol_superheroes, arbol_villanos = generar_bosque(arbol, arbol_superheroes, arbol_villanos)
print('Arbol superheroes: ')
inorden(arbol_superheroes)
print('\nArbol villanos')
inorden(arbol_villanos)

print('\nCantidad de nodos superherores: ', cantidad_nodos(arbol_superheroes,0))
print('Cantidad de nodos villanos: ', cantidad_nodos(arbol_villanos,0))

print("Barrido del arbol de villanos:")
inorden(arbol_villanos)
print()
print("Barrido del arbol de heroes")
inorden(arbol_superheroes)