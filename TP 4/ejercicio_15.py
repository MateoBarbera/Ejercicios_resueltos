from tda_lilista import Lista, barrido_con_sublista,barrido,busqueda,tamanio, insertar
from random import choice, randint

class Entrenador():
    def __init__(self, entrandor, t_ganados, b_ganadas, b_perdidas):
        self.entrenador = entrandor
        self.t_ganados = t_ganados
        self.b_ganadas = b_ganadas
        self.b_perdidas = b_perdidas

    def __str__(self):
        return self.entrenador + ' | ' + str(self.t_ganados) + ' | ' + str(self.b_ganadas) + ' | ' + str(self.b_perdidas)


class Pokemon():
    def __init__(self, pokemon, nivel, tipo, subtipo):
        self.pokemon = pokemon
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return self.pokemon + ' | ' + str(self.nivel) + ' | ' + self.tipo + ' | ' + self.subtipo


def pokemon():
    lista = Lista()
    pokemon = ['Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu', 'Spearow',
               'Dugtrio', 'Primeape', 'Terrakion', 'Tyrantrum', 'Wingull']
    tipo = ['Fuego', 'Agua', 'Electrico', 'Normal', 'Veneno']
    subtipo = ['Tierra', '-', 'Planta', 'Agua', '-', 'Volador']
    dato = Entrenador('Ranchero', randint(0, 10), randint(50, 200), randint(0, 100))
    insertar(lista, dato, 'entrenador')
    dato = Entrenador('Alevin', randint(0, 10), randint(50, 200), randint(0, 100))
    insertar(lista, dato, 'entrenador')
    dato = Entrenador('Pescador', randint(0, 10), randint(50, 200), randint(0, 100))
    insertar(lista, dato, 'entrenador')
    for i in range(2):
        poke = Pokemon(choice(pokemon), randint(1, 20), choice(tipo), choice(subtipo))
        pos = busqueda(lista, 'Ranchero', 'entrenador')
        insertar(pos.sublista, poke, 'pokemon')
    for i in range(3):
        poke = Pokemon(choice(pokemon), randint(1, 20), choice(tipo), choice(subtipo))
        pos = busqueda(lista, 'Alevin', 'entrenador')
        insertar(pos.sublista, poke, 'pokemon')
    for i in range(4):
        poke = Pokemon(choice(pokemon), randint(1, 20), choice(tipo), choice(subtipo))
        pos = busqueda(lista, 'Pescador', 'entrenador')
        insertar(pos.sublista, poke, 'pokemon')
    # d
    print('NOMBRE | TORNEOS GAN. | VICTORIAS | DERROTAS')
    barrido_con_sublista(lista)
    print()
    aux = lista.inicio
    # barrido sublista
    while aux is not None:
        print('Entrenador:', aux.info.entrenador)
        print('NOMBRE | NIVEL | TIPO | SUBTIPO')
        barrido_con_sublista(aux.sublista)
        print()
        aux = aux.sig

    # a
    aux = lista.inicio
    print('Cantidad de Pokemons de un determinado entrenador')
    entr = input('Ingrese nombre del entrenador: ')
    while aux is not None:
        pos = busqueda(lista, entr, 'entrenador')
        if pos is not None:
            print(aux.info.entrenador, 'posee', tamanio(aux.sublista), 'pokemones')
        else:
            print('El entrenador no existe')
            break
        aux = aux.sig
    print()

    # b
    aux = lista.inicio
    print('Entrenadores que ganaron mas de 3 torneos')
    while aux is not None:
        if aux.info.t_ganados >= 3:
            print(aux.info.entrenador + ':', aux.info.t_ganados, 'torneos')
        aux = aux.sig
    print()

    # c
    aux = lista.inicio
    mg, mn = 0, 0
    while aux is not None:
        if aux.info.t_ganados > mg:
            mg = aux.info.t_ganados
            mas_ganador = aux.info.entrenador
        sublista = aux.sublista.inicio
        while sublista is not None:
            if sublista.info.nivel > mn:
                mn = sublista.info.nivel
                mayor_nivel = sublista.info.pokemon
            sublista = sublista.sig
        aux = aux.sig
    print('El entrenador mas ganador es', mas_ganador, 'con', mg, 'torneos')
    print('Su pokemon de mayor nivel es', mayor_nivel, 'con nivel', mn)
    print()

    # e
    aux = lista.inicio
    while aux is not None:
        batallas_totales = aux.info.b_ganadas + aux.info.b_perdidas
        porcentaje_batallas = (aux.info.b_ganadas * 100)/batallas_totales
        if porcentaje_batallas > 79:
            print(aux.info.entrenador, 'tiene un porcentaje de batalladas ganadas mayor a 79%')
        aux = aux.sig
    print()

    # f
    aux = lista.inicio
    while aux is not None:
        sublista = aux.sublista.inicio
        while sublista is not None:
            if sublista.info.tipo == 'Fuego' and sublista.info.subtipo == 'Planta':
                print(aux.info.entrenador, 'posee un pokemon tipo fuego y subtipo planta, llamado', sublista.info.pokemon)
            if sublista.info.tipo == 'Agua' and sublista.info.subtipo == 'Volador':
                print(aux.info.entrenador, 'posee un pokemon tipo agua y subtipo volador, llamado', sublista.info.pokemon)
            sublista = sublista.sig
        aux = aux.sig
    print()

    # g
    aux = lista.inicio
    while aux is not None:
        sublista = aux.sublista.inicio
        cont_nivel = 0
        while sublista is not None:
            cont_nivel += sublista.info.nivel
            prom_nivel = cont_nivel / tamanio(aux.sublista)
            sublista = sublista.sig
        # round redondea el valor prom_nivel a 2 digitos despues de la coma
        print(aux.info.entrenador + ', promedio de nivel de sus pokemons:', round(prom_nivel, 2))
        aux = aux.sig
    print()

    # h
    aux = lista.inicio
    cont = 0
    poke = input('Ingrese nombre de pokemon a buscar: ')
    while aux is not None:
        pos = busqueda(aux.sublista, poke, 'pokemon')
        if pos is not None:
            cont += 1
        aux = aux.sig
    print(cont, 'entrenadores tienen al pokemon', poke)
    print()

    # j
    aux = lista.inicio
    while aux is not None:
        sublista = aux.sublista.inicio
        while sublista is not None:
            if sublista.info.pokemon == 'Tyrantrum' or sublista.info.pokemon == 'Terrakion' or sublista.info.pokemon == 'Wingull':
                print(aux.info.entrenador, 'tiene al pokemon', sublista.info.pokemon)
            sublista = sublista.sig
        aux = aux.sig
    print()

    # k
    aux = lista.inicio
    print('Busca un entrenador y sus pokemones')
    entr = input('Ingrese nombre de entrenador a buscar: ')
    poke = input('Ingrese nombre de pokemon a buscar: ')
    while aux is not None:
        sublista = aux.sublista.inicio
        while sublista is not None:
            if entr == aux.info.entrenador and poke == sublista.info.pokemon:
                print()
                print('NOMBRE | TORNEOS GAN. | VICTORIAS | DERROTAS')
                print(aux.info)
                print()
                print('NOMBRE | NIVEL | TIPO | SUBTIPO')
                print(sublista.info)
            sublista = sublista.sig
        aux = aux.sig
