from datetime import date
td = date.today()
yy = 1950
mm = 12
dd = 18
bd = date(yy,mm,dd)
age = td.year-bd.year-((td.month,td.day) < (bd.month,bd.day))
print(age)