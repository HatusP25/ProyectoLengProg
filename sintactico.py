import ply.yacc as yacc
from lexer import tokens


def p_declaracion(p):
    'declaracion : VARIABLE IGUAL asignacion'

def p_declaracion_funcion(p):
    'declaracion : DEF ID LPAREN params RPAREN'


def p_params(p):
    '''params : rubyParams
               | rubyParams COMA params
                  '''
    pass

def p_rubyParams(p):
    '''rubyParams : ID
                    | boolean
                    | NUMBER'''

def p_asignacion_primitivo(p):
    'asignacion : primitivo'

def p_asignacion_hash(p):
    'asignacion : HASH'

def p_asignacion_arreglo(p):
    'asignacion : ARREGLO'

def p_asignacion_fichero(p):
    'asignacion : FICHERO'


def p_asignacion_expresion(p):
    'asignacion : expresion'

def p_asignacion_string(p):
    'asignacion : STRING'

def p_expresion_suma(p):
    'expresion : NUMBER PLUS NUMBER'


def p_expresion_resta(p):
    'expresion : NUMBER MINUS NUMBER'


def p_expresion_term(p):
    'expresion : termino'


def p_termino_multi(p):
    'termino : termino TIMES factor'


def p_termino_div(p):
    'termino : termino DIVIDE factor'


def p_termino_factor(p):
    'termino : factor'

def p_factor_number(p):
    'factor : NUMBER'

def p_factor_expresion(p):
    'factor : LPAREN expresion RPAREN'


def p_primitivo_flotante(p):
    'primitivo : NUMBER PUNTO NUMBER'

def p_primitivo_number(p):
    'primitivo : NUMBER'


def p_primitivo_booleano(p):
    'primitivo : boolean'



def p_boolean(p):
    '''boolean : TRUE
             | FALSE
        '''

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
