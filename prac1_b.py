height = int(input("Height :"))
m = height + 1
for i in range(1,m):
	for j in range(i):
		print("*",end="")
	print()
print("""    
	       Without nested loop :  """)
for i in range(height):
	print("*" * (i+1))