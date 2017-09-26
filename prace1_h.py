import re
regex = re.compile(r'[ \t\n]')
num = str(input(" Enter the number in binary :"))
num1 = regex.sub(r'',num)
print(num)
total = 0
count = len(num1) - 1
for x in num1:
    n = int(x)
    total += n* 2**count
    count -= 1
print(" Decimal value : ", total)
    
    
