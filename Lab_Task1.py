"""

"""
print("Hello")

for i in range (20):
    if i%3==0:
           print (i)
           if i % 5 == 0:
               print ("Bingo!")

           print ("_____")



print (123123123123123123123123123123123123+1)


print(0o10)

#Activity 1
#n= input("Enter a Number")
#if int(n)%2==0:
 #   print("Given number is Even ")
#else:
 #   print("Given number is Odd ")


#Activity 2
"""sum =0
s= input ("Enter a Integer Value.. ")

n= int(s)
while n!= 0:
    sum=sum+n
    s=input ("Enter an Integer value...")
    n = int(s)

print("Sum of given value is ",sum)

"""

#Activity 3
""""
isPrime = True
i=2
n= int (input("Enter a number "))
while i<n:
    remainder = n%i
    if remainder==0:
        isPrime=False
    break

else:
    i=i+1

if isPrime:
    print("Number is Prime")
else:
    print("Number is Not Prime ")
    """

#Activity 4
"""
sum = 0

i =0

while i<4:
    s = input("Enter a Number :")
    n = int (s)
    sum= sum+n
    i=i+1

print ("sum is ", sum)
"""


#Activity 5
"""
sum =0

i=1
while i<10:
    sum= sum+i
    i=i+1

print("Sum is", sum)

"""


#Activity 6

"""
name = input('What is your name? ')
print('Hello ' + name)
job = input('What is your job? ')
print('Your job is ' + job)
num = input('Give me a number? ')
print('You said: ' + str(num))

"""

#Activity 7
"""
import random
MINIMUM = 1
MAXIMUM = 9
NUMBER = random.randint(MINIMUM, MAXIMUM)
GUESS = None
ANOTHER = None
TRY = 0
RUNNING = True
print ("Alright...")
while RUNNING:
 GUESS = raw_input("What is your lucky number? ")
 if int(GUESS) < NUMBER:
     print ("Wrong, too low.")
 elif int (GUESS) > NUMBER:
      print ("Wrong, too high.")
 elif GUESS.lower() == "exit":
      print ("Better luck next time.")
 elif int(GUESS) == NUMBER:
      print ("Yes, that's the one, %s." % str(NUMBER))
 if TRY < 2:
      print ("Impressive, only %s tries." % str(TRY))
 elif TRY > 2 and TRY < 10:
     print ("Pretty good, %s tries." % str(TRY))
 else:
        print ("Bad, %s tries." % str(TRY))


RUNNING = False
TRY += 1


"""




#Lab Task 1
"""num = int(input("Enter a number "))
temp = num
revers=0
while temp>0:
    digit = temp%10
    revers= digit + revers*10
    temp= int(temp/10)
print("Reverse of",num,"is",revers)
"""

#Lab Task 1
#Build_in

"""num = (input("Enter a number "))
print("Your Enter Number ",num, "Reverse is  ",reversed(num) )

"""



#Lab_Task 2
"""
sum = 0

i =0

while i<4:
    s = input("Enter a Number :")
    n = int (s)
    if n%2==0:
     sum= sum+n
    i=i+1

print("sum of Even Number is  ", sum)


"""
#Lab Task 4
"""
n = int(input("Enter Your Marks between 1 to 100: "))

if (n>=91):
    print("You got Grade 'A' ")
elif n>=81 and n<91:
    print("You got Grade 'B' ")
elif n>=71 and n<81:
    print("You got Grade 'C' ")
elif n>=61 and n<71:
    print("You got Grade 'D' ")
elif n>=50 and n<61:
    print("You got Grade 'E' ")
else:
    print("Sorry! You are Fail ")

"""



#Lab Task 3
"""
n=int(input('how many terms to be displayed:'))
fibonacci=(0,1)
for i in range(2,n):
    fibonacci+=(fibonacci[i-2]+fibonacci[i-1],)
print(fibonacci)

"""
#Lab Task 5

num = int(input("Enter a Number: "))
fac = 1
for i in range(1, num + 1):
    fac = fac * i
print("factorial of ", num, " is ", fac)