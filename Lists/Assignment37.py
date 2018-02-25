marks = {"John":86.5,"Jack":91.2,"Jill":84.5,"Harry":72.1,"Joe":80.5}

sorted_marks = sorted(marks.values())
sorted_marks.reverse()

top_3=[]

for i in range(0,3):
    top_3.append(sorted_marks[i])

print("Top 3 Courses are >",top_3)

print("Average marks >",sum(top_3)/3)
