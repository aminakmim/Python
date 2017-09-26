fin = open("addin.txt","r")
fout = open("addout.txt", "w")

x,y = map(int,fin.read().split(" "))
z = x+y
#z = int(x)+int(y)
fout.write(str(z))
fin.close()
fout.close()
