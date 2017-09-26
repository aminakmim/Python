fin = open("mixin.txt","r")
fout = open("mixout.txt", "w")

n,d = map(int,fin.read().split(" "))
a = n // d
b = n % d
s = str(a)+" "+str(b)+"/"+str(d) if b else str(a)


fout.write(s)
fin.close()
fout.close()
