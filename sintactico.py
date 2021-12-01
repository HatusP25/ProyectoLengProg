import ply.yacc as yacc
from lexer import tokens

resultado = ""
arreglo_claves=[]
arreglo_valores=[]

# aporte de Josue Montoya Ortiz
def p_sentecias(p):
    '''sentencias : estructurasControl
                | declaracion
                | estructurasControl sentencias
                | declaracion sentencias
                | declaracion_funcion
                | declaracion_funcion sentencias
                | funcioneshash
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
    global resultado
    resultado += "\n Se declaro la sentencia if"

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
    global resultado
    resultado += "\n Se declaro la sentencia Else"


# aporte de Josue Montoya Ortiz
def p_estrucWhile(p):
    ''' estrucWhile : WHILE logica cuerpo END
                    '''
    global resultado
    resultado += "\n Se declaro la sentencia While"

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
                    | VARIABLE IGUAL hashf
                    | VARIABLE IGUAL hashf declaracion
                    | VARIABLE operadorMat IGUAL opcion
                    | VARIABLE operadorMat IGUAL opcion declaracion
                    '''
    global resultado
    resultado += f'\n Variable definida con nombre:{p[1]} y con valor {p[3]}'


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


# aporte sentencia for
def p_sentenciafor(p):
    'sentenciafor : FOR VARIABLE IN LPAREN NUMBER PUNTO PUNTO NUMBER RPAREN cuerpo END'
    global resultado
    resultado += " \n Se ha defenido un ciclo for "


def p_imprimir(p):
    '''imprimir : PUTS STRING
                | PUTS VARIABLE
    '''
    global resultado
    resultado+= f"\n Se imprimio = {p[2]}"


# aporte Hatus Pellegrini
def p_rubyParams(p):
    '''rubyParams : VARIABLE
                    | boolean
                    | NUMBER'''


# aporte Hatus Pellegrini
def p_asignacion_primitivo(p):
    '''asignacion : NUMBER
                    | boolean
                    '''
    p[0] = p[1]

def p_contenidohash(p):
    '''contenidohash : elemento
                    | elemento COMA contenidohash'''

# aporte de Moisés Atupaña
def p_hashf(p):
    'hashf : LLLAVE contenidohash RLLAVE'
    global resultado
    resultado += "\n HASH definido"


def p_elemento(p):
    'elemento : clave FHASH value'
    arreglo_claves.append(p[1])
    arreglo_valores.append(p[3])

# aporte de Moisés Atupaña
def p_asignacion_arreglo(p):
    'asignacion : ARREGLO'
    p[0] = p[1]


# aporte de Moisés Atupaña
def p_asignacion_fichero(p):
    'asignacion : FICHERO'
    p[0] = p[1]

    global resultado
    resultado+= " \n Se ha  definido un fichero"

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
    p[0] = p[1] + p[3]


# aporte Hatus Pellegrini
def p_expresion_resta(p):
    'expresion : NUMBER MINUS NUMBER'
    p[0] = p[1] - p[3]


# aporte Hatus Pellegrini
def p_expresion_term(p):
    'expresion : termino'
    p[0] = p[1]


# aporte Hatus Pellegrini
def p_termino_multi(p):
    'termino : termino TIMES factor'
    p[0] = p[1] * p[3]


# aporte Hatus Pellegrini
def p_termino_div(p):
    'termino : termino DIVIDE factor'
    p[0] = p[1] / p[3]


# aporte Hatus Pellegrini
def p_termino_factor(p):
    'termino : factor'
    p[0] = p[1]


# aporte Hatus Pellegrini
def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]


# aporte Hatus Pellegrini
def p_factor_expresion(p):
    'factor : LPAREN expresion RPAREN'
    p[0] = p[2]


# aporte Hatus Pellegrini
def p_primitivo_flotante(p):
    'primitivo : NUMBER PUNTO NUMBER'
    p[0] = p[1]


# aporte Hatus Pellegrini
def p_primitivo_number(p):
    'primitivo : NUMBER'
    p[0] = p[1]


# aporte Hatus Pellegrini
def p_primitivo_booleano(p):
    'primitivo : boolean'
    p[0] = p[1]


# aporte Hatus Pellegrini
def p_boolean(p):
    '''boolean : TRUE
             | FALSE
        '''
    p[0] = p[1]

#funciones hash-semantica Moisés Atupaña
def p_funcioneshash(p):
    '''funcioneshash : hlength
                    | haskey
                    | hkeys
                    | hvalues
                    '''
    global resultado
    resultado += "-Función de Hash"

def p_hlength(p):
    'hlength : hashf PUNTO LENGTH LPAREN  RPAREN'
    global resultado
    resultado += f"\n {len(arreglo_claves)}"
    resultado += " \n length "


# falta interpoalcion

def p_error(p):
    global resultado
    if p:
        resultado += f'\n Error Sintactico de tipo {str(p.type)} con valor: {str(p.value)}'
    else:
        resultado += '\n Error Sintactico!'


def p_haskey(p):
    'haskey : hashf HASKEY INTERROGACION LPAREN clave RPAREN'

def p_hkeys(p):
    'hkeys : hashf PUNTO KEY LPAREN value RPAREN'

def p_hvalues(p):
    'hvalues : hashf PUNTO VALUES'

def p_clave(p):
    '''clave : STRING
            | VARIABLE
            | NUMBER
            | NUMBER PUNTO NUMBER'''

def p_value(p):
    '''value : NUMBER
            | VARIABLE
             | STRING
             | boolean
             | NUMBER PUNTO NUMBER'''
# Aporte de Moisés Atupaña
data = '''
     var1=20
     var2=30
     var3=40
     var+=var2
     hash2= {name => "Joe",age=>35}
     {name => "Joe",age=>35}.length()

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
        if not st: continue
        res = parser.parse(st)
        break
    print(len(resultado))
    return resultado
