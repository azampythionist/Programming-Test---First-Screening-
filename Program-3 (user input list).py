#Question 3 (user values for the input list)
li=[1,2,3,4,5,6,7,8,9]
#l1=[1,2,8,9,12,46,76,82,15,20,30]
l1=[]
for i in range(10+1):
    values=int(input("Enter values for input list:"))
    l1.append(values)                                  # random values given from the user for the input list
    print("input list:", l1)
total_1=[]
total_2=[]
total_3=[]
total_4=[]
total_5=[]
total_6=[]
total_7=[]
total_8=[]
total_9=[]
for i in l1:
    if i%1==0:
        total_1.append(i)      #input lists values are appended if they are multiples of 1
        t_1=len(total_1)       #total length/no. of multiples of 1 from input list(l1)
for j in l1:
    if j%2==0:
        total_2.append(j)      #input lists values are appended if they are multiples of 2
        t_2=len(total_2)       #total length/no. of multiples of 2 from input list(l1)
for k in l1:
    if k%3==0:
        total_3.append(k)
        t_3=len(total_3)
for l in l1:
    if l%4==0:
        total_4.append(l)
        t_4=len(total_4)
for m in l1:
    if m%5==0:
        total_5.append(m)
        t_5=len(total_5)
for n in l1:
    if n%6==0:
        total_6.append(n)
        t_6=len(total_6)
for o in l1:
    if o%7==0:
        total_7.append(o)
for p in l1:
    if p%8==0:
        total_8.append(p)
        t_8=len(total_8)
for q in l1:
    if q%9==0:
        total_9.append(q)
        t_9=len(total_9)
t_all=[t_1,t_2,t_3,t_4,t_5,t_6,len(total_7),t_8,t_9]
z=zip(li,t_all)
print(dict(z))
