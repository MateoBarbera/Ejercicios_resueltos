from tda_lista import Lista 
lista_super=Lista()

datos = [
         {'name':'Wolverine','aparicion': 1960, 'casa de comic' : 'DC', 'biografia': 'garras'},
         {'name':'Linterna Verde','aparicion': 1970, 'casa de comic' : 'MARVEL', 'biografia': 'linterna'},
         {'name':'Dr. Strange','aparicion': 1978, 'casa de comic' : 'DC', 'biografia': 'traje'},
         {'name': 'Black Panther','aparicion':1970, 'casa de comic' : 'MARVEL', 'biografia': 'armadura'},
         {'name':'Capitana Marvel','aparicion': 1976, 'casa de comic' : 'MARVEL', 'biografia': 'traje'},
         {'name':'Mujer Maravilla','aparicion': 1998, 'casa de comic' : 'DC', 'biografia': 'capa'},
         {'name':'Flash','aparicion': 1999, 'casa de comic' : 'MARVEL', 'biografia': 'rapidez'},
         {'name':'Star-Lord','aparicion': 1991, 'casa de comic' : 'MARVEL', 'biografia': 'lord'},
         {'name': 'Iron man','aparicion':1940, 'casa de comic' : 'MARVEL', 'biografia': 'armadura'},
      ]

for personas in datos:
    lista_super.insertar( personas,'name')

lista_super.barrido()
print()
#A
print('elemento eliminado: ')
print(lista_super.eliminar('Linterna Verde', 'name'))
print()

#B
pos = lista_super.busqueda('Wolverine','name')
if (pos != -1):
    print('Wolverine aparecio en el año: ', lista_super.obtener_elemento(pos)['aparicion'])

#C
pos2 = lista_super.busqueda('Dr. Strange','name')
if (pos2 != -1):
    lista_super.obtener_elemento(pos2)['casa de comic'] = 'Marvel'
print()
lista_super.barrido()
print()

#D
for i in range(lista_super.tamanio()):
    aux = lista_super.obtener_elemento(i)
    bus_traje = aux['biografia']
    if (('traje' in bus_traje) or ('armadura' in bus_traje)):
        print ('El personaje ',aux['name'],' tiene ', aux['biografia'])
        print()

#E
print ('personajes que aparecieron antes el año 1963 :')
for i in range (lista_super.tamanio()):
    aux = lista_super.obtener_elemento(i)
    if (aux['aparicion'] < 1963):
        print (aux['name'],'--',aux['casa de comic'])
        print()

#F
for i in range (lista_super.tamanio()):
    aux = lista_super.obtener_elemento(i)
    if ((aux['name'] == 'Capitana Marvel') or (aux['name'] == 'Mujer Maravilla')):
        print (aux['name'],', pertenece a la casa de ', aux['casa de comic'])
        print()    
   
#G
for i in range (lista_super.tamanio()):
    aux = lista_super.obtener_elemento(i)
    if ((aux['name'] == 'Flash') or (aux['name'] == 'Star-Lord')):
        print (aux)
    print()    

#H 
print('superheroes que empiezan con B, M, S :')
for i in range (lista_super.tamanio()):
    aux = lista_super.obtener_elemento(i)
    if (((aux['name'])[0] == 'B') or ((aux['name'])[0] == 'M') or ((aux['name'])[0] == 'S')):
        print (aux['name'])
print()    

#I
cont_marvel = 0
cont_dc = 0
for i in range(lista_super.tamanio()):
    aux = lista_super.obtener_elemento(i)
    if (aux['casa de comic'] == 'MARVEL'):
         cont_marvel += 1
    if (aux['casa de comic'] == 'DC'):
         cont_dc += 1

print (cont_marvel, ' personaje/s de marvel')
print (cont_dc, ' personaje/s de DC')

