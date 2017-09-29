fin = open("tripin.txt", "r")
fout = open("tripout.txt","w")

data = list(map(int,fin.read().split("\n")))
data = data[1:]
#print(data)
found = False
for i in range(len(data)):
	if (data[i] % 3 == 0):
		found = True
		s = str(i+1)+"\n"
		fout.write(s)
if not(found):
	fout.write("Nothing here!\n")

fin.close()
fout.close()