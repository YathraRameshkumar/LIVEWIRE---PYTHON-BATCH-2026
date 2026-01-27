# PRINT HELLO WIRLD
print("hello world")

#ADD, SUBRACT, DIVIDE, SQUARE, FLOOR DIVISION, 
a = 5
b = 10
c = a+b
print(c)
c = a-b
print(c)
c = a*b
print(c)
c = a/b
print(c)
c = a%b
print(c)

c = a**0.5
print(c)
c = b**0.5
print(c)

#area of triangle[formula=0.5*base*height
a = float(input("Enter the base of the triangle="))
b = float(input("Enter the height of the triangle="))
c = 0.5*a*b
print("The area of the triangle is=" , c)

#quadratic equation[ (a+b)**2, (a-b)**2, a**2-b**2 ]

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("(a+b)^2 =", a**2+b**2+2*a*b)
print("(a-b)^2 =", )
print("a^2 - b^2 =", a**2 - b**2)

#swap two variables [ using third variable , without using third variable ]

#using third variable

a = int(input("Enter the first number="))
b = int(input("Enter the second number="))

c = x
x = y
y = c
print("After swapping using third variable", x,y) 

#without using third variable

a = int(input("Enter first number  :")) # 5
b = int(input("Enter second number :")) # 3

a,b = b , a

print ( a,b ) 


# using operators

a = int(input("Enter first number  :")) # 5
b = int(input("Enter second number :")) # 3

a=a+b
b=a-b
a=a-b

print(" Swapped number : " , a,b)

#program to miles[ 1 km = 0.63miles ]

a = int(input("Enter KILOMETER : "))
print(" Miles : " , a*0.63 ) 

#celsius to fahrenheit [ formula =(celsius * 1.8)+32 ]

a = int(input(" Enter CELSIUS :" ))
b = a*1.8+32
print(" FAHRENHEIT : " , b )

#find the lasst  digit of the number

a = int(input(" Enter a NUMBER :"))
print( "the last digit " , a%10)

# find last two digit of the number

a = int(input(" Enter a NUMBER :"))
print( "the last two digit " , a%100)

# take five digit number as input, square the middle digit and print number and the square

a = int(input(" Enter FIVE DIGIT NUMBER: ")) # 12345 - 3 and 9 
a=a//100
a=(a%10)
print(a)
a = a**2
print(a)












