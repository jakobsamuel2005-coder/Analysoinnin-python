number1=2
number2=3
number3=5
name1="Jake"
name2="Sam"
name3="Alex"
if number1==number2:
    print("number1 is equal to number2")
if number1>number2:
    print("number1 is greater than number2")
if number1>=number2:
    print("number1 is greater than or equal to number2")
if number1!=number2:
    print("number1 is not equal to number2")
if number1==number2 and number1==number3 and number2==number3:
    print("All numbers are equal")
if number1==number2 or number2==number3:
    print("Number1 is equal to number2 or number2 is equal to number3")
if number1>number2 and number1>number3:
    print("number1 is the greatest")
if number1>number2:
    print("number1 is greater than number2")
else:
    print("number1 is not greater than number2")
if name1==name2:
    print("name1 is equal to name2")
if name1!=name2:
    print("name1 is not equal to name2")
if name1==name2:
    print("name1 is equal to name2")
else: 
    if name1==name3:
        print("name1 is equal to name3")
    else:
        print("name1 is not equal to name2 or name3")