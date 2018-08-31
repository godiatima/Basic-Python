# CONDITIONALS

x = 4

# BASIC IF
if x < 6:
	print('This is true')

# If Else 
if x < 6:
	print("This is true")
else:
	print('This is false')

#Elif

color = 'red'

if color == 'red':
	print('Color is red')
elif color == 'blue':
	print('Color is blue')
else:
	print('Color is not red or blue')

# Nested if
if color == 'red':
	if x < 10:
		print('Color is red and x is less than 10')
# Logical Operators
if color == 'red' and x < 10:
	print('color is red and x is less than 10')
