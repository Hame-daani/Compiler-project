from mylexer import MyLexer, tokens
import ply.yacc as yacc


lexer = MyLexer()


def MyParser():
    def p_e_add(p):
        'e : e ADD t'
        p[0] = p[1] + p[3]

    def p_e_sub(p):
        'e : e SUB t'
        p[0] = p[1] - p[3]

    def p_e_negative(p):
        'e : SUB e'
        p[0] = -1 * p[2]

    def p_e_t(p):
        'e : t'
        p[0] = p[1]

    def p_t_mul(p):
        't : t MUL f'
        p[0] = p[1] * p[3]

    def p_t_div(p):
        't : t DIV f'
        p[0] = p[1] / p[3]

    def p_t_f(p):
        't : f'
        p[0] = p[1]

    def p_f_power(p):
        'f : g POWER f'
        p[0] = p[1] ** p[3]

    def p_f_g(p):
        'f : g'
        p[0] = p[1]

    def p_g_n(p):
        'g : n'
        p[0] = p[1]

    def p_g_exp(p):
        'g : LEFTPAR e RIGHTPAR'
        p[0] = p[2]

    def p_n_int(p):
        'n : INT'
        p[0] = p[1]

    def p_n_float(p):
        'n : FLOAT'
        p[0] = p[1]

    def p_error(p):
        print("syntax error!")
        
    return yacc.yacc()
