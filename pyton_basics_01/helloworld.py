
import math
x = math.sqrt(25)
print(x) 


import math
x = math.pow(3,2)
print(x)


import math
num = 5
factorial = math.factorial(num)
print(f"Factorial of {num} is {factorial}")


import math 
x= math.pi
print(x)


add = lambda x, y: x + y
print(add(5, 3))  

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared) 

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  


students = [("Alice", 25), ("Bob", 22), ("Charlie", 23)]
sorted_students = sorted(students, key=lambda x: x[1])  
print(sorted_students)


