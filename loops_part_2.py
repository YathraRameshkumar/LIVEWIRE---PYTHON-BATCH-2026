#16.Write a program to find the greatest common factor of given 2 integers. Input : 10 20 , Output : 10
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b :
    minimum = a
else :
    minimum = b

i = 1
count = 0

while i <= minimum :
    if a % i == 0 and b % i == 0:
        count += 1
    i+=1
print(minimum)

#17.Print the common factors of two positive integers n and m. Input : 8 12 , Output : 1 2 4

n = int(input("ENTER FIRST NUMBER : "))
m = int(input("ENTER SECOND NUMBER : "))

for i in range (1,(n+m)) :
    if n % i == 0 and m % i == 0:
        print(i)

#18.Write a program to get the Fibonacci series between 0 to 50.

num = int(input("ENTER A NUMBER : "))
a = 0
b = 1
print(a,end=" ")
print(b,end=" ")
for i in range(0,num+1,1):
    s = a+b
    if s >= num:
        break
    print(s,end=" ")
    a,b = b,s 


#a
#b b
#c c c
#d d d d
#e e e e e



for i in range (1,6,1):
    for j in range(1,i+1,1):
        print(chr(96+i), end =" ")
    print()



#a
#a b
#a b c
#a b c d
#a b c d e


for i in range (1,6,1):
    for j in range(1,i+1):
        print(chr(97+j), end=" ")
    print()

#* * * * * 
#*       * 
#*       * 
#*       * 
#* * * * *

for i in range(1,6,1):
    for j in range(1,6,1):
        if i==1 or i == 5 or j ==1 or j == 5 :
            print("*",end=" ")
        else:
            print(" ", end=" " )
    print()

# i1 = j1 , i2 = j2 , i3 = j3, i4 = j4, i5 = j5 and i + j = 6

#*      * 
# *   *   
#   *     
# *   *   
#*      * 


for i in range(1,6,1):
    for j in range(1,6,1):
        if i==j or i+j==6:
            print("*",end=" ")
        else:
            print(" ", end=" " )
    print()



for i in range(1,6,1):
    for j in range(1,6,1):
        if i==1 or i == 5 or j ==1 or j == 5 or i==j or i+j==6:
            print("*",end=" ")
        else:
            print(" ", end=" " )
    print() 


#Write a program to check whether the given number is palindrome or not. Palindrome is a number when reversed it gives the same number. Example 1: If the number is 121 Reverse is 121 Hence, 121 is a Palindrome Example 2: If the number is 438 Reverse is 834 Hence, 438 is not a Palindrome

n = int(input("ENTER A NUMBER : "))  
n1 = n                               
rev = 0
while n > 0:
    x = n % 10                       
    rev = (rev*10)+x                 
    n //= 10                         
if n1 == rev:
    print("PALINDROME")
else:
    print("NOT A PALINDRAME")

#Write a program to print if a number is an Armstrong number or not. 153 is an Armstrong number. 13+53+33 = 153.

n = int(input("ENTER A NUMBER :"))
n1 = n
n2 = n
digit = 0
while n > 0:
    n//=10
    digit+=1
s = 0
while n1>0 :
    m = n1%10
    s = s+(m**digit)
    n1//=10
if s == n2 :
    print("Armstrong number")

else:
    print("Not a armstrong number")

'''

#INPUT 20
#1 2 3 4 5 6 8 9 10 11 12 13 14 15 16 17 18 19 20

#OUTPUT
#EVEN : 2 4 6 8 10 12 14 16 18 20 = 110
#ODD  : 1 3 5 7 9 11 13 15 17 19  = 91
odd=0
even=0

n = int(input("ENTER A NUMBER : "))
for i in range (1,n+1,1):
    if i % 2 == 0:
        even+=i
    else:
        odd+=i
print("EVEN : " ,even)
print("ODD :" ,odd)

    


    



































    
