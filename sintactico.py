import ply.yacc as yacc
from lexer import tokens

resultado= ""
# aporte de Josue Montoya Ortiz
def p_sentecias(p):
    '''sentencias : estructurasControl
                | declaracion
                | estructurasControl sentencias
                | declaracion sentencias
                | declaracion_funcion
                | declaracion_funcion sentencias
                '''


# aporte de Josue Montoya Ortiz
def p_estructurasControl(p):
    '''estructurasControl : estrucIf
                            | estrucWhile
                            | sentenciafor
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
                | imprimir
                | imprimir cuerpo
                | estructurasControl
                | estructurasControl cuerpo
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
    global resultado
    resultado+= "\n variable definida : " + p[1]

def p_opcion(p):
    '''opcion : VARIABLE
                | NUMBER
                '''


# aporte Hatus Pellegrini
def p_declaracion_funcion(p):
    'declaracion_funcion : DEF VARIABLE LPAREN params RPAREN cuerpo END'


# aporte Hatus Pellegrini
def p_params(p):
    '''params : rubyParams
               | rubyParams COMA params
                  '''
    pass

#aporte sentencia for
def p_sentenciafor(p):
    'sentenciafor : FOR VARIABLE IN LPAREN NUMBER PUNTO PUNTO NUMBER RPAREN cuerpo END'

def p_imprimir(p):
    '''imprimir : PUTS STRING
                    | PUTS VARIABLE
    '''

# aporte Hatus Pellegrini
def p_rubyParams(p):
    '''rubyParams : VARIABLE
                    | boolean
                    | NUMBER'''


# aporte Hatus Pellegrini
def p_asignacion_primitivo(p):
    'asignacion : primitivo'
    p[0]=p[1]


# aporte de Moisés Atupaña
def p_asignacion_hash(p):
    'asignacion : HASH'
    p[0] = p[1]


# aporte de Moisés Atupaña
def p_asignacion_arreglo(p):
    'asignacion : ARREGLO'
    p[0] = p[1]


# aporte de Moisés Atupaña
def p_asignacion_fichero(p):
    'asignacion : FICHERO'
    p[0] = p[1]


# aporte Hatus Pellegrini
def p_asignacion_expresion(p):
    'asignacion : expresion'
    p[0] = p[1]


# aporte de Moisés Atupaña
def p_asignacion_string(p):
    'asignacion : STRING'
    p[0] = p[1]


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
    p[0] = p[1]


# aporte Hatus Pellegrini
def p_factor_expresion(p):
    'factor : LPAREN expresion RPAREN'


# aporte Hatus Pellegrini
def p_primitivo_flotante(p):
    'primitivo : NUMBER PUNTO NUMBER'
    p[0] = p[1]


# aporte Hatus Pellegrini
def p_primitivo_number(p):
    'primitivo : NUMBER'
    p[0]=p[1]



# aporte Hatus Pellegrini
def p_primitivo_booleano(p):
    'primitivo : boolean'
    p[0] = p[1]


# aporte Hatus Pellegrini
def p_boolean(p):
    '''boolean : TRUE
             | FALSE
        '''


# falta interpoalcion

def p_error(p):
    print("Error sintactico")
    print(p)



# Aporte de Moisés Atupaña
data = '''
     var1=20
     var2=30
     var3=40
     var+=var2
     hash2= {:name => "Joe",:age=>35} 
     arreglo1=[8,'nose',4]
     def suma(var1,var2)
        var=5
        var=6
     end
     if var1<20
        var1=100
     else 
        var1=0
     end
     for i in(1..9)
        puts "hola mundo"
        for j in(1..9)
            puts "Adios mundo"
        end
     end
     while 12>10 and 2<3
        puts "hola mundo"
    end
     
     '''
parser = yacc.yacc()
def getSintactico(data):
    global resultado
    resultado += ""
    while True:
        try:
            st = data
        except EOFError:
            break
        if not st : continue
        res = parser.parse(st)
        break
    print(len(resultado))
    return resultado

