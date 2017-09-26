height = 6

for i in range(height):
	x_range = i
	j_range = height - i
	for x in range(x_range):
		print(" ",end="")
	for j in range(j_range):
		print("*",end="")
	print()

print('''
	            Without nested loop :''')
for x in range(height):
	s = " "*x + "*" * (height - x)
	print(s)