import ply.lex as lex
import ply.yacc as yacc

# --- Symbol table to hold variable values ---
variables = {}

# ---------- LEXER ---------- #
tokens = (
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'ASSIGN', 'PLUSASSIGN',
    'LPAREN', 'RPAREN',
    'GT', 'LT', 'GE', 'LE', 'EQ', 'NE',
    'AND', 'OR', 'NOT',
    'QUESTION', 'COLON',
    'BOOL'
)

t_PLUS       = r'\+'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'/'
t_ASSIGN     = r'='
t_PLUSASSIGN = r'\+='
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_GT         = r'>'
t_LT         = r'<'
t_GE         = r'>='
t_LE         = r'<='
t_EQ         = r'=='
t_NE         = r'!='
t_AND        = r'&&'
t_OR         = r'\|\|'
t_NOT        = r'!'
t_QUESTION   = r'\?'
t_COLON      = r':'

def t_BOOL(t):
    r'true|false'
    t.value = True if t.value == 'true' else False
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    raise SyntaxError(f"Illegal character '{t.value[0]}'")

lexer = lex.lex()

# ---------- PARSER ---------- #
precedence = (
    ('right', 'ASSIGN', 'PLUSASSIGN'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NE'),
    ('left', 'GT', 'LT', 'GE', 'LE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'NOT'),
    ('right', 'QUESTION', 'COLON')
)

def p_statement_expr(p):
    '''statement : expression'''
    p[0] = p[1]

def p_statement_assign(p):
    '''statement : ID ASSIGN expression
                 | ID PLUSASSIGN expression'''
    var = p[1]
    if p[2] == '=':
        variables[var] = p[3]
    elif p[2] == '+=':
        variables[var] = variables.get(var, 0) + p[3]
    p[0] = variables[var]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression GT expression
                  | expression LT expression
                  | expression GE expression
                  | expression LE expression
                  | expression EQ expression
                  | expression NE expression
                  | expression AND expression
                  | expression OR expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] == 0:
            raise ZeroDivisionError("Division by zero")
        p[0] = p[1] / p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '&&':
        p[0] = bool(p[1]) and bool(p[3])
    elif p[2] == '||':
        p[0] = bool(p[1]) or bool(p[3])

def p_expression_not(p):
    'expression : NOT expression'
    p[0] = not p[2]

def p_expression_ternary(p):
    'expression : expression QUESTION expression COLON expression'
    p[0] = p[3] if p[1] else p[5]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_bool(p):
    'expression : BOOL'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    p[0] = variables.get(p[1], 0)

def p_error(p):
    raise SyntaxError("Syntax error in input")

parser = yacc.yacc()

# ---------- Entry Point ---------- #
def forecast(units):
    """Fake forecast: increases usage by 15%"""
    return units * 1.15

def evaluate_expression(input_str):
    # Handle fake function call
    if "forecast(" in input_str:
        import re
        match = re.findall(r'forecast\((.*?)\)', input_str)
        for expr in match:
            try:
                val = evaluate_expression(expr)
                input_str = input_str.replace(f"forecast({expr})", str(forecast(val)))
            except Exception as e:
                raise Exception(f"Forecast error: {str(e)}")
    return parser.parse(input_str)

