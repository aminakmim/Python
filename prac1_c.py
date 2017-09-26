height = int(input("Height :"))
m = height + 1
for i in range(1,m):
	j_range = height - i
	k_range = i
	for j in range(j_range):
		print(" ",end="")
	for k in range(k_range):
		print("*",end="")
	print()

print('''  
	               Without nested loop  :  ''')

for i in range(1,m):
	s = " "*(height - i) + "*" * i
	print(s)

