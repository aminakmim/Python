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
    avg = sum(ct1_list)/len(ct1_list)
    min_ct1 = min(ct1_list)
    max_ct1 = max(ct1_list)
    print("Average : ",avg,"\nMinimum : ",min_ct1,"\nMaximum : ",max_ct1)
