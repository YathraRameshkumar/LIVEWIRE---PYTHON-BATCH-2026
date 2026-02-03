#print the first N natural numbers. Input : 10 , Output : 1 2 3 4 5 6 7 8 9 10

num = int(input("ENTER A NUMBER :"))
for i in range (1,num+1,1):
    print(i, end=" ") 

#print the first N even natural numbers. Input : 5 , Output 2 4 6 8 10

num = int(input("ENTER A NUMBER "))
for i in range (1,num+1,1):
    print(i*2, end=" ") 

#print the first N odd natural numbers. Input : 5 , Output : 1 3 5 7 9
#for loop

num = int(input("ENTER A NUMBER"))
for i in range (1,2*num,2):
    print(i)

#while loop

num = int(input(" ENTER A NUMBER : "))
i=1
count=0
while count<num:
    print(i)
    i=i+2
    count+=1

#Write a program to print first N multiples of 3. Input : 7 , Output : 3 6 9 12 15 18 21

num = int(input("ENTER A INPUT :"))
i = 3
count = 0
while count<num:
    print(i)
    i+=3
    count+=1

#Write a program to print first N multiples of 5. Input : 5 , Output : 5 10 15 20 25

num = int(input("ENTER A INPUT :"))
i = 5
count = 0
while count<num:
    print(i)
    i+=5
    count+=1 

#Write a program to print all the multiples of 2 till N. Input : 15 , Output : 2 4 6 8 10 12 14

num = int(input("ENTER THE INPUT :"))
for i in range (2,num+1,2):
    print(i) 

#Write a program to print all the numbers which are multiples of either 2 or 3 till N. Input : 15 , Output : 2 3 4 6 8 9 10 12 14 15

num = int(input("ENTER A INPUT :"))
for i in range (2,num+1):
    if i%2==0 or i%3==0 :
        print(i) 
  
#Write a program to print all the numbers which are multiples of either 2, 5 or 7 till N. Input : 15 , Output : 2 4 5 6 7 8 10 12 14 15

num = int(input("ENTER A INPUT :"))
for i in range (2,num+1):
    if i%2==0 or i%5==0 or i%7==0:
        print(i) 

#Write a program to print the first N multiples of either 3, 5 or 7.Input : 10 , Output : 3 5 6 7 9 10 12 14 15 18

num = int(input("ENTER A INPUT : "))
for i in range (3,num+1):
    if i%3==0 or i%5==0 or i%7==0 :
        print(i) 

#Find the sum of all digits in a positive integer. Input : 123456789 , Output : 45

num = int(input("ENTER A NUMBER :"))  #1234
count = 0         #EXECUTION
while num>0:      # 1234 > 0       #123> 0        #12>0       #1>0       #0>0
    m = num%10    # 1234%10= 4     #123%10 = 3    #12%10=2    #1%10=1    #EXIT LOOP
    count+=m      # 0+4=4          #4+3=7         #7+2=9      #9+1=10
    num//=10      #123             #12            #1          #0
print(count)

#Count the number of digits in a positive integer. Input : 123456789 , Output : 9

num = int(input("ENTER A NUMBER :"))
count = 0
while num>0:
    num//=10
    count+=1
print(count)

#Write a program to find factors of a given number. Input : 20 , Output : 1 2 4 5 10 20

num = int(input("ENTER A NUMBER TO FIND FACTORS"))
for i in range (1,num+1,1):
    if num%i == 0 :
        print(i) 

#Write a program to count factors of a given number. Input : 20 , Output : 6

num = int(input("ENTER A NUMBER :"))
i=1
count = 0
while i<num+1:
    if num%i == 0 :
        count+=1
    i+=1
print(count) 

#Write a program to find whether the given number is a prime number or not.I nput : 11 , Output : Yes

num = int(input("ENTER A NUMBER : "))
count = 0
for i in range (2,num):
    if num%i == 0:
        count+=1
if count == 0:
    print("PRIME NUMBER")
else :
    print("  NOT PRIME NUMBER ")

#Print all prime numbers from 2 up to and including 'n'. Input : 15 , Output : 2 3 5 7 11 13

n = int(input("ENTER A NUMBER :"))
for j in range (2,n+1,1):
    num = j
    count = 0
    for i in range (2,num):
        if num%i == 0:
            count+=1
    if count == 0:
        print(j)



        
    
    
    











































    

















