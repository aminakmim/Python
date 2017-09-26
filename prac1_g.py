height = int(input(" Height :"))

x_range = 2*(height - 1)

new_height = x_range // 2

for x in range(x_range,-1,-1):
	k_range = abs(x - new_height)
	j_range = 2*(height - k_range) - 1
	for k in range(k_range):
		print(" ",end="")
	for j in range(j_range):
		print("*",end="")
	print()
print(''' 
	      ................ Without nested loop..................''')

for x in range(x_range,-1,-1):
	k = abs(x - new_height)
	j = 2*(height - k) - 1
	s = " " * k + "*" * j
	print(s)