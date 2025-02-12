# Program to add two numbers

# Input: Ask the user for the first number
num1 = float(input("Enter the first number: "))

# Input: Ask the user for the second number
num2 = float(input("Enter the second number: "))

# Calculate the sum of the two numbers
sum = num1 + num2

# Output: Display the result
print("The sum of", num1, "and", num2, "is:", sum)
a =4
b =5
x =a+b
print(x)
price = 1000000
has_good_credit = True

if  has_good_credit:
    down_payment = 0.1 * price
else:down_payment =0.2 *price
print(f"down payment:{down_payment}")

ha_high_income = True
has_good_credit =True

if 'has_high_income'and has_good_credit:
    print("Eligible for loan")
   
    ha_high_credit = True
has_criminal_record =False

if 'has_high_credit'and not has_criminal_record:
    print("Eligible for loan")

    i = 1
while i <= 5:
    print(i)
    i = i + 1
print('Done')

kg = float(input("Enter weight in kg: "))
lbs = kg * 2.20462
print(f"{kg} kg is equal to {lbs} lbs")
number = 10

if number > 0:
    print("The number is positive")
elif number == 0:
    print("The number is zero")
else:
    print("The number is negative")



for i in range(5):
    print(f"Outer loop iteration {i}")
    for j in range(3):
        print(f"  Inner loop iteration {j}")
        if j == 2:
            print("    Condition met for the inner loop")
    print("End of outer loop\n")


    command = ""
while command != "quit":
    command = input(">").lower()
    if command == "start":
        print("Car started.")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop  - to stop the car
quit  - to exit
        """)

    else:
        print("I don't understand that command.")


        for item in ['john', 'jerry', 'sarah']:
        print (item)

              for item in range(5,10):
                print(item)

                price=[10,20,30]
                total =0
                for price in price:
                    total  += price
                    print (f"total :{total}")


secret_number = 25  # Fixed secret number for testing

guess = int(input("Guess the secret number: "))

if guess == secret_number:
    print("Correct! You guessed the secret number.")
else:
    print("Wrong guess. Try again!")

    
for i in range(1, 6):
    if i == 3:
        continue 
    if i == 5:
        break  
    print(i)

import array

# Create an integer array
numbers = array.array('i', [10, 20, 30, 40])

numbers.append(50)        
numbers.insert(1, 15)     
numbers.remove(30)       
popped = numbers.pop()    

print("Array:", numbers)
print("Popped element:", popped)


import array

arr = array.array('i', [1, 2, 4])
arr.insert(2, 3)  # Insert 3 at index 2
print("After Insert:", arr)


