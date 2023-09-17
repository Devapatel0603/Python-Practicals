def main():
    stud_list = []
    n = int(input("Enter number of students : "))
    for _ in range(n):
        ins_details(stud_list)
    print(sort_spi(stud_list))

def ins_details(dic):
    di={}
    name = input("Student Name : ")
    no = int(input("Enrollment No. : "))
    spi = float(input("SPI : "))
    di["Name"] = name
    di["Enrollment_no"] = no
    di["SPI"] = spi
    dic.append(di)

def sort_spi(spi_list):
    print(sorted(spi_list,key = lambda i:i["SPI"]))
            
if __name__ == "__main__":
    main()
