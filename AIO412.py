fin = open("encyin.txt" , "r")
fout = open("encyout.txt" , "w")

d_str = fin.read().strip("\n")
d_list = d_str.split(" ")
#print(d_list)
n = int(d_list[0])
new_d_list = list(map(int,d_list[1].split("\n")))
q =new_d_list[0]

temp = n+1
pages = new_d_list[1:temp]
ques = new_d_list[temp:]
#print(pages)
#print(ques)
s = ""
for x in ques:
	#print(x,pages[x-1])
	s += str(pages[x-1]) + "\n"
fout.write(s)

#fout.write(str(ix))
fin.close()
fout.close()

