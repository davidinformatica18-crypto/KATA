# En esta kata, se solicita al usuario un numero, si este es:
# - Divisible entre 3, el programa debe imprimir "Fizz"
# - Divisible entre 5, el programa debe imprimit "Buzz"
# - Divisible entre 3 y entre 5, el programa debe imprimir "FizzBuzz"
# - Si no es divisible ni entre 3 ni entre 5, debe imprimir el número

numero = int(input("Escribe un número: ")) # La variable con el nombre numero guarda el valor int y input que pregunta el numero al usuario

try:
   
 if numero % 3 == 0 and numero % 5 == 0:    # Condicional if dice que numero es divise entre 3 y es igual a 0 y nuevo numero es divise entre 5 y es igual a 0

 print ("FlizzBuuz")                         # Imprime FizzBuzz

 except ZeroDivisionError as excepcion:     # Excepcion ZeroDivisionError como excepcion

 print("No se puede dividir por ningun nombre")      # Imprime No se puede dividir por ningun nombre

 elif numero % 3 == 0:                      # Condicional elif (y si no) dice que numero es divise entre 3 y es igual a 0

    print ("Fizz")                         # Imprime Fizz

 elif numero % 5 == 0:                      # Condicional elif (y si no) dice que numero es divise entre 5 y es igual a 0

    print ("Buzz")                         # Imprime Buzz

 else:                                      # ESi no se cumple ninguna de las condiciones anteriores

    print (numero)



#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def nombre_usuario():
    
    usuario = lent(input("Escribe Tu Nombre:"))
    
    if nombre_usuario % usuario == "pablo":
       
         print ("Bienbenido Pablo, FizzBuzz")
    
    else:
        
        print ("Usuario no admitido Fizz")

    nombre_usuario()

    nombre_usuario()
