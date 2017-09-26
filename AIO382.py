fin = open("taktakin.txt","r")
fout = open("taktakout.txt", "w")

fruit = int(fin.read().strip("\n"))
#print(fruit)

i = 0
while True:
	if ((fruit - 1) % 11) == 0:
		break
	fruit *= 2
	i += 1

#print(i,fruit)
total = str(i)+" "+str(fruit)
fout.write(str(total))
fin.close()
fout.close()
