
#positive number or negative number
num1=int(input("enter a number: "))
if num1>0:
    print("positive number")
elif num1<0:
    print("negative number")
else:
    print("zero")


#even number or odd number

num1=int(input("enter a number: "))
if num1%2==0:
    print("even number")
else:
    print("odd number")

#eligible to vote

age=int(input("enter your age: "))
if age>18:
    print("your eligible to vote")
else:
    print("Not eligibe")



#two numbers greater number

num1=int(input("enter a first number: "))
num2=int(input("enter a second number"))
if num1>num2:
    print("greater number is ",num1)
else:
    print("greater number is ",num1)



#divisibe by 5

num=int(input("enter a number: "))
if num%5==0:
    print("divisible by 5")
else:
    print("Not divisible")



#multiple of 3

n=int(input("enter a number: "))
if n%3:
    print("multiple of 3")
else:
    print("Not multiple of 3")



#vowel or consonant

letter=input("enter a letter: ")
if letter in "aeiouAEIOU":
    print("vowel")
else:
    print("Not a vowel")

#number is greater than 100

letter=input("enter a letter: ")
if letter in "aeiouAEIOU":
    print("vowel")
else:
    print("Not a vowel")


#lep year or not
year=int(input("enter a year: "))
if year%4==0 and year%100!=0:
    print("leap year")
else:
    print("Not leap year")


#Take temperature input and print “Hot” or “Cold” based on value (>30 hot).

temp=int(input("enter temperature: "))
if temp>30:
    print("hot")
else:
    ("cold")


#Take marks and print grade: A (90+), B (75–89), C (50–74), Fail (<50).

marks=int(input("enter your marks: "))
if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=50:
    print("C")
else:
    print("D")


#Create a simple calculator using two numbers and an operator (+, -, *, /).

num1=int(input("enter a first number: "))
num2=int(input("enter a second number: "))
op=input("enter a operator (+,-,/,* )")
if op=="+":
    sum1=num1+num2
    print("sum",sum1)
elif op=="-":
    sub=num1-num2
    print("subtraction",sub)
elif op=="*":
    mult=num1*num2
    print("mutiplication",mult)
elif op=="/":
    div=num1/num2
    print("division",div)


#Take a number and print: “FizzBuzz” (divisible by 3 & 5), “Fizz” (only 3), “Buzz” (only 5), otherwise print number.

num=int(input("enter a number"))
if num%3==0 and num%5==0:
    print("FizzBuss")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buss")



#Check whether a character is uppercase, lowercase, digit, or special character.

character=input("enter a character: ")
if character.islower():
    print("lower case")
elif character.isupper():
    print("upper case")
elif character.isdigit():
    print("digit")
else:
    print("specail symbol")


#Take salary and assign tax percentage: No tax (<2.5L), 5% (2.5L–5L), 20% (5L–10L), 30% (>10L).

salary=int(input("enter your salary: "))
if salary<=250000:
    print("no tax")
elif salary<=500000:
    tax=salary-250000
    tax_to_pay=tax*5/100
    print("tax you have to pay",tax_to_pay)
elif salary<=1000000:
    tax=salary-250000
    tax_to_pay=tax*7/100
    print("tax you have to pay",tax_to_pay)
else:
    tax=salary-250000
    tax_to_pay=tax*10/100
    print("tax you have to pay",tax_to_pay)

    
#Find the largest of three numbers using nested if.

num1=int(input("enter a first number: "))
num2=int(input("enter a second number: "))
num3=int(input("enter a third number:"))
if num1>num2:
    if num1>num3:
        print(num1,"largest number")
if num2>num3:
    if num2>num1:
        print(num2,"largest number: ")
if num3>num1:
    if num3>num2:
        print(num3,"largest number")



#Take username and password and check login success or failure.

Username="pavankalyan"
Password="pavan123"
username=input("enter a username: ")
password=input("enter a password: ")
if username==Username:
    if password==Password:
        print("login successfull")
else:
    print("login failure")



#Check whether a number is positive; if yes, then check even or odd.

num=int(input("enter a number: "))
if num>0:
    print("number is positive")
    if num%2==0:
        print("even number")
    else:
        print("odd number")


#ATM withdrawal system: check balance, then withdrawal limit, then allow/deny transaction.

amount=34000
pin=9106
key1="check_balance"
key2="cash withdraw"
pin_number=int(input("enter your pin: "))
if pin_number==pin:
    check=input("if you want to check balance key of check balance or press not: ")
    if check==key1:
        print(amount)
    withdraw=input("if you want to withdraw than press cash_withdraw: ")
    if withdraw==key2:
        withdraw_amount=int(input("enter withdraw amount: "))
        if withdraw_amount<=amount:
            print("please collect your cash")
            print(f'avialable balance is {amount-withdraw_amount}')
            print("transaction successful")
        else:
            print("insufficient balance")
    else:
        print("please enter correct key2 correctly")
else:
    print("invalid pin")

    


#Check student result: If marks ≥ 35 → Pass; inside pass check Distinction (≥75) or First Class (≥60).

marks=int(input("enter your marks: "))
if marks>=35:
    print("pass")
    if marks>=75:
        print("Distinction")
    if marks>=60:
        print("First Class")


#Check whether a number is a 3-digit number or not.

num=int(input("enter a number: "))
if len(str(num))==3:
    print("three digit")


#Take three angles and check if they form a valid triangle.

angle1=int(input("enter a first angle: "))
angle2=int(input("enter a second angle: "))
angle3=int(input("enter third angle "))

if angle1+angle2+angle3==180:
    print("valid triangle")



#Find the second largest among three numbers.

num1=int(input("enter a first number: "))
num2=int(input("enter a second number: "))
num3=int(input("enter a second number: "))
list1=[num1,num2,num3]
print(list1)
list1.sort()
print(list1[-2])



#Check whether a character is an alphabet or not (without using built-in functions).
ch=input("enter a character: ")
ascii_value=ord(ch)
if (ascii_value>=65 and ascii_value<=90) or (ascii_value>=97 and ascii_value<=122):
    print("it is alphabet")
else:
    print("it is not alphabet")

    

#Calculate electricity bill based on units: First 100 free, next 100 ₹5/unit, above 200 ₹10/unit.
units=int(input("enter a units: "))
if units<=100:
    print("no current")
elif units>100 and units<=200:
    no_units=units-100
    amount=no_units*5
    print(amount)
else:
    amount=(units-100)*10
    print(amount)


#Movie ticket pricing based on age: Child (<12), Adult, Senior (>60).

age=int(input("enter your age: "))
ticket=150
if age<12:
    print(ticket/2)
elif age>12 and age <60:
    print(ticket)
else:
    print("free")



#Implement login system with maximum 3 attempts (use nested if).

user_name="pavan kalyan"
password="pavan@123"
User=input("enter a usrename: ")
passw=input("enter password: ")
if User==user_name:
    if passw==password:
        print("login successful")
    else:
        User=input("enter a usrename: ")
        passw=input("enter password: ")
        if User==user_name:
            if passw==password:
                print("login successful")
    
                

#Check whether a number is a palindrome
num=int(input("enter a number: "))
var=""
for i in str(num):
    var=str(i)+var
if num==int(var):
    print("palindrome")
else:
    print("not palindrome")


    


#Apply discount based on shopping amount: 5000 → 20%, >2000 → 10%, otherwise no discount.
purchase_amount=int(input("enter a amount: "))
if purchase_amount>5000:
    discount=purchase_amount*20/100
    print(discount,"discount amount")
elif purchase_amount>2000:
    discount=purchase_amount*10/100
    print(discount,"discount amount")
else:
    print("no discount")

#Traffic signal system: Red, Yellow, Green actions.
signal=input("enter a colur: ")
if signal=="red":
    print("stop")
elif signal=="yellow":
    print("start the vehicle")
elif signal=="green":
    print("move")


