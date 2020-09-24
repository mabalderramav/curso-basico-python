import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un numero del 1 al 100:'))
    while numero_aleatorio != numero_elegido:
        if numero_elegido < numero_aleatorio:
            print('Busca un nemero mas grande')
        else:
            print('Busca un numero mas pequenio')

        numero_elegido = int(input('Elige otro numero: '))

    print('Ganaste!')


if __name__ == "__main__":
    run()
