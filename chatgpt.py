#a = input("what is your name ! And date of birth")
#print(a)
A = "akash sharma"
print(A)
print(ord("A"))

leap = int(input("plz give your birt year"))
if (leap %4 == 0 and leap%400==0) or(leap%100!=0):
    print("this is leap year")
else:
    print("this is not leap year")