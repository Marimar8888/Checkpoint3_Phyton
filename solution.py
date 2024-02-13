#Exercise 1

string_new = 'Esto sería la muestra de lo que es una cadena'
age = 40
female = True
name_list = ['Maria', 'Antonia', 'Sofia']

#Exercise 2

first_three_letters = string_new[0:3]


#Exercise 3

first_element = name_list[0]


#Exercise 4

new_age = age + 10

#Exercise 5
#Si sé cuantos elementos tiene la lista
last_element = name_list[2]

#si no sé cuantos elementos tiene la lista o por defecto puedo usar el -1
last_element_two = name_list[-1]

#Exercise 6

names = 'harry,alex,susie,jared,gail,conner'

#Si la lista la quiero de un solo elemento compuesto por todos los nombres que hay en la variable names.
list_names = names.split()

#Si la lista la quiero de tantos elementos como nombres tiene el string names.
list_names_two = names.split(',')

#Exercise 7

firt_name = list_names_two[0].upper()

names_new = names.replace('harry', firt_name)

list_names_three = names_new.split(',')

#Exercise 8

email_context =f"""
Bienvenida a nuestra familia 

Por la información aportada usted tiene, {age} años.
Hay muchos miembros con edades cercanas a usted.
Espero pueda disfrutar de las actividades que se organizan 
en función de las edades en su entorno más cercano.

Un saludo
Dpto. Relaciones Sociales
"""

#Exercise 9

print('Hola mundo!')