def main():
    with open("Practical_1_10.txt", encoding="utf-8") as file:
        count = 0
        pds_count = 0
        for row in file:
            count = count+1
            if(row.startswith("PDS")):
                pds_count = pds_count + 1
    print("Number of lines :",count)
    print("Number of lines which starts with 'PDS' :",pds_count)

if __name__ == "__main__":
    main()