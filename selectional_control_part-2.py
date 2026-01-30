#ASCII value of an upper case alphabet or not

ASCII_NO = int(input("ENTER A ASCII NUMBER : "))
ch = chr(ASCII_NO)
if ch>= 'A' and ch <= 'Z' :
    print("IT IS UPPERCASE ASCII NUMBER : ")
else:
    print("IT IS NOT UPPERCASE ASCII NUMBER : ")

#ASCII value of an lower case alphabet or not

ASCII_NO = int(input("ENTER A ASCII NUMBER : "))
ch = chr(ASCII_NO)
if ch>= 'a' and ch <= 'z' :
    print("IT IS LOWERCASE ASCII NUMBER : ")
else:
    print("IT IS NOT LOWERCASE ASCII NUMBER : ")

#accept two numbers, subtract the two numbers and check if the difference (answer) is 0 or not

num1 = int(input("ENTER A NUMBER 1 :"))
num2 = int(input("ENETER NUMBER 2 : "))
if num1 - num2 == 0 :
    print("THE DIFFERENCE IS ZERO :")
else:
    print("THE DIFFERENCE IS NOT ZERO :")

#to read the Computer Science marks of a student and print if the student has passed or failed. The student has passed if marks is 50 or above otherwise failed).

CS_Mark = int(input("ENTER THE COUMPUTER SCIENCE MARK :"))
if CS_Mark >= 50 :
    print("PASSED")
else:
    print("FAILED")

#accept a number and check if the number is divisible by 10.

number = int(input("ENTER A NUMBER"))
if number%10 == 0 :
    print(" THE NUMBER IS DIVISIBLE BY 10 ")
else:
    print(" THE NUMBER IS NOT DIVISIBLE BY 10")

#to take a two-digit number and print the biggest digit.

num = int(input("ENTER A TWO DIGIT NUMBER :"))
a = num//10
b = num%10
if a>b :
    print(a)
else:
    print(b) 

#accept the choice from the user. If the choice is 1 print “The exam will be easy”, otherwise print “The exam will be difficult”.

num = int(input("CHOOSE 1 IF THE EXAM WAS EASY :"))
if num == 1 :
    print(" THE EXAM WAS EASY ")
else:
    print(" THE EXAM WAS DIFFICULT ") 

#accept a value from the user. If the value entered is 1 then print “You can go out and play” otherwise “You cannot go out and play”

num = int(input("CHOOSE 1 IF YOU WANT TO PLAY OUTSIDE :"))
if num == 1 :
    print(" YOU CAN  GO OUT AND PLAY ")
else:
    print(" YOU CAN NOT GO OUT AND PLAY OUTSIDE ") 

#accept the length and breadth of a shape and print if they are the same. If they are the same, print it’s a square otherwise its rectangle

l = int(input(" ENTER LENGTH OF THE SHAPE :"))
b = int(input(" ENTER BREADTH OF THE SHAPE :"))
if l == b :
    print(" IT IS A SQUARE ")
else :
    print(" IT IS A RECTANGLE ") 

#given number is a multiple of both 5 and 3

num = int(input("ENTER A NUMBER "))
if num%5 == 0 and num%3 == 0 :
    print(" THE NUMBER IS DIVISIBLE BY 3 AND 5 ")
else :
    print("THE NUMBER IS not DIVISIBLE BY 3 AND 5") 
    
#given number is a three-digit number and also a multiple of 10.

num = int(input("ENTER A NUMBER "))
if num%100 == 0:
    print("IT IS A THREE DIGIT AND ALSO MULTIPLE OF 10")
else:
    print("IT IS NOT A THREE DIGIT AND ALSO MULTIPLE OF 10") 

#given number is a three-digit number and also a multiple of 2, 5, and 10


num = int(input("ENTER A NUMBER "))
if num%100 == 0 and num%2 == 0 and num%5 == 0 and num%10 == 0:
    print("IT IS A THREE DIGIT AND ALSO MULTIPLE OF 2,5,10")
else:
    print("IT IS NOT A THREE DIGIT AND ALSO MULTIPLE OF 2,5,10") 

#the given two integer inputs. If both numbers are even, find their product. Otherwise, find their sum.

num = int(input("ENTER A TWO DIGIT NUMBER :"))
a = num//10
b = num%10
if a%2 == 0 and b%2 ==0  :
    print("THE PRODUCT OF THE NUMBER IS :", a*b)
else:
    print("THE SUM OF THE NUMBER IS : ", a+b) 










     
