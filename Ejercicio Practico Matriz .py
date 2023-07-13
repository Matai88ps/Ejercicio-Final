# Ejercicio Matriz Curso IBM-Bejob

try:
    # tamaño matriz.
    N = int(input("Introduce el tamaño de tu Matriz: "))

    # En el caso que introduzcan un 0.
    if N == 0:
        print("El valor 0 no genera una matriz, por favor introduce un valor mayor de 0. ")

    else:
        #Si introducen un numero negativo.
        if N < 0:
            print("El valor es menor que 0, por favor introduce un valor mayor de 0. ")

        else:
            # Crear matriz
            import random
            matriz = []
            for i in range(N):
                matriz.append([])
                for j in range(N):
                    matriz[i].append(random.randint(0, 9))

            # Mostrando en pantalla la matiz.
            print("La matriz es la siguiente:")
            for i in matriz:
                print("\t", i)

except ValueError:
    print("El valor introducido no es un numero entero.")

