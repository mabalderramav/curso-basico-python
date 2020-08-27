# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('Estoy aprendiendo funciones!')

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def conversacion(mensaje):
    print('Hola')
    print('Cómo estás?')
    print(mensaje)
    print('Adios')


opcion = int(input('Elige una opcion (1, 2, 3, 4): '))
if opcion == 1:
    conversacion('Elegiste la opcion 1')
elif opcion == 2:
    conversacion('Elegiste la opcion 2')
elif opcion == 3:
    conversacion('Elegiste la opcion 3')
elif opcion == 4:
    conversacion('Elegiste la opcion 4')
else:
    print('Por favor elige la opcion correcta')
