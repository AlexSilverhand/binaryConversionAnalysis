# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 00:45:30 2024

@author: diego
"""

import matplotlib.pyplot as plt
import math

# Pasar de decimal a binario 1
def decimalToBinary1(numero):
    operations = 1  # Contador de operaciones
    arr = [0] * 17
    i = 0
    while numero > 1:
        arr[i] = numero % 2
        numero = numero // 2
        i += 1
        operations += 3  # 1 asignación para arr[i], 1 operación de módulo, 1 operación de división
    arr[i] = numero
    operations += 2  # 1 asignación para arr[i], 1 comparación en el while
    return operations

# Pasar de decimal a binario 2
def decimalToBinary2(numero):
    operations = 1  # Contador de operaciones
    arr = [0] * 17
    i = 0
    while numero >= 0:
        if numero <= 1:
            break
        arr[i] = numero % 2
        numero = numero // 2
        i += 1
        operations += 4  # 1 asignación para arr[i], 1 operación de módulo, 1 operación de división, 1 incremento
    arr[i] = numero
    operations += 2  # 1 asignación para arr[i], 1 comparación en el while
    return operations

# Pasar de decimal a binario 3
def decimalToBinary3(numero):
    operations = 0  # Contador de operaciones
    res = 0
    if numero > 0:
        i = 0
        while numero > 1:
            res = res + (numero % 2) * 10 ** i
            numero = numero // 2
            i += 1
            operations += 4  # 1 operación de módulo, 1 operación de multiplicación, 1 operación de adición, 1 operación de división
        res = res + 10 ** i
        operations += 2  # 1 operación de adición, 1 operación de potencia
    else:
        res = 0 # 1
        operations += 1
    return operations

# Rango de valores de prueba
test_values = range(1, 101)  # Puedes ajustar el rango según lo necesario

# Inicialización de listas para almacenar los resultados
operations1 = []
operations2 = []
operations3 = []

# Ejecutar las funciones para cada valor de prueba
for value in test_values:
    operations1.append(decimalToBinary1(value))
    operations2.append(decimalToBinary2(value))
    operations3.append(decimalToBinary3(value))

# Graficar los resultados
plt.figure(figsize=(12, 6))

plt.plot(test_values, operations1, marker='o', label='Algoritmo 1')
plt.plot(test_values, operations2, marker='x', label='Algoritmo 2')
plt.plot(test_values, operations3, marker='^', label='Algoritmo 3')

plt.xlabel('Valor Decimal')
plt.ylabel('Operaciones')
plt.title('Número de Operaciones para Convertir Decimal a Binario')
plt.legend()
plt.grid(True)
plt.show()
