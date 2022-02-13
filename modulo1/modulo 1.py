
## imprimir
from __future__ import division
from operator import truediv
from unicodedata import name


print('Hola desde la consola')

## variables
sum = 1 + 2 # 3
product = sum * 2
print(product)

## tipos de datos

planetas_en_el_sistema_solar = 8    # entero
distancia_a_alfa_centauri = 4.367   # con decimales
puede_despegar = True               # booleano
transbordador_que_aterrizo_en_la_luna = "Apollo 11"  # string

## Descubrimos su tipo de dato
type(distancia_a_alfa_centauri)

## operadores
left_side = 10
right_side = 5
left_side / right_side # 2
print("el resultado de la division es",left_side/right_side)

## operadores aritmeticos
print (1+1)
print (1-1)
print (10/2)
print (2*2)

## operadores de asignación
x=2
print(x)
x+=2
print(x)
x-=2
print(x)
x/=2
print(x)
x*=2
print(x)

## fechas
from datetime import date
date.today()
print(date.today())

## conversion de datos
print("La fecha de hoy es:" + str(date.today()))

## recopilar información
str("Alonso")
print("Bienvenido al programa de bienvenida")
name = input ("Alonso") 
print("Saludos: " & str(name ))

## trabajar con números
print("calculadora")
first_number = input(3)
second_number = input(4)
print(first_number + str( second_number))


print("calculadora")
first_number = input(3)
second_number = input(4)
print(int(first_number) + int(second_number))