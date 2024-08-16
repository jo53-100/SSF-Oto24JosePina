import math


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
    return degrees * (math.pi / 180)


def display_table(x_degrees, max_terms):
    """
    Displays a table of cosine approximations and their errors for a range of terms.

    Parameters:
    - x_degrees: The angle in degrees.
    - max_terms: The maximum number of terms to use for approximation.
    """
    x_radians = degrees_to_radians(x_degrees)  # Convert degrees to radians
    true_value = math.cos(x_radians)  # True cosine value

    # Print table header
    print(f"{'Términos':<10} {'Aproximación':<20} {'Valor Real':<20} {'Error (%)':<20}")
    print("=" * 70)

    # Print table rows
    for terms in range(1, max_terms + 1):
        approx_value = cosine_series(x_radians, terms)
        error = abs(true_value - approx_value)
        print(f"{terms:<10} {approx_value:<20.10f} {true_value:<20.10f} {error:<20.10f}")


if __name__ == "__main__":
    while True:
        x_input = input('Introduce un valor para el ángulo x en grados: ').strip()
        try:
            x_degrees = float(x_input)
            break
        except ValueError:
            print("Por favor, introduce un número válido para el ángulo.")

    while True:
        terms_input = input('Introduce el número máximo de términos: ').strip()
        try:
            max_terms = int(terms_input)
            if max_terms > 0:
                break
            else:
                print("Por favor, introduce un número entero positivo para los términos.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")

    # Now x_degrees and max_terms contain the user inputs
    print(f"El ángulo introducido es {x_degrees}°.")
    print(f"El número de términos es: {max_terms}")

    # Display the table of approximations for all term counts from 1 to max_terms
    display_table(x_degrees, max_terms)

    # Display the true value using math library
    valor_función = math.cos(degrees_to_radians(x_degrees))
    print(f"Usando la biblioteca math, el valor del coseno con {x_degrees} grados es {valor_función}")
