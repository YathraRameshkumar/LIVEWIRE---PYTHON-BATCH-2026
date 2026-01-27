# SELECTION CONTROL
# Smallest number among two given integer

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
if a>b:
    print("b is smaller", b)
else:
    print("a is smaller" ,a)

# largest number among two given integers

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
if a>b:
    print("a is greater", a)
else:
    print("b is greater" ,b)

# absolute value of given integer

a = int(input("Enter a integer :"))
print(" The  absolute value of the given integer :" , abs(a))

# odd or even 

a = int(input("Enter a number :"))
if a%2 == 0:
    print( "EVEN" )
else:
    print( "ODD") 

#multiple of 5 or not.
a = int(input("Enter a number :"))
if a%5 == 0:
    print( "THE GIVEN NUBER IS MULTIPLE BY FIVE" )
else:
    print( "THE GIVEN NUMBER IS NOT MULTIPLE BY FIVE") 

#multiple of 10 or not.

a = int(input("Enter a number :"))
if a%10 == 0:
    print( "THE GIVEN NUBER IS MULTIPLE BY TEN" )
else:
    print( "THE GIVEN NUMBER IS NOT MULTIPLE BY TEN")

#two-digit number or not

a = int(input("Enter a number:"))
if a>=10 and a<=99:
    print("IT IS TWO DIGIT NUMBER:")
else:
    print("IT IS NOT TWO DIGIT NUMBER:")


#three-digit number or not.

a = int(input("Enter a number:"))
if a>=100 and a<=999:
    print("IT IS THREE DIGIT NUMBER:")
else:
    print("IT IS NOT THREE DIGIT NUMBER:") 

# NUMBER ENDS WITH ZERO OR NOT

a = int(input("Enter a number :"))
if a%10 == 0:
    print( "THE GIVEN NUBER IS ENDS WITH ZERO" )
else:
    print( "THE GIVEN NUMBER IS NOT ENDS WITH ZERO") 

#accept a number and check if its square is above 50 or below 50.

a = int(input("ENTER A NUMBER :"))
b = a**2
if b>50:
    print("THE SQUARE OF THE NUMBER IS ABOVE 50")
else:
    print("THE SQUARE OF THE NUMBER IS BELOW 50")
    
#absolute value

a = int(input("ENTER A NUMBER :"))

if a>=0:
    print(a)
else:
    print(-(a)) 

#to accept two numbers, subtract the two numbers and check if the difference (answer) is 0 or not

NUM1 = int(input("ENTER NUMBER 1 :"))
NUM2 = int(input("ENTER NUMBER 2 :"))

if NUM1-NUM2 == 0 :
    print("THE DIFFERENCE IS ZERO")
else:
    print("THE DIFFERENCE IS NOT ZERO")


#Write a program to compute the discount according to the given conditions for the purchase of laptop. to take the price of the laptop.to calculate the charge according to the following condition.
#Display the output as per the given format:
#Price of laptop : 
#Discount : 
#Total Price :

PRICE_OF_LAPTOP = int(input(" ENTER THE PRICE OF THE LAPTOP"))
if PRICE_OF_LAPTOP <50000:
    print("NO DISCOUNT")
elif PRICE_OF_LAPTOP >= 50001 and PRICE_OF_LAPTOP <= 100000:
    D=(PRICE_OF_LAPTOP//100)*10
    print("Discount 10% :",D )
    T=PRICE_OF_LAPTOP-D
    print("TOTAL PRICE :" ,T)
elif PRICE_OF_LAPTOP >= 100001 and PRICE_OF_LAPTOP <= 150000:
    D=(PRICE_OF_LAPTOP//100)*15
    print("Discount 15% :",D )
    T=PRICE_OF_LAPTOP-D
    print("TOTAL PRICE :" ,T)
else:
    D=(PRICE_OF_LAPTOP//100)*20
    print("Discount 20% :",D )
    T=PRICE_OF_LAPTOP-D
    print("TOTAL PRICE :" ,T)    

#To input weight of the parcel and type of booking (`O' for ordinary and 'E' for express).To compute and display the charges based on the weight of the parcel as per the tariff given 

weight = float(input("ENTER THE WEIGHT OF THE PARCEL : "))
booking = input("ENTER 'O' FOR ORDINARY AND 'E' FOR EXPRES BOOKING RESPECTIVELY : ")
                    
if booking == 'O' or booking == 'o':
    if weight <= 100:
        print(" PRICE FOR ORDINARY BOOKING = RS.80")
    elif weight >= 101 and weight <= 500:
        print(" PRICE FOR ORDINARY BOOKING = RS.150 ")
    elif weight >= 501 and weight <= 1000:
        print(" PRICE FOR ORDINARY BOOKING = RS.210 ")
    else:
        print(" PRICE FOR ORDINARY BOOKING = RS.250")


elif booking == 'E' or booking == 'e':
    if weight <= 100:
        print(" PRICE FOR EXPRESS BOOKING = RS.100")
    elif weight >= 101 and weight <= 500:
        print(" PRICE FOR EXPRESS BOOKING = RS.200 ")
    elif weight >= 501 and weight <= 1000:
        print(" PRICE FOR EXPRESS BOOKING = RS.250 ")
    else:
        print(" PRICE FOR EXPRESS BOOKING = RS.300")


    

    

  
