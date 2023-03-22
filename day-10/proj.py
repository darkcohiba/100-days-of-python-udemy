processes = [
    "+",
    "-",
    "/",
    "x"
]

def do_math(first_number, second_number, options):
    if options == "x":
        return (first_number * second_number)
    elif options == "+":
        return (first_number + second_number)
    elif options == "-":
        return (first_number - second_number)
    elif options == "/":
        return (first_number / second_number)
    else:
        return (first_number)



print("Welcome to the Calculator")
# first_number = int(input("What is your first number?: "))
# process = input(f"Choose a symbol from the options below: \n {processes} ")
# second_number = int(input("What is your second number?: "))
continue_math = True
result = 0
while continue_math:
    if result == 0:
        first_number = float(input("What is your first number?: "))
        second_number = float(input("What is your second number?: "))
        process = input(f"Choose a symbol from the options below: \n {processes} ")

        result = do_math(first_number, second_number, process)
        print(f"{first_number} {process} {second_number} = {result}")
        continue_question = input("Would you like to continue and use the result as the first number?: \n (yes/no): ")
        if continue_question == "no":
            continue_math = False
    else:
        second_number = float(input("What is your second number?: "))
        process = input(f"Choose a symbol from the options below: \n {processes} ")
        result = do_math(result, second_number, process)
        print(f"{first_number} {process} {second_number} = {result}")
        continue_question = ""
        if result == 0:
            continue_question = input("Would you like to continue and two new numbers?: \n (yes/no): ")
        else:
            continue_question = input("Would you like to continue and use the result as the first number?: \n (yes/no): ")
        if continue_question == "no":
            print("Thanks for using the calculator! Please come again!")
            continue_math = False
    