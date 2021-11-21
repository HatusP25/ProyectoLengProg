import ply.yacc as yacc
from lexer import tokens


def p_sentencias(p):
    'sentencias : VARIABLE'


def p_error(p):
    print("Error sintactico")


parser = yacc.yacc()
while True:
    try:
        s = input('calc>')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
