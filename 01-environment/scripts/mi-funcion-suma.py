# script.py
def MiFuncionSuma(A, B, C, imprime = True):
    resultado=A+B+C
    if imprime != False:
        print(resultado)
    return resultado
a          = 4
variable_b = 5
var_c      = 10

MiFuncionSuma(a, variable_b, var_c)



-----------------------------


def mi_funcion_suma(a, b, c, imprime=True):
    resultado = a + b + a
    if imprime:
        print(resultado)
    return resultado


a = 4
variable_b = 5
var_c = 10

mi_funcion_suma(a, variable_b, var_c)
