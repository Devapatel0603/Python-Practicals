a = [0]*10
print(a)
for i in range(0,10):
    print(f"Enter element no. {i+1} : ")
    a[i] = int(input())
odd_count = 0
even_count = 0
max_even = 0
max_odd = 0
for j in range(0,10):
    if(a[j]%2 == 0):
        even_count =even_count + 1
        if(max_even < a[j]):
            max_even = a[j]
    elif(a[j]%2 != 0):
        odd_count = odd_count + 1
        if(max_odd < a[j]):
            max_odd = a[j]
print("Total odd numbers : ",odd_count)
print("Largest odd number : ",max_odd)
print("Total even numbers : ",even_count)
print("Largest even number : ",max_even)