# ESTE ARCHIVO CONTIENE TESTS PARA LOS EJERCICIOS

def test_suma():
    assert suma(2, 3) == 5

def test_resta():
    assert resta(5, 3) == 2
    # ESTE TEST VA RESTART DOS NUMEROS
    pass

def test_resta():
    assert resta(5, 3) == 2
    # ESTE TEST VA RESTART DOS NUMEROS
    pass    

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6
    # ESTE TEST VA MULTIPLICAR DOS NUMEROS
    pass

def test_division():
    assert division(6, 2) == 3
    # ESTE TEST VA DIVIDIR DOS NUMEROS
    pass

def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(9) == "Fizz"
    # ESTE TEST VA A COMPROBAR LA FUNCION FIZZBUZZ
    pass

def test_nombre_usuario():
    assert nombre_usuario("pablo") == "Bienbenido Pablo, FizzBuzz"
    assert nombre_usuario("juan") == "Usuario no admitido Fizz"
    # ESTE TEST VA A COMPROBAR LA FUNCION NOMBRE_USUARIO
    pass   

def test_edad_usuario():
    assert edad_usuario(2000) == 26
    assert edad_usuario(1990) == 36
    # ESTE TEST VA A COMPROBAR LA FUNCION EDAD_USUARIO
    pass

def test_par_impar():
    assert par_impar(4) == "par"
    assert par_impar(5) == "impar"
    # ESTE TEST VA A COMPROBAR LA FUNCION PAR_IMPAR
    pass


def test_frutas_m():
    assert frutas_m(["manzana", "pera", "mango", "melón", "uva"]) == ["manzana", "mango", "melón"]
    # ESTE TEST VA A COMPROBAR LA FUNCION FRUTAS_M
    pass

