# import unittest
from TEST import Bizzbuzz

# En esta kata, se solicita al usuario un numero, si este es:
# - Divisible entre 3, el programa debe imprimir "Fizz"
# - Divisible entre 5, el programa debe imprimit "Buzz"
# - Divisible entre 3 y entre 5, el programa debe imprimir "FizzBuzz"
# - Si no es divisible ni entre 3 ni entre 5, debe imprimir el número

try:

    numero = int(input("Escribe un número: ")) # La variable con el nombre numero guarda el valor int y input que pregunta el numero al usuario


    if numero % 3 == 0 and numero % 5 == 0:    # Condicional if dice que numero es divise entre 3 y es igual a 0 y nuevo numero es divise entre 5 y es igual a 0

     print ("FizzBuzz")                         # Imprime FizzBuzz

    elif numero % 3 == 0:                      # Condicional elif (y si no) dice que numero es divise entre 3 y es igual a 0
        print ("Fizz")                         # Imprime Fizz

    elif numero % 5 == 0:                      # Condicional elif (y si no) dice que numero es divise entre 5 y es igual a 0

        print ("Buzz")                         # Imprime Buzz
    else:                                      # ESi no se cumple ninguna de las condiciones anteriores

        print (numero)

except EvaluaError:                                # Excepcion para el caso que el usuario no ingrese un numero valido
    print("Por favor, ingresa un número válido.")  # Imprime mensaje de error

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def fizzbuzz(n) -> str: # Función que implementa la lógica de FizzBuzz
    
    """...divisible entre 3, el programa deve devolver fliz
    Divide entre 5, el programa deve devolver buzz
    Divisible entre 3 y 5, el programa deve devolver fizzbuzz
    Si no es divisible entre 3 ni entre 5 , deve devolver el numero"""

    if n % 3 == 0 and n % 5 == 0: # Condicional if dice que n es divise entre 3 y es igual a 0 y nuevo n es divise entre 5 y es igual a 0

        return "FizzBuzz" # Imprime FizzBuzz

    elif n % 3 == 0:      # Condicional elif (y si no) dice que n es divise entre 3 y es igual a 0

        return "Fizz"     # Imprime Fizz

    elif n % 5 == 0:      # Condicional elif (y si no) dice que n es divise entre 5 y es igual a 0

        return "Buzz"     # Imprime Buzz

    else:                 # ESi no se cumple ninguna de las condiciones anteriores

        return str(n)     # Devuelve el numero como string

        print (flizzbuzz(3)) # Prueba la funcion fizzbuzz con el numero 3
