# Ejercicio_FizzBuzz_Assert.py

from funciones import *

# TESTS _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 


def test_suma():
   
    assert suma(2, 3) == 5

def test_resta():
    
    assert resta(5, 3) == 2


def test_multiplicacion():
  
    assert multiplicacion(2, 3) == 6


def test_division():
    
    assert division(6, 2) == 3

# TEST FIZZBUZZ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


def test_fizzbuzz():

    assert fizzbuzz(15) == "FizzBuzz"

    assert fizzbuzz(9) == "Fizz"

# TEST USUARIO _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


def test_nombre_usuario():

    assert nombre_usuario("pablo") == "Bienbenido Pablo, FizzBuzz"

    assert nombre_usuario("juan") == "Usuario no admitido Fizz"


def test_edad_usuario():

    assert edad_usuario(2000) == 26 # Si nació en 2000 tiene 26 años

    assert edad_usuario(1990) == 36 # Si nació en 1990 tiene 36 años

# TEST PAR / IMPAR _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def test_par_impar():
  
    assert par_impar(4) == "par"  # 4 es par

    assert par_impar(5) == "impar" # 5 es impar

# TEST FRUTAS _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _


def test_frutas_m():

    frutas = ["manzana", "pera", "mango", "melón", "uva"]

    assert frutas_m(frutas) == ["manzana", "mango", "melón"] # Solo tienen que salir las que empiezan por m _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
