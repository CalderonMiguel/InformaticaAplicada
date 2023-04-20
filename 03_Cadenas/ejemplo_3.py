a='Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.'.replace('Celsius', 'C')
print(a)


#Conceptos basicos de cadenas en Python 
fact = 'Esto es una Cadena'
fact + ' esto es otra cadena'

print(fact)

two_facts = fact + ' esto es otra variable'
print(two_facts)
####Acerca del uso de comillas 

moon_radius = "The Moon has a radius of 1,080 miles"

'The "near side" is the part of the Moon that faces the Earth'

"We only see about 60% of the Moon's surface"

#'We only see about 60% of the Moon's surface' marca error por la sintaxis de las comillas 

"""We only see about 60% of the Moon's surface, this is known as the "near side"."""
###Texto multilinea 
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

multiline = """Facts about the Moon:
...  There is no atmosphere.
...  There is no sound."""
print(multiline)

###METODOS STRING AN PYTHON 

'temperatures and facts about the moon'.title()

heading = 'temperatures and facts about the moon'
heading.title()


###Dividir cadenas 
temperatures = '''Daylight: 260 F
... Nighttime: -280 F'''
temperatures .split()

temperatures .split('\n')

#Buscar una Cadena 

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""
temperatures.find('Moon')

temperatures.find('Mars')

temperatures.count('Mars')

temperatures.count('Moon')

"The Moon And The Earth".lower()

'The Moon And The Earth'.upper()