#!/usr/bin/env python3

'''******************************************************************************
 *
 * MAT0122 ALGEBRA LINEAR I
 * Aluno: Gabriel Geraldino de Souza
 * Numero USP: 12543885
 * Tarefa: L01
 * Data: NOVEMBRO, 2021
 * 
 * DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESTE PROGRAMA. TODAS AS PARTES 
 * DO PROGRAMA, EXCETO AS QUE SÃO BASEADAS EM MATERIAL FORNECIDO PELO PROFESSOR 
 * FORAM DESENVOLVIDAS POR MIM. DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS CÓPIAS 
 * DESTE PROGRAMA E QUE NÃO DISTRIBUÍ NEM FACILITEI A DISTRIBUIÇÃO DE CÓPIAS DESTE 
 * PROGRAMA.
 *
 ******************************************************************************'''

import random
import timeit
from numpy.linalg import inv

def generate_random_matrix(order:int=3) -> list:
	matrix = [[random.random() for i in range(order)] for j in range(order)]
	return matrix

def generate_random_lower_triangular_matrix(order:int=3) -> list:
	matrix = [[0 for i in range(order)] for j in range(order)]
	for i in range(order):
		for j in range(i+1):
			matrix[i][j] = random.random()
	return matrix

def generate_random_upper_triangular_matrix(order:int=3) -> list:
	matrix = [[0 for i in range(order)] for j in range(order)]
	for i in range(order):
		for j in range(order-1, i-1, -1):
			matrix[i][j] = random.random()
	return matrix

def generate_hilbert_matrix(order:int=3) -> list:
	matrix = [[0 for i in range(order)] for j in range(order)]
	for i in range(order):
		for j in range(order):
			matrix[i][j] = 1/(i+j+1)
	return matrix

def inverse_lower(matrix:list) -> list:
	order = len(matrix)
	inverse_matrix = [[0 for i in range(order)] for j in range(order)]
	for i in range(order-1,-1,-1):
		inverse_matrix[i][i] = 1/matrix[i][i]
		for j in range(i+1, order):
			for k in range(i, j):
				inverse_matrix[j][i] += matrix[j][k]*inverse_matrix[k][i]
			inverse_matrix[j][i] /= -matrix[j][j]
	return inverse_matrix

def inverse_upper(matrix:list) -> list:
	order = len(matrix)
	inverse_matrix = [[0 for i in range(order)] for j in range(order)]
	for i in range(order):
		inverse_matrix[i][i] = 1/matrix[i][i]
		for j in range(i+1,order):
			for k in range(i, j):
				inverse_matrix[i][j] += matrix[k][j]*inverse_matrix[i][k]
			inverse_matrix[i][j] /= -matrix[j][j]
	return inverse_matrix

def inverse(matrix:list) -> list:
	order = len(matrix)
	inverse_matrix = [[i for i in row] for row in matrix]
	for i in range(order):
		for j in range(order, 2*order):
			if(j==(i+order)):
				inverse_matrix[i].append(1)
				for _ in range(j+1, 2*order):
					inverse_matrix[i].append(0)
				break
			else:
				inverse_matrix[i].append(0)
	for i in range(order):
		for j in [x for x in range(2*order) if x!=i]:
			inverse_matrix[i][j] /= inverse_matrix[i][i]
		for j in [x for x in range(order) if x!=i]: 
			for k in [x for x in range(2*order) if x!=i]: 
				inverse_matrix[j][k] -= inverse_matrix[j][i] * inverse_matrix[i][k]
	for i in range(order):
		inverse_matrix[i] = inverse_matrix[i][order:]
	return inverse_matrix

def print_matrix(matrix:list) -> None:
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print(round(matrix[i][j],2), end=" ")
		print()

#print(timeit.timeit('inverse_upper(generate_random_upper_triangular_matrix(random.randint(1,10)))', 'from __main__ import inverse_upper, generate_random_upper_triangular_matrix, random'))

testing=True
if(testing):
	'''
	4. Implemente o algoritmo do item 1 e teste o seu código para a matrizes aleatórias.
		Analise o resultado dos seus testes.
	'''
	print(f"Matrix:")
	matrix = generate_random_upper_triangular_matrix(random.randint(2,8))
	print_matrix(matrix)
	print("Inverse:")
	print_matrix(inverse_upper(matrix))
	print("numpy:")
	print(inv(matrix))
	print()

	'''
	5. Implemente o algoritmo do item 2 e teste o seu código para a matrizes aleatórias.
		Analise o resultado dos seus testes.
	'''
	print(f"Matrix:")
	matrix = generate_random_lower_triangular_matrix(random.randint(2,8))
	print_matrix(matrix)
	print("Inverse:")
	print_matrix(inverse_lower(matrix))
	print("numpy:")
	print(inv(matrix))
	print()

	''' 
	6. Implemente o algoritmo do item 3 e teste o seu código para a matriz de Hilbert
		de dimensões de 1 a 50. Analise os resultados dos seus testes.
	'''
	for i in range(1,51):
		print(f"Matrix {i}:")
		print_matrix(generate_hilbert_matrix(i))
		print("Inverse:")
		print_matrix(inverse(generate_hilbert_matrix(i)))
		print("numpy:")
		print(inv(generate_hilbert_matrix(i)))
		print()
