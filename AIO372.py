fin = open("bendin.txt","r")
fout = open("bendout.txt", "w")

rec_a = fin.readline()
rec_a = rec_a.strip("\n")
x1,y1,x2,y2 = map(int,rec_a.split(" "))

if x1 > x2 :
	x1,x2 = x2,x1
	y1,y2 = y2,y1

rec_b = fin.readline()
rec_b = rec_b.strip("\n")
xa,ya,xb,yb = map(int,rec_b.split(" "))

if xa > xb :
	xa,xb = xb,xa
	ya,yb = yb,ya

area1 = (x2 - x1)*(y2 - y1)

area2 = (xb - xa)*(yb - ya)
#print(area1,area2)

px = py = px2 = py2 = 0	

if (xa <= x1 <= xb):
	px = x1 
	px2 = x2 if (x2 <= xb) else xb
elif (x1 <= xa <= x2):
	px = xa
	px2 = xb if (xb <= x2) else x2

if (ya <= y1 <= yb):
	py = y1 
	py2 = y2 if (y2 <= yb) else yb
elif (y1 <= ya <= y2):
	py = ya
	py2 = yb if (yb <= y2) else y2



area12 = (px - px2)* (py - py2)
#print(area12)

total = int(area1+area2-area12)
#print(total)
fout.write(str(total))
fin.close()
fout.close()
