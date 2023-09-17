a = []
def perfect(b):
    count = 0
    sum = 0
    for i in range(1,int(n/2+1)):
        if(n % i == 0):
            a.append(i)
            count = count + 1
    for j in range(0,count):
        sum = sum + a[j]
    if(sum == n):
        print(f"{n} is a perfect number.")
    else:
        print(f"{n} is not a perfect number.")
n = int(input("Enter a number : "))
perfect(n)


