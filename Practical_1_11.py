a=[]
n = int(input("Enter number of elements in List : "))
for i in range(0,n):
    el = int(input("Enter element : "))
    a.append(el)
find = int(input("Enter a number :"))
count = 0
for i in range(0,n):
    if(find == a[i]):
        count = count+1
        flag = True
if(flag == True):
    print("Occurenrce of ",find,"is ",count)
else:
    print("There is no such element...")
    