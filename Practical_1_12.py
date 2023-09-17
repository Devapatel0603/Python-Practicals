def list_sort(list,n,c):
	list.sort(key=lambda x:x[c])

list = [["java", 1995], ["c++", 1983], ["python", 1989]] 
list_sort(list,3,1)
print(list)
num_list = [3, 328, 48, 38, 3827]
print("Number list : ",num_list)
print("Smallest : ",min(num_list))
print("Largest: ",max(num_list))
print("Addition of all members : ",sum(num_list))
