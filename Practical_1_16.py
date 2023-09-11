def main():
    n = int(input("Enter no. of students : "))
    student = {}
    for _ in range(n):
        name = input("Enter student name : ")
        e_no = int(input("Enter student's enrollment no. : "))
        student[e_no] = name
    print(student)
    print("Copy of student :",student.copy())
    print("Get value of specific key :")
    k = int(input("Enter key value :" )
    print(student.get(k))

if __name__ == "__main__":
    main()