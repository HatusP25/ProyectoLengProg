import ply.yacc as yacc
from lexer import tokens

def p_sentecias(p):
    '''sentencias : estructurasControl
                | declaracion
                '''

def p_estructurasControl(p):
    '''estructurasControl : estrucIf
                            | estrucElse
                            | estrucWhile
                            '''
def p_operadorMat(p):
    '''operadorMat : IGUAL
                | PLUS
                | MINUS
                | TIMES
                '''
def p_operadorLog(p):
    '''operadorLog : AND
                 | OR
                '''

def p_estrucIf(p):
    '''estrucIf : IF logica cuerpo END
                | IF logica cuerpo estrucElse
                '''

def p_logica(p):
    '''logica : condicion
                | condicion operadorLog  logica
                '''
def p_condicion(p):
    '''condicion : comparador COMPARACION comparador
                    | boolean
                    '''

def p_comparador(p):
    '''comparador : VARIABLE
                    | primitivo
                    '''

def p_estrucElse(p):
    '''estrucElse : ELSE cuerpo END
                    | ELSE logica cuerpo END
                    '''

def p_estrucWhile(p):
    ''' estrucWhile : WHILE logica cuerpo END
                    '''


def p_cuerpo(p):
    '''cuerpo : declaracion
                | declaracion cuerpo
                | cuerpo RETURN retornos
                '''

def p_retornos(p):
    '''retornos : VARIABLE
                | primitivo
                | expresion
                | asignacion
                '''

def p_declaracion(p):
    'declaracion : VARIABLE IGUAL asignacion'

def p_declaracion_funcion(p):
    'declaracion : DEF VARIABLE LPAREN params RPAREN cuerpo END'


def p_params(p):
    '''params : rubyParams
               | rubyParams COMA params
                  '''
    pass

def p_rubyParams(p):
    '''rubyParams : VARIABLE
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

#falta interpoalcion

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
