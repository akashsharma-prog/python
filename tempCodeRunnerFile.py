leap = int(input("plz give your birt year"))
if (leap %4 == 0 and leap%400==0):
    print("this is leap year")
else:
    print("this is not leap year")