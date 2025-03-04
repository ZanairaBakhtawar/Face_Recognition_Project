def remove_substring(original_string, substring):
    return original_string.replace(substring, "")


line = "Hello, world!"
new_line = remove_substring(line, "world")
print(new_line) 



def replace_string(line, old, new):
    return line.replace(old, new)


line = "python for advanced!"
new_line = replace_string(line, "advanced", "beginners")
print(new_line) 


a = "HELLO PYTHON!"
print(a.replace("H", "J"))

a ="king edward"
print(a.replace("k","L"))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

year = int(input().strip())
print(is_leap(year))



 




