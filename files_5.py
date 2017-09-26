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
    	temp.append(m[0])
    	temp.append(ct1)
    	temp.append(ct2)
    	new_marks_list.append(temp)
    	ct1_list.append(ct1)
    	ct2_list.append(ct2)
    #print(new_marks_list)
    ct1_list_tuple = list(enumerate(ct1_list))
    ct2_list_tuple = list(enumerate(ct2_list))
    ct1_list_tuple = sorted(ct1_list_tuple, key=lambda x: x[1])
    ct2_list_tuple = sorted(ct2_list_tuple, key=lambda x: x[1])
    h = ct1_list_tuple[-1][0]
    print("Highest in CT1 : ",new_marks_list[h][0])
    l = ct2_list_tuple[0][0]
    print("Lowest in CT2 : ",new_marks_list[l][0])
