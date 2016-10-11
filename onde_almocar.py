# coding: utf-8
import pandas as pd
import numpy as np

# initializes df with some data and columns
restaurante = pd.Series(['verdilha', 'antenas', 'servidores', 'ruchello', 'ru'])
df = pd.DataFrame(restaurante)
df['distancia']=[5,4,3,1,2]
df['sabor']=[2,3,4,5,1]
df['preco']=[3,2,2,1,8]
df['fila']=[4,3,3,5,1]
df = df.rename(columns={0:'restaurante'})
df = df.set_index('restaurante')

# prints a simple message
print('\n\n--- Onde almoçar hoje? Escolha abaixo os critérios e te darei a resposta ;) ---\n')

# asks user for weights in each criterion
p_distancia = int(input('Qual o peso da distância (0-10)? '))
p_sabor 	= int(input('Qual o peso do sabor (0-10)?     '))
p_preco 	= int(input('Qual o peso do preço (0-10)?     '))
p_fila    	= int(input('Qual o peso da fila (0-10)?      '))

pesos = np.array([p_distancia, p_sabor, p_preco, p_fila])

# multiplies evaluations by the weights and prints the resulting sum, sorted
df_pesos = df*pesos
total = df_pesos.sum(axis=1)
total = total.sort_values(ascending=False)

print('\nEssas são as sugestões, por ordem de relevância: ')
print(total)
