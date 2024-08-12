# Calculo de cos(x) usando la expansión de Taylor

def factorial(n):
    """Computa el factorial de n (n!)."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def cosine_series(x, terms):
    """
    Computa el coseno de x usando la serie de Taylor.

    Parámetros:
    - x: El ángulo en radianes.
    - terms: El número de términos a usar para la aproximación.

    Retorna:
    - El valor aproximado de cos(x).
    """
    cosine_approx = 0
    for n in range(terms):
        # Calculate each term in the series
        term = ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
        cosine_approx += term
    return cosine_approx

def degrees_to_radians(degrees):
    """Convierte grados a radianes."""
    return degrees * (3.141592653589793 / 180)

if __name__ == "__main__":
    while True:
        x_input = input('Introduce un valor para el ángulo x en grados: ').strip()
        try:
            x_degrees = float(x_input)
            x_radians = degrees_to_radians(x_degrees)
            break
        except ValueError:
            print("Por favor, introduce un número válido para el ángulo.")

    while True:
        terms_input = input('Introduce el número de términos: ').strip()
        try:
            terms = int(terms_input)
            if terms > 0:
                break
            else:
                print("Por favor, introduce un número entero positivo para los términos.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")

    # Ahora A contiene todos los coeficientes que el usuario introdujo
    print(f"El ángulo introducido es {x_degrees}°, o bien, {x_radians} rad.")
    print(f"El número de términos es: {terms}")

    # Calcular el coseno usando la expansión de Taylor
    cosine_value = cosine_series(x_radians, terms)

    print(f"Usando la expansión de Taylor, el coseno de {x_degrees} grados es aproximadamente: {cosine_value}")
