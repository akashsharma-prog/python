#a = 1               # starting value
#while a < 11:       # loop until a is 10
    #print(a)
    #a = a + 1       # increase a by 1
 # question 2
#a = 10
#while a>0:
   # print(a)
    #a = a-1#
    #question 3
#a = int(input("What number you want to reverse: "))

#while a > 0:
    #print(a % 10)     # print last digit
    #a = a // 10       # remove last digit
#question 2
#count = 1
#num = 2

#while count<=10:
   # print(num)
    #count = count+1
    #num = num+2
    

    # question 3
#count =1
#num = 1 
#while count<= 10:
      #  print(num)
       # count = count +1 
        #num = num+2
# question 4
#a = 1
#while a<=5:
        #print("Akash sharma")
        #a = a+1

# question 5
#a = int(input("please give me a number"))
#b = 1
#while b<=10:
       # print(f"{a}*{b}*{a*b}")
       # b = b+1

        # question 6
#a = int(input("Please give me a number for sum: "))
#sum = 0
#b = 1
#while b <= a:
    #sum = sum + b
    #b = b + 1
#print("Sum is:", sum)
# question 7
#a = int(input("give me a number"))
#b = 2
#sum = 0
#while b<=a:
  #b = b+2
#sum = sum+b
#print(f"{a}number sum is {sum}")

# question 8 
#a = int(input("Please give me a number: "))
#count = 0

#while a > 0:
   ## a = a // 10    # remove last digit
   # count += 1     # increase digit counter

#print(f"Your number has {count} digits.")
#for loop question
#question no 1
for i in range(1,11,1):
      print(i)

#question 2
for i in range(0,21,2):
      print(i)
      #question 3
for i in range(1,21,2):
      print(i)  

#question4
a = int(input("tell me a number for print a table:-"))
for i in range(1,11,1):
      print(f"{a}*{i} = {a*i}")

# question 5
a = int(input("tell me your number:- "))
sum = 0
for i in range(1, a + 1):
    sum = sum + i
print(sum)
#question 6
a = int(input("tell me your even number:-"))
sum  = 0
for i in range(0,a+1,2):
      sum = sum+i
      print(sum)

     #question 7
     
a = int(input("tell me your odd number"))
sum = 0 

if a % 2 == 0:
    print(f"your num is not odd{a}")

for i in range(1, a+1, 2):
    sum = sum + i
else:
    for i in range(1, a+1, 2):
        sum = sum + i
    print(sum)
    # question 8
    a = int(input("give me a number"))
    if a%2==0:
         print("tis is even number")
    else:
         print ("this is odd numer")
