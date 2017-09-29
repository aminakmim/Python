fin = open("listin.txt" , "r")
fout = open("listout.txt" , "w")

data = fin.read().split("\n")
data = data[1:]
#print(data)

frndlist = {}
for t in data:
	temp = t.split(" ")
	frndlist[temp[0]] = frndlist.get(temp[0],0) + 1
	frndlist[temp[1]] = frndlist.get(temp[1],0) + 1
#print(frndlist.keys())

max_val = max(frndlist.values())
max_list = []
for f in frndlist:
	if (frndlist[f] == max_val):
		#print(f)
		max_list.append(f)
max_list.sort()
for i in max_list:
	s = i + "\n"
	fout.write(s)
fin.close()
fout.close()