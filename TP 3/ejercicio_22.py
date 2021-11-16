from tda_cola import Cola
personaje = Cola()

class persona(object):
    nombre_personaje, nombre_super, genero = '', '', ''

    def __init__(self, nombre_personaje, nombre_super, genero):
            self.nombre_personaje = nombre_personaje
            self.nombre_super = nombre_super
            self.genero = genero
          

    def __str__(self):
          return self.nombre_personaje+': ' + self.nombre_super +'. '+ ' Genero: '+ self.genero

dato = persona ('tony stark', 'iron man', 'm') 
personaje.arribo(dato)
dato = persona ('steve rogers', 'capitan america', 'm')
personaje.arribo(dato)
dato = persona ('thor odinson', 'thor.', ' m')
personaje.arribo(dato)
dato = persona ('sam wilson', 'falcon ', 'm')
personaje.arribo(dato)
dato = persona ('carol danvers', 'capitana marvel', 'f')
personaje.arribo(dato)
dato = persona ('nati romanoff', 'black widow', 'f')
personaje.arribo(dato)
dato = persona ('wanda maximoff', 'bruja escarlata', 'f')
personaje.arribo(dato)
dato = persona ('stephen strange', 'doctor strange', 'm')
personaje.arribo(dato)
dato = persona ('bruce banner', 'hulk', 'm')
personaje.arribo(dato)
dato = persona ('scott lang', 'ant-man', 'm')
personaje.arribo(dato)


cantidad_elemento = 0
while (cantidad_elemento < personaje.tamanio()):
    dato = personaje.mover_final ()
    print (dato)
    cantidad_elemento += 1

print ()

cantidad_elemento = 0
while ( cantidad_elemento < personaje.tamanio()):
    dato = personaje.atencion()
    ##punto A
    if (dato.nombre_super == 'capitana marvel'):
        print ('Nombre real capitana marvel')
        print (dato.nombre_personaje)

    ##punto B
    if (dato.genero =='f'):
        print ('Listado de personajes femeninas')
        print (dato.nombre_super)
    
    ##punto C
    if (dato.genero =='m'):
        print ('Listado de personajes masculinos')
        print (dato.nombre_personaje)
    
    ##punto D
    if (dato.nombre_personaje == 'scott lang'):
        print ('Nombre de superheroe de scott lang')
        print (dato.nombre_super)
    
    ##Punto E
    if ((dato.nombre_personaje[0] == 's') or (dato.nombre_super[0] == 's')):
        print ('Nombres empezados por "S"')
        print (dato)
    
    ##punto F
    if (dato.nombre_personaje == 'carol danvers'):
        print ('Determinar si carol danvers existe y mostrar super nombre')
        print (dato.nombre_super)
   

    personaje.arribo(dato)
    cantidad_elemento +=1