#Este script computa polinomiales de dos formas

# Primer metodo de computar polinomiales
def poly_naive(A, x):
    p = 0
    for i, a in enumerate(A):
        p += (x ** i) * a
    return p


# Segundo metodo de computar polinomiales
def poly_iter(A, x):
    p = 0
    xn = 1
    for a in A:
        p += xn * a
        xn *= x
    return p

if __name__ == "__main__":
    A = []
    while True:
        # Ask the user for a value of `a`
        a = input('Introduce un valor para \'a\' (o escribe \'n\' para terminar): ').strip()

        if a.lower() == 'n':
            break  # Exit the loop if the user types 'stop'

        try:
            # Convert the input to a float and add it to the list A
            A.append(float(a))
        except ValueError:
            print("Por favor, introduce un número válido o 'stop' para terminar.")

    while True:
        x = input('Introduce el valor de x: ').strip()
        try:
            x = float(x)
            break
        except ValueError:
            print("Por favor, introduce un número válido para x.")

    # Now A contains all the coefficients the user entered
    print("Los coeficientes introducidos son:", A)
    print("el grado polinomial a evaluar es:", x)

    r1= poly_naive(A,x)
    r2= poly_iter(A,x)
    print(f'El resultado de la evaluación por el método ingenuo del polinomio en x = {x} es {r1}')
    print(f'El resultado de la evaluación por el método de iteración del polinomio en x = {x} es {r2}')

