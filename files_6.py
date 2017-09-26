import csv

with open("marks.csv") as f:
    marks_list = list(csv.reader(f))
    marks_list = marks_list[1:]
    new_marks_list = []
    ct1_list = []
    ct2_list = []
    for m in marks_list:
        temp = []
        ct1 = int(m[1].strip("\t"))
        ct2 = int(m[2].strip("\t"))
        total = ct1 + ct2
        temp.append(m[0])
        temp.append(ct1)
        temp.append(ct2)
        temp.append(total)
        new_marks_list.append(temp)
        print(temp[0],temp[-1])
        
    #print(new_marks_list)
    
