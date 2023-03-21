def adding(num1, num2):
    result = num1 + num2
    return result

output = adding(2, 294)
# print (output)

def format_name(f_name, l_name):
    full_name = f_name.title() + ' ' + l_name.title()
    return full_name

# print(format_name("Sam", "WaTERS"))

def greeting(first, last):
    return (f"Hello, {format_name(first, last)}")

print(greeting("Sam", "waTERS"))

