def main():
    tup = ()
    n = int(input("Enter number of students : "))
    for _ in range(n):
        name = input("Enter student name : ")
        marks = float(input("Enter student marks : "))
        student = {name : marks}
        tup = list(tup)
        tup.append(student)
        tup = tuple(tup)
    print(tup)

if __name__ == "__main__":
    main()