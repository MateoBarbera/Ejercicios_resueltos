from TDA_ArbolBin import Arbol, insertar_nodo
from TDA_ArbolBin_AVL import busqueda_proximidad, eliminar_nodo, busqueda_arbol, inorden, postorden, preorden, por_nivel

arbol_criaturas = Arbol()


arbol_criaturas = insertar_nodo(arbol_criaturas, 'nombre: Ceto  ,   capturada: ', 'descripcion: '),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre Cerda de Cromión  ,  capturada: Teseo', 'descripcion: '),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Tifón  ,  capturada: Zeus', 'descripcion: '), 
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Ortro  ,   capturada: Heracles', 'descripcion:'),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Equidna  ,  capturada: Argos Panoptes', 'descripcion: '), 
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Toro de Creta  ,  capturada: Teseo', 'descripcion: '),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Dino  ,  capturado: ', 'descripcio: '), 
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Jabalí de Calidón  , capturada: Atalanta', 'descripcion:'),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Pefredo  ,  capturada: ', 'descripcion:'),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Carcinos  ,  capturada: ', 'descripcion: '),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Enio  ,  capturada: ', 'descripcion: '),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Gerión  ,  capturada: Heracles', 'descripcion:'),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Escila  ,   capturada'  '', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Cloto  ,  capturada'  '', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Caribdis  ,  capturada'  '', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Laquesis  ,  capturada'  '', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Euríale  ,  capturada'  '', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Atropos  ,  capturada'  '', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Esteno  ,   capturada'  '', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Minotauro de Creta  ,  capturada'  'Teseo', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Medusa  ,  capturada'  'Perseo', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Harpías  ,   capturada'  '', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Ladón  ,  capturada'  'Heracles', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Argos Panoptes  ,  capturada'  'Hermes', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre  Aguila del Cáucaso   ,   capturada'  '', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre:  Aves del Estínfalo  ,  capturada'  '', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre:  Quimera  ,  capturada'  'Belerofonte', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre:  Talos  ,  capturada'  'Medea', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre:  Hidra de Lerna  ,   capturada'  'Heracles', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre:  Sirenas  ,  capturada'  '', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre:  León de Nemea  ,  capturada'  'Heracles', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre:  Pitón  ,  capturada'  'Apolo', 'descripcion' ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre:  Esfinge  ,   capturada'  'Edipo', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre:  Cierva de Cerinea  ,  capturada'  '', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre:  Dragón de la Cólquida  ,  capturada'  '', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre:  Basilisco  ,   capturada'  '', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre:  Cerbero  ,  capturada'  '', 'descripcion'  ''),
arbol_criaturas = insertar_nodo(arbol_criaturas,'nombre:  Jabalí de Erimanto  ,   capturada'  '', 'descripcion'  '') 



arbol_criaturas.inorden()

# Punto A
print ('Criaturas inorden')
arbol_criaturas.inorden_criaturas()
print()

#Punto B
criatura = input('Ingrese nombre de la criatura para agregarle una descripcion: ')
arbol_criaturas.cargar_descripcion(criatura)
print() 
arbol_criaturas.inorden()

# Punto C
print('Informacion de la criatura Talos:')
arbol_criaturas.mostrar_informacion('Talos')
print()

#Punto D
def ordenar(elemento):
    return elemento[1]

dic = ()
arbol_criaturas.contador_criaturas_derrotadas(dic)
lista = list(dic.items())
lista.sort (key = ordenar, reverse = True)

print('Los 3 heroes o dioses que derrotaron a la mayor cantidad de criaturas son:')
for i in range (3):
    print(lista[i][0], 'derroto a',  lista[i][1], 'criatura(s)')
    print()

#Punto E
print('Criaturas derrotadas por Heracles: ')
arbol_criaturas.criaturas_derrotadas('Heracles')
print()

#Punto F
print('Lista de criaturas que no han sido derrotadas:')
arbol_criaturas.criaturas_no_derrotadas()
print()

#Punto H
arbol_criaturas.modificar_captura('Cerbero', 'Heracles')
arbol_criaturas.modificar_captura('Toro de Creta', 'Heracles')
arbol_criaturas.modificar_captura('Cierva de Cerinea', 'Heracles')
arbol_criaturas.modificar_captura('Jabalí de Erimanto', 'Heracles')
arbol_criaturas.inorden_criaturas()
print ()

#Punto I
clave = input('Comience a escribir parte del nombre de una criatura para buscarla: ')
print('Criaturas que contienen "', clave, '" en su nombre:' )
arbol_criaturas.busqueda_por_coincidencia(clave)
print()

#Punto J
info, datos = arbol_criaturas.eliminar_nodo('Basilisco')
print (info, 'ha sido eliminado')
info, datos = arbol_criaturas.eliminar_nodo('Sirenas')
print (info, 'ha sido eliminado')
print()
arbol_criaturas.inorden_criaturas()
print()

#Punto K
pos = arbol_criaturas.busqueda('Aves del Estínfalo')
if (pos):
    pos.datos['capturada'] = 'Heracles'
    pos.datos['descripcion'] = 'Heracles derrotó a varias.'

# Punto L
pos = arbol_criaturas.busqueda('Ladón')
if (pos):
    nombre, datos = arbol_criaturas.eliminar_nodo('Ladón')
    datos['nombre'] = 'Dragón Ladón'
    arbol_criaturas = arbol_criaturas.insertar_nodo('Dragón Ladón', datos)
print()

# Punto M
print('Barrido por nivel del arbol:')
arbol_criaturas.barrido_por_nivel()
print()

# Punto N
print('Lista de criaturas capturadas por Heracles:')
arbol_criaturas.criaturas_derrotadas('Heracles')
print()