height = int(input("Height :"))

for i in range(height):
	j_range = height - i
	for j in range(j_range):
		print("*",end="")
	print()
print('''
	            Without nested loop :''')

for i in range(height):
	s = "*" * (height - i)
	print(s)