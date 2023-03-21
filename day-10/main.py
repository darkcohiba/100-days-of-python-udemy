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

# lab 1
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


year = int(input("enter a year: "))
month = int(input("enter a month: "))
days = days_in_month(year, month)
print(days)