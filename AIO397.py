from functools import reduce
fin = open("dishin.txt","r")
fout = open("dishout.txt","w")

data_str = fin.read()
data = list(map(int,data_str.split("\n")))
data1 = data[1:]
#print(data)

min_num = max_num = data1[0]
total = 0

'''for d in data1:
	if (d < min_num):
		min_num = d
	if (d > max_num):
		max_num = d
	#total += d'''
f = lambda x,y : x+y
total = reduce(f,data1)
total /= data[0]

f1 = lambda x,y: x if x<=y else y
min_num = reduce(f1,data1)

f2 = lambda x,y: y if x<=y else x
max_num = reduce(f2,data1)

#print(min_num,max_num,total)



s = str(min_num)+" "+str(max_num)+" "+str(int(total))

fout.write(s)
fin.close()
fout.close()