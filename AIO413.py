fin = open("dictin.txt", "r")
fout = open("dictout.txt","w")

d,w = map(int,fin.readline().split(" "))

#print(d)
#print(w)

a = fin.read().split("\n")
train = a[:d]
test = a[d:]

translation = [-1]*1000
#print(translation[1:5])

for t in train:
	temp = list(map(int,t.split(" ")))
	translation[temp[0]] = temp[1]

for t in test:
	temp2 = int(t)
	if (translation[temp2] != -1):
		s = str(translation[temp2]) + "\n"
		fout.write(s)
	else:
		s = "C?"
		fout.write(s)
'''
dictionary = {}

for t in train:
	temp = t.split(" ")
	dictionary[temp[0]] = temp[1]
#print(dictionary)

for t in test:
	try:
		s = dictionary[t] + "\n"
	except Exception as e:
		s = "C?"
	fout.write(s)'''
fin.close()
fout.close()