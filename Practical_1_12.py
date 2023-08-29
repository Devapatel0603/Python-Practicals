def list_sort(list,n,c):
	list.sort(key=lambda x:x[c])

list = [["java", 1995], ["c++", 1983], ["python", 1989]] 
list_sort(list,3,1)
print(list)
print("smallest : ",min(list))
print("Largest : ",list[len(list)-1])
num_list = [3,328,48,38,3827]
print("Sum : ",sum(num_list))