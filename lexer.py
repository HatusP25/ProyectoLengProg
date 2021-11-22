import ply.lex as lex

# Aporte Hatus Pellegrini
reserved = {
    'if': 'IF',
    'and': 'AND',
    'alias': 'ALIAS',
    'for': 'FOR',
    'def': 'DEF',
    'begin': 'BEGIN',
    'break': 'BREAK',
    'case': 'CASE',
    'class': 'CLASS',
    'do': 'DO',
    'else': 'ELSE',
    'elsif': 'ELSIF',
    'end': 'END',
    'ensure': 'ENSURE',
    'false': 'FALSE',
    'module': 'MODULE',
    'next': 'NEXT',
    'nil': 'NIL',
    'not': 'NOT',
    'or': 'OR',
    'redo': 'REDO',
    'rescue': 'RESCUE',
    'retry': 'RETRY',
    'return': 'RETURN',
    'self': 'SELF',
    'super': 'SUPER',
    'then': 'THEN',
    'true': 'TRUE',
    'undef': 'UNDEF',
    'unles': 'UNLES',
    'until': 'UNTIL',
    'when': 'WHEN',
    'while': 'WHILE',
    'yield': 'YIELD'
}

tokens = (
             'NUMBER',
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'LPAREN',
             'RPAREN',
             'LLLAVE',
             'RLLAVE',
             'LBRACKET',
             'RBRACKET',
             'COMA',
             'DOLAR',
             'ARROBA',
             'DARROBA',
             'GUIONBAJO',
             'VARIABLE',
             'HASH',
             'ARREGLO',
             'FICHERO',
             'COMPARACION',
             'COMILLASIMPLE',
             'COMILLASDOBLE',
             "PUNTO",
             'STRING',
             'IGUAL',
             'ID',
    'BOOLEANO'
         ) + tuple(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOLAR = r'\$'
t_ARROBA = r'@'
t_DARROBA = r'@@'
t_GUIONBAJO = r'_'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMA = r','
t_COMILLASIMPLE = r"'"
t_COMILLASDOBLE = r"\""
t_PUNTO = r'\.'
t_LLLAVE = r'{'
t_RLLAVE = r'}'
t_IGUAL = r'='
t_BOOLEANO = r'TRUE|FALSE'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_STRING(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t

def t_ARREGLO(t):
    r'\[((((\"|\')[a-zA-Z]+(\"|\'),)|([0-9],))*(((\"|\')[a-zA-Z]+(\"|\'))|([0-9])))?\]'
    # r"^\[(((\d)|('.*')),)+(\d|'.*')\]$"
    return t


def t_FICHERO(t):
    r"File\.(open|new)\('[\w]+\.txt','(r|w|a)'\)"
    return t




# Aporte Moises Atupaña
# Define una regla para inicializar Hashes
def t_HASH(t):
    r'HASH\.new|{((:[a-z]+(\s)*=>(\s)*("[0-9a-zA-Z]+"|[0-9]+),)*(:[a-z]+(\s)*=>(\s)*("[0-9a-zA-Z]+"|[0-9]+)))*}'

    return t


# Define una regla para operadores de comparación
def t_COMPARACION(t):
    r'([\!\<\>]=?)|=='
    return t


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_VARIABLE(t):
    r'(^(@|@@|\$)[a-zA-z_]{1,14})|\w{1,15}'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t


lexer = lex.lex()
if __name__ == '__main__':
    lexer = lex.lex()
    data = input('analizador > ')

    # Give the lexer some input
    lexer.input(data)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
