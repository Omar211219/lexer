from nodes import *
from values import Number

class Interpreter:
	def __init__(self):
		pass

	def visit(self, node):
		method_name = f'visit_{type(node).__name__}'
		method = getattr(self, method_name)
		return method(node)
	#si solo se puso un numero
	def visit_NumberNode(self, node):
		return Number(node.value)
	#funcion para sumar
	def visit_AddNode(self, node):
		return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)
	#funcion para restar
	def visit_SubtractNode(self, node):
		return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)
	#funcion para multiplicar
	def visit_MultiplyNode(self, node):
		return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)
	#funcion para dividir
	def visit_DivideNode(self, node):
		try:
			return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
		except:
			raise Exception("Runtime math error")
