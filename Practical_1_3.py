import datetime 
yy = int(input("Enter year :"))
mm = int(input("Enter month :"))
dd = int(input("Enter day :"))
dt = datetime.date(yy,mm,dd)
print("12 days...")
print(dt)
for i in range(12):
    dt = dt+datetime.timedelta(days = 10)
    print(f"{dt}")