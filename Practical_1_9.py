def gcd_hcf(a,b):
    gcd = []
    max = 0
    if(a == 0 or b == 0):
        return 0
    elif(a > b):
        for i in range(1,a):
            if(a%i == 0 and b%i == 0):
                gcd.append(i)
                if(max < i):
                    max = i
    elif(b > a):
        for i in range(1,b):
            if(a%i == 0 and b%i == 0):
                gcd.append(i)
                if(max < i):
                    max = i
    return max
c = int(input("Enter first number : "))
d = int(input("Enter second number : "))
maximum = gcd_hcf(c,d)
print("Highest Common Factor (HCF) and Greatest Common Divisor (GCD) of two numbers is : ",maximum)