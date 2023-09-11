def main():
    a = {1,3,5,7,9}
    b = {0,1,2,4,6,7,8}
    print(a,"\n",b,sep="")
    a.add(6)
    b.remove(0)
    print("Add 6 in a :",a)
    print("Delete 0 from b :",b)
    print("Union of a and b :",a.union(b))
    print("Intersection of a and b :",a.intersection(b))
    print("Difference between a and b :",a.difference(b))
    print("Symmetric difference between a and b :",a.symmetric_difference(b))
    print("Is 10 in a :",10 in a)

if __name__ == "__main__":
    main()