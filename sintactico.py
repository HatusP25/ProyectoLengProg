import ply.yacc as yacc
from lexer import tokens


# aporte de Josue Montoya Ortiz
def p_sentecias(p):
    '''sentencias : estructurasControl
                | declaracion
                '''


# aporte de Josue Montoya Ortiz
def p_estructurasControl(p):
    '''estructurasControl : estrucIf
                            | estrucElse
                            | estrucWhile
                            '''
# aporte de Josue Montoya Ortiz
def p_operadorMat(p):
    '''operadorMat : IGUAL
                | PLUS
                | MINUS
                | TIMES
                '''
# aporte de Josue Montoya Ortiz
def p_operadorLog(p):
    '''operadorLog : AND
                 | OR
                '''


# aporte de Josue Montoya Ortiz
def p_estrucIf(p):
    '''estrucIf : IF logica cuerpo END
                | IF logica cuerpo estrucElse
                '''


# aporte de Moisés Atupaña
def p_logica(p):
    '''logica : condicion
                | condicion operadorLog  logica
                '''


# aporte de Moisés Atupaña
def p_condicion(p):
    '''condicion : comparador COMPARACION comparador
                    | boolean
                    '''


# aporte de Moisés Atupaña
def p_comparador(p):
    '''comparador : VARIABLE
                    | primitivo
                    '''



# aporte de Josue Montoya Ortiz y Moisés Atupaña
def p_estrucElse(p):
    '''estrucElse : ELSE cuerpo END
                    | ELSE logica cuerpo END
                    '''


# aporte de Josue Montoya Ortiz
def p_estrucWhile(p):
    ''' estrucWhile : WHILE logica cuerpo END
                    '''


# aporte de Josue Montoya Ortiz
def p_cuerpo(p):
    '''cuerpo : declaracion
                | declaracion cuerpo
                | cuerpo RETURN retornos
                '''


# aporte de Josue Montoya Ortiz
def p_retornos(p):
    '''retornos : VARIABLE
                | primitivo
                | expresion
                | asignacion
                '''


# aporte de Josue Montoya Ortiz
def p_declaracion(p):
    '''declaracion : VARIABLE IGUAL asignacion
                    | VARIABLE IGUAL asignacion declaracion
                    | VARIABLE operadorMat IGUAL opcion
                    | VARIABLE operadorMat IGUAL opcion declaracion
                    '''

def p_opcion(p):
    '''opcion : VARIABLE
                | NUMBER
                '''


# aporte Hatus Pellegrini
def p_declaracion_funcion(p):
    'declaracion : DEF VARIABLE LPAREN params RPAREN cuerpo END'


# aporte Hatus Pellegrini
def p_params(p):
    '''params : rubyParams
               | rubyParams COMA params
                  '''
    pass


# aporte Hatus Pellegrini
def p_rubyParams(p):
    '''rubyParams : VARIABLE
                    | boolean
                    | NUMBER'''


# aporte Hatus Pellegrini
def p_asignacion_primitivo(p):
    'asignacion : primitivo'

# aporte de Moisés Atupaña
def p_asignacion_hash(p):
    'asignacion : HASH'

# aporte de Moisés Atupaña
def p_asignacion_arreglo(p):
    'asignacion : ARREGLO'

# aporte de Moisés Atupaña
def p_asignacion_fichero(p):
    'asignacion : FICHERO'


# aporte Hatus Pellegrini
def p_asignacion_expresion(p):
    'asignacion : expresion'

# aporte de Moisés Atupaña
def p_asignacion_string(p):
    'asignacion : STRING'


# aporte Hatus Pellegrini
def p_expresion_suma(p):
    'expresion : NUMBER PLUS NUMBER'


# aporte Hatus Pellegrini
def p_expresion_resta(p):
    'expresion : NUMBER MINUS NUMBER'


# aporte Hatus Pellegrini
def p_expresion_term(p):
    'expresion : termino'


# aporte Hatus Pellegrini
def p_termino_multi(p):
    'termino : termino TIMES factor'


# aporte Hatus Pellegrini
def p_termino_div(p):
    'termino : termino DIVIDE factor'


# aporte Hatus Pellegrini
def p_termino_factor(p):
    'termino : factor'


# aporte Hatus Pellegrini
def p_factor_number(p):
    'factor : NUMBER'


# aporte Hatus Pellegrini
def p_factor_expresion(p):
    'factor : LPAREN expresion RPAREN'


# aporte Hatus Pellegrini
def p_primitivo_flotante(p):
    'primitivo : NUMBER PUNTO NUMBER'


# aporte Hatus Pellegrini
def p_primitivo_number(p):
    'primitivo : NUMBER'


# aporte Hatus Pellegrini
def p_primitivo_booleano(p):
    'primitivo : boolean'


# aporte Hatus Pellegrini
def p_boolean(p):
    '''boolean : TRUE
             | FALSE
        '''


# falta interpoalcion

def p_error(p):
    print("Error sintactico")
    print(p)

parser = yacc.yacc()

while True:
    try:
        s = input('GRUPO_10>>')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
