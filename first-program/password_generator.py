import random


def password_generator():
    mayusculas = ["A", "B", "C", "D", "E", "F", "G"]
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    caracteres = mayusculas + minusculas + simbolos + numeros

    password = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    return "".join(password)


def run():
    password = password_generator()
    print("tu nuevo password es : " + password)


if __name__ == "__main__":
    run()
