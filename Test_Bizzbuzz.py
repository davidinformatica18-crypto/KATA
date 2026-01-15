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
