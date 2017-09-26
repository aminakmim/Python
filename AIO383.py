fin = open("countin.txt","r")
fout = open("countout.txt","w")

n = int(fin.read().strip("\n")) + 1
s = ""
for i in range(1,n):
	s += str(i)+"\n"
fout.write(s)
fin.close()
fout.close()