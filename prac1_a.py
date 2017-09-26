height = int(input("Height :"))
for i in range(height):
    for j in range(height):
        print("*",end="")
    print()
print("""
               Without nested loop :""")
for i in range(height):
    print("*" * height)
