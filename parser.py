import sys
import ply.yacc as yacc
from lexer import tokens

precedence =    (
                ('left', 'AND', 'OR'),
                ('left', 'PLUS', 'MINUS'),
                ('left', 'MUL', 'DIV')
                )

start = 'program'

def p_program(p):
    '''program  : PROGRAM ID vars functionDecs block END'''

def p_vars(p):
    '''vars     : VAR var 
                | empty '''

def p_var(p):
    '''var      : ids COLON type SEMICOLON more_var'''

def p_more_var(p):
    '''more_var : var
                | empty'''

def p_functionDecs(p):
    '''functionDecs : functionDec functionDecs
                    | empty'''

def p_functionDec(p):
    '''functionDec  : FUNCTION ID LPAREN params RPAREN vars block END'''

def p_params(p):
    '''params   : param
                | empty'''

def p_param(p):
    '''param    : type ID more_param'''

def p_more_param(p):
    '''more_param   : COMMA param
                    | empty'''

def p_ids(p):
    '''ids      : ID more_ids '''

def p_more_ids(p):
    '''more_ids : COMMA ids
                | empty'''

def p_type(p):
    '''type     : INT
                | FLO
                | STR'''

def p_block(p):
    '''block    : LBRACE statements RBRACE'''

def p_statements(p):
    '''statements   : statement SEMICOLON statements
                    | empty'''

def p_statement(p):
    '''statement    : ID assignOrFunccall
                    | instruction
                    | condition
                    | loop
                    | print'''

def p_assignOrFunccall(p):
    '''assignOrFunccall : assignment
                        | functionCall'''

#Warning: there is currently no way to assign a string value to a variable.
def p_assignment(p):
    '''assignment   : EQU ssuperexp'''

def p_functionCall(p):
    '''functionCall : LPAREN args RPAREN'''

def p_args(p):
    '''args     : arg
                | empty'''

def p_arg(p):
    '''arg      : number more_arg'''

def p_more_arg(p):
    '''more_arg : COMMA arg
                | empty'''

def p_instruction(p):
    '''instruction  : movement number
                    | DRAW boolean
                    | PRESSURE integer
                    | COLOR colorConstant
                    | ARC integer integer
                    | CIRCLE integer
                    | SQUARE integer integer'''

def p_movement(p):
    '''movement : FORWARD
                | BACKWARD
                | RIGHT
                | LEFT'''

def p_number(p):
    '''number   : integer
                | FLOAT'''

def p_boolean(p):
    '''boolean  : TRUE
                | FALSE'''

def p_integer(p):
    '''integer  : ID
                | INTEGER'''

def p_colorConstant(p):
    '''colorConstant    : RED
                        | ORANGE
                        | YELLOW
                        | GREEN
                        | BLUE
                        | CYAN
                        | PURPLE
                        | WHITE
                        | BLACK'''

def p_condition(p):
    '''condition    : IF LPAREN ssuperexp RPAREN block else END'''

def p_else(p):
    '''else     : ELSE block
                | empty '''
    
def p_loop(p):
    '''loop     : loophead block END'''

def p_loophead(p):
    '''loophead : FOR LPAREN assignments SEMICOLON ssuperexp SEMICOLON assignments RPAREN
                | WHILE LPAREN ssuperexp RPAREN'''

def p_assignments(p):
    '''assignments  : ID assignment more_assignments'''

def p_more_assignments(p):
    '''more_assignments : COMMA assignments
                        | empty'''

def p_print(p):
    '''print    : PRINT LPAREN printables RPAREN'''

def p_printables(p):
    '''printables   : printable more_printables'''

#Possible error detected: printing a "string variable"?
def p_printable(p):
    '''printable    : ssuperexp
                    | STRING'''

def p_more_printables(p):
    '''more_printables  : COMMA printables
                        | empty'''

def p_ssuperexp(p):
    '''ssuperexp    : superexp ssuperexp2'''

def p_ssuperexp2(p):
    '''ssuperexp2   : andor ssuperexp
                    | empty'''
                    
def p_andor(p):
    '''andor        : AND
                    | OR'''

def p_superexp(p):
    '''superexp   : exp compareto'''

def p_compareto(p):
    '''compareto    : comparator exp
                    | empty'''

def p_comparator(p):
    '''comparator   : CEQ
                    | CGT 
                    | CGE
                    | CLT
                    | CLE
                    | CNE'''

def p_exp(p):
    '''exp      : term exp2'''

def p_exp2(p):
    '''exp2     : sumsub exp
                | empty'''

def p_sumsub(p):
    '''sumsub   : PLUS
                | MINUS'''

def p_term(p):
    '''term     : factor term2'''

def p_term2(p):
    '''term2    : muldiv term
                | empty'''

def p_muldiv(p):
    '''muldiv   : MUL
                | DIV'''

def p_factor(p):
    '''factor   : LPAREN ssuperexp RPAREN
                | number'''

def p_empty(p):
    'empty :'
    pass

#Test routine
if __name__ == '__main__':
    if len(sys.argv) == 2:
        f = open(sys.argv[1], 'r')
        s = f.read()
        parser = yacc.yacc()
        parser.parse(s);
    else:
        print "Usage syntax: %s filename" %sys.argv[0]

