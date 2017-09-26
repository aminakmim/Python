from functools import reduce
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

f = lambda x: str(pages[x-1])+"\n"
ans = list(map(f,ques))
f2 = lambda x,y: x+y
s = reduce(f2,ans)
#print(ans)
fout.write(s)

#fout.write(str(ix))
fin.close()
fout.close()

