height = int(input("Height :"))
for i in range(height):
	j_range = height - (i+1)
	k_range = 2*i + 1
	for j in range(j_range):
		print(" ",end="")
	for k in range(k_range):
		print("*",end="")
	print()
print(''' 
	           Without nested loop :''')
for i in range(height):
	j = height - (i+1)
	k = 2*i + 1
	s = " "*j + "*" * k
	print(s)