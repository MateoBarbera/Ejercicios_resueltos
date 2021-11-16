from tda_cola import Cola
from heap import HeapMax

cola_prioridad = HeapMax()

# A
cola_prioridad.arribo('DocEmpleado1', 1)
cola_prioridad.arribo('DocEmpleado2', 1)
cola_prioridad.arribo('DocEmpleado3', 1)


# B
print('el primer objeto de la cola es: ' )
print(cola_prioridad.atencion())
print()


# C
cola_prioridad.arribo('DocTI1', 2)
cola_prioridad.arribo('DocTI2', 2)


# D
cola_prioridad.arribo('DocGerente1', 3)

# E
print('los dos primeros objetos de la cola son:')
print(cola_prioridad.atencion())
print(cola_prioridad.atencion())
print()

# F
cola_prioridad.arribo('DocEmpleado4', 1)
cola_prioridad.arribo('DocEmpleado5', 1)
cola_prioridad.arribo('DocGerente2', 3)

# G
print('todos los objetos de la cola: ')
while(not cola_prioridad.vacio()):
    print(cola_prioridad.atencion())

print()