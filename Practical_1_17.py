def main():
    str1 = get_str()
    mkdic = make_dic(str1)
    print(mkdic)

def make_dic(st):
    dic = {}
    for character in st:
        dic[character] = st.index(character)+1
    return dic

def get_str():
    return (input("Enter String : "))

if __name__ == "__main__":
    main()