from Algoritmos.Algoritmos.trabajos.tda_cola_dinamico import Cola, arribo, atencion, en_frente, mover_final, tamanio
cola_o = Cola()

def imprimir_Cola(cola_o):
    mat = []
    for i in range(0, tamanio(cola_o)):
        mat.append(en_frente(cola_o))
        print('Nombre: ', mat[i][0], 
              '\nPlaneta: ', mat[i][1])

        mover_final(cola_o)
        
#A
def personajes_A_E_T_(cola_o):
    Planetas = ['Alderaan', 'Endor', 'Tatooine']
    indice = 0
    matriz_personajes = []

    for i in range(0, tamanio(cola_o)):

        if (en_frente(cola_o)[1] in Planetas):
            matriz_personajes.append(en_frente(cola_o))
            indice += 1

        mover_final(cola_o)

    return matriz_personajes

def mostrar_personajes_y_planetas_(personajes_y_Planetas):
    
    for personaje_y_Planeta in personajes_y_Planetas:
        print('Nombre: ', personaje_y_Planeta[0], 
              '\nPlaneta: ', personaje_y_Planeta[1])
        

#B
def planeta_L_H_(obj_Cola):
    luke_Y_Han = ['Luke Skywalker', 'Han Solo']
    nombre_Personajes_Y_Planetas = []

    for Planeta in range(0, tamanio(cola_o)):

        if (en_frente(cola_o)[0] in luke_Y_Han):
            nombre_Personajes_Y_Planetas.append(en_frente(cola_o))

        mover_final(cola_o)

    return nombre_Personajes_Y_Planetas

def mostrar_planeta_L_H_(personajes_y_Planetas):
    luke = []
    han = []

    for personaje_y_Planeta in personajes_y_Planetas:
        if (personaje_y_Planeta[0] == 'Luke Skywalker'):
            luke.append(personaje_y_Planeta)
        elif(personaje_y_Planeta[0] == 'Han Solo'):
            han.append(personaje_y_Planeta)
    
    if (len(luke) == 0):
        print('Luke no esta en la cola')
    else:
        print('Nombre: ', luke[0][0], 
              '\nPlaneta: ', luke[0][1])
    
    if (len(han) == 0):
        print('Han no esta en la cola')
    else:
        print('Nombre: ', han[0][0], 
              '\nPlaneta: ', han[0][1])

#C
def insertar_antes_Yoda(cola_o):
    N = input('ingrese el nombre del personaje: ')
    P = input('Ingrese el planeta natal del personaje: ')

    for i in range(0, tamanio(cola_o)):

        if (en_frente(cola_o)[0] == 'Yoda'):
            arribo(cola_o,[N, P])
        
        mover_final(cola_o)

#D
def eliminar_despues_JJ(cola_o):  
    contador = 1

    while(en_frente(cola_o)[0] != 'Jar Jar Binks'):
            mover_final(cola_o)
            contador +=1

    if(tamanio(cola_o) == contador):
        mover_final(cola_o)
    elif(en_frente(cola_o)[0] == 'Jar Jar Binks'):
        mover_final(cola_o)
        atencion(cola_o)

    for i in range(contador, tamanio(cola_o)):
        mover_final(cola_o)



cola_o = Cola()

matriz_personajes = [
    
                    ['Chewbacca', 'Anoat'],
                    ['Obi-Wan Kenobi', 'Tatooine'],
                    ['Yoda','Endor'],
                    ['BB8', 'Alderaan'],
                    ['Padme Amidala','Atollon'],
                    ['Luke Skywalker', 'Tatooine'], 
                    ['Jar Jar Binks', 'Anoat'], 
                    ['Han Solo','Corellia']
                    ]

for datos_PJ in matriz_personajes:
   arribo(cola_o,datos_PJ)

print(matriz_personajes)

print('\nPersonajes con sus planetas\n')
mostrar_personajes_y_planetas_(personajes_A_E_T_(cola_o))

print('\nPlaneta de Luke y Han\n')
mostrar_planeta_L_H_(planeta_L_H_(cola_o))

print('ingresar un personaje antes que Yoda')
insertar_antes_Yoda(cola_o)

print('eliminar personaje despues de Jar Jar')
eliminar_despues_JJ(cola_o)

imprimir_Cola(cola_o)