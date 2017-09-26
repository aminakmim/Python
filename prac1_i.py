s = str(input(" Enter the string : "))

new_s = ""
p = -len(s)-1
for i in range(-1,p,-1):
    new_s += s[i]
print(new_s)
