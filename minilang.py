# =====================================================
# Analizador Sintáctico y Semántico con Verificación de Tipos
# Lenguaje MiniLang - Desarrollado para práctica de Compiladores
# =====================================================

import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'ID', 'NUM', 'FLOAT', 'STRING',
    'MAS', 'MENOS', 'POR', 'DIV',
    'ASIGNAR', 'PUNTOYCOMA', 'PARIZQ', 'PARDER'
)

t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIV = r'/'
t_ASIGNAR = r'='
t_PUNTOYCOMA = r';'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_ignore = ' \t'

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = str(t.value.strip('"'))
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# PRECEDENCIA DE OPERADORES
precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIV'),
)

tabla_simbolos = {}

# REGLAS DE PRODUCCIÓN
def p_sentencias(p):
    '''sentencias : sentencias sentencia
                  | sentencia'''
    pass

def p_sentencia_asignacion(p):
    'sentencia : ID ASIGNAR expresion PUNTOYCOMA'
    tipo, valor = p[3]
    tabla_simbolos[p[1]] = (tipo, valor)
    print(f"Asignado: {p[1]} = {valor} ({tipo})")

def p_expresion_binaria(p):
    '''expresion : expresion MAS expresion
                 | expresion MENOS expresion
                 | expresion POR expresion
                 | expresion DIV expresion'''
    tipo1, val1 = p[1]
    tipo2, val2 = p[3]

    if tipo1 == 'string' or tipo2 == 'string':
        if p[2] == '+' and tipo1 == tipo2 == 'string':
            p[0] = ('string', val1 + val2)
        else:
            print("Error semántico: operación inválida entre cadenas.")
            p[0] = ('error', None)
        return

    if tipo1 == 'error' or tipo2 == 'error':
        p[0] = ('error', None)
        return

    if tipo1 != tipo2:
        print(f"Advertencia: conversión implícita entre {tipo1} y {tipo2}")
        tipo_result = 'float'
    else:
        tipo_result = tipo1

    try:
        if p[2] == '+': p[0] = (tipo_result, val1 + val2)
        elif p[2] == '-': p[0] = (tipo_result, val1 - val2)
        elif p[2] == '*': p[0] = (tipo_result, val1 * val2)
        elif p[2] == '/':
            if val2 == 0:
                print("Error semántico: división por cero.")
                p[0] = ('error', None)
            else:
                p[0] = ('float', val1 / val2)
    except:
        print("Error semántico en operación aritmética.")
        p[0] = ('error', None)

def p_expresion_num(p):
    '''expresion : NUM
                 | FLOAT'''
    if isinstance(p[1], int):
        p[0] = ('int', p[1])
    else:
        p[0] = ('float', p[1])

def p_expresion_string(p):
    'expresion : STRING'
    p[0] = ('string', p[1])

def p_expresion_id(p):
    'expresion : ID'
    if p[1] in tabla_simbolos:
        p[0] = tabla_simbolos[p[1]]
    else:
        print(f"Error semántico: variable '{p[1]}' no definida.")
        p[0] = ('error', None)

def p_expresion_parentesis(p):
    'expresion : PARIZQ expresion PARDER'
    p[0] = p[2]

def p_error(p):
    if p:
        print(f"Error sintáctico en token '{p.value}' (línea {p.lineno})")
    else:
        print("Error sintáctico al final del archivo")

parser = yacc.yacc()

# PROGRAMA PRINCIPAL
if __name__ == '__main__':
    print("=== Luis E Nunez--1081958 - Analizador Sintáctico y Semántico ===")
    print("Escribe una sentencia o presiona Ctrl+Z (Windows) o Ctrl+D (Linux) para salir.\n")
    while True:
        try:
            entrada = input('MiniLang > ')
        except EOFError:
            break
        if not entrada:
            continue
        parser.parse(entrada)
