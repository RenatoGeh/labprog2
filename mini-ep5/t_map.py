# Lexer Token Map

import ply.lex as lex

tokens = (
	'NUMBER',
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE'
)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'

def t_NUMBER(token):
	r'\d+'
	token.value = int(token.value)
	return token

t_ignore = r' \t'

def t_error(token):
	print("'%s' is not a valid token." % token.value[0])
	token.lexer.skip(1)

lexer = lex.lex()

