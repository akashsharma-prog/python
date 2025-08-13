#for loops
#a = range(1,20,1)
#for i  in a:
    #print(i)

#for i in range(2,17,2):
    #print(i)

#for a in range(16,0,-1):
   # print(a)
#for a  in range(-16,-2005,-1):
   # print(a)

    # table of 5
#for t in range(5,51,5):#
       #print(t)

#n = int(input("which table you want to print"))      
#for d in range(n,n*10+1,n):
       #print(d)
A="HELLOW MAFIYA MUNDE"    
print(len(A))
for i in range(len(A)):
       print(A[i])
#DIRECT METHOD
A = "Akash is very cool"

for i in A:print(i)


for i in range(1,21):
      if i ==15:
             continue
      print(i)


#loop question
a = int(input("please tell your number "))

for i in range(1,a+1,):
       print("hellow world")
       #question 2

a = int(input("tell me your number"))
for i in range(1,a+1):
       print(i)
  #question 3
#0
a = int(input("tell me your number"))
for i in range(a,0,-1):
       print(i)
#question 4

n = int(input("tell me your table"))
for i in range(1,5):
  print(f"{n}*{i}={n*i}")

#question 5 
n = int(input("please tell your number:-"))
sum = 0
for i in range(1,n+1):
      sum = sum +i
print(f"your sum is {sum}")

#question 6
n = int(input("Please tell your number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i  # multiply step by step

print(f"Your factorial is {fact}")
