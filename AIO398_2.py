from functools import reduce

fin = open("rainin.txt" , "r")
fout = open("rainout.txt" , "w")

d_str = fin.read().strip("\n")
d_list = d_str.split(" ")
#print(d_list)
days = int(d_list[0])
new_d_list = list(map(int,d_list[1].split("\n")))
capacity =new_d_list[0]
predictions = new_d_list[1:]
#print(predictions)
total = 0
f = lambda x,y: x+y if x < capacity else x

fout.write(str(ix))
fin.close()
fout.close()

