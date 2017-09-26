fin = open("sitin.txt","r")
fout = open("sitout.txt", "w")

x,y,z = map(int,fin.read().replace("\n"," ").split(" "))
sit = x*y
stand = z - sit
s = str(sit) + " " + str(stand)
fout.write(s)
fin.close()
fout.close()
