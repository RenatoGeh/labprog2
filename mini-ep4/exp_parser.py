# Yacc Expression Parser

import ply.yacc as yacc

from t_map import tokens

def p_expression_number(p):
	"expression : NUMBER"
	p[0] = p[1]

def p_expression_plus(p):
	"expression : NUMBER NUMBER PLUS"
	p[0] = p[1] + p[2]

def p_expression_minus(p):
	"expression : NUMBER NUMBER MINUS"
	p[0] = p[1] - p[2]

def p_expression_times(p):
	"expression : NUMBER NUMBER TIMES"
	p[0] = p[1] * p[2]

def p_expression_divide(p):
	"expression : NUMBER NUMBER DIVIDE"
	p[0] = p[1] / p[2]

def p_error(p):
	print "Syntax error."

parser = yacc.yacc()
line_no = 1

while True:
	try:
		line = input("%s: " % line_no)
	except EOFError:
		break
	
	if not s:
		continue

	result = parser.parse(s)
	print(result)


