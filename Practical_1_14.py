def main():
    n = int(input("Enter number of students : "))
    student = set({})
    for _ in range(n):
        e_no = int(input("Enter student enrollment no. : "))
        student.add(e_no)
    print(student)

if __name__ == "__main__":
    main()