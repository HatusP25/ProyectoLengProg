import ply.lex as lex

# Aporte Hatus Pellegrini
reserved = {
    'if': 'IF',
    'and': 'AND',
    'alias': 'ALIAS',
    'for': 'FOR',
    'begin': 'BEGIN',
    'break': 'BREAK',
    'case': 'CASE',
    'class': 'CLASS',
    'def': 'DEF',
    'defined?': 'DEFINED?',
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
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

if __name__ == '__main__':
    lexer = lex.lex()
    # Test it out
    data = '''
     3 + 4 * 10
       + -20 *2
     '''

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

