a = "abcdefghigklmnopqrstuvwxyz"
ip = input("Enter sentence or string : ")
st = ip.lower()
not_contain = []
for letter in a:
    if letter not in st:
        not_contain.append(letter)
if(len(not_contain) != 0):
    print("This string is not Pangram.")
    print(f"Character Which are not in String : {not_contain}")
else:
    print("This string is Pangram.")