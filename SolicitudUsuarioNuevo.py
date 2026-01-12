# En esta kata, se solicita al usuario un numero, si este es:
# - Divisible entre 3, el programa debe imprimir "Fizz"
# - Divisible entre 5, el programa debe imprimit "Buzz"
# - Divisible entre 3 y entre 5, el programa debe imprimir "FizzBuzz"
# - Si no es divisible ni entre 3 ni entre 5, debe imprimir el número

numero = int(input("Escribe un número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print ("FlizzBuuz")

#__________________________________________________________________________

def nombre_usuario():
    
    usuario = input("Escribe Tu Nombre:")
    
    if nombre_usuario % usuario == "pablo":
       
        print ("Bienbenido Pablo, FizzBuzz")
    
    else:
        
        print ("Usuario no admitido Fizz")

    nombre_usuario()
