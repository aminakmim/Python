fin = open("addin.txt","s")
fout = open("addout.txt", "t")

x,y = map(int,fin.read().split(" "))
z = x+y
#z = int(x)+int(y)
fout.write(str(z))
fin.close()
fout.close()
