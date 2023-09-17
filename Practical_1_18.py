def main():
    stud_list = []
    n = int(input("Enter number of students : "))
    for _ in range(n):
        ins_details(stud_list)
    # print(stud_list)
    print(sort_spi(stud_list))

def ins_details(dic):
    dict={}
    name = input("Student Name : ")
    no = int(input("Enrollment No. : "))
    spi = float(input("SPI : "))
    dict["Name"] = name
    dict["Enrollment_no"] = no
    dict["SPI"] = spi
    dic.append(dict)

def sort_spi(spi_list):
    # for i in spi_list:
        # spi_list[i]["SPI"].sort()
    #     i["SPI"].sort()
    # return(spi_list)
    print(sorted(spi_list,key = lambda i:i["SPI"]))
            
if __name__ == "__main__":
    main()
