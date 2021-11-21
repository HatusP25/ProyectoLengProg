import ply.yacc as yacc
from lexer import tokens


def p_declaracion(p):
    'declaracion : VARIABLE IGUAL asignacion'


def p_asignacion_primitivo(p):
    'asignacion : primitivo'

def p_asignacion_hash(p):
    'asignacion : HASH'

def p_asignacion_arreglo(p):
    'asignacion : ARREGLO'

def p_asignacion_fichero(p):
    'asignacion : FICHERO'

def p_primitivo_flotante(p):
    'primitivo : NUMBER PUNTO NUMBER'

def p_primitivo_number(p):
    'primitivo : NUMBER'


def p_primitivo_booleanotrue(p):
    'primitivo : TRUE'

def p_primitivo_booleanofalse(p):
    'primitivo : FALSE'

def p_error(p):
    print("Error sintactico")
    print(p)


parser = yacc.yacc()

while True:
    try:
        s = input('calc>')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
