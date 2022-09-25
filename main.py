from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
	try:
		# Leer la cadena de caracteres
		text = input("calc > ")
		# llamar a la funcion lexer para identificar la operacion que lo compone 
		lexer = Lexer(text)
		# guardamos la operacion del pedido
		tokens = lexer.generate_tokens()
		# llamar a la funcion parser para identificar la sintaxis
		parser = Parser(tokens)
		tree = parser.parse()
		if not tree: continue
		#realizar la funcion correspondiente
		interpreter = Interpreter()
		#extraer el resultado
		value = interpreter.visit(tree)
		#imprimir
		print(value)
	except Exception as e:
		print(e)
