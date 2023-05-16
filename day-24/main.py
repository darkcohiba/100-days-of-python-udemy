# using files and writing to text files
# basic
# file = open("file.txt")
# contents = file.read()
# print(contents)
# file.close()


# best practice
# with open("file.txt") as file:
#     contents = file.read()
#     print(contents)


# replace text on file
# with open("file.txt", mode="w") as file:
#     file.write("help.")

# append text to the file
# with open("file.txt", mode="a") as file:
#     file.write("\nthird help.")


# write a new file
# with open("new_file.txt", mode="w") as file:
#     file.write("New File.")

# with open("../../../../Desktop/file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("./Input/Names/invited_guests.txt") as f:
    contents = f.readlines()

with open("./Input/Letters/starting_letter.txt") as f:
    old_letter = f.read()
    for name in contents:
        stripped_name = name.strip()
        new_letter = old_letter.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

# with open("./Input/Letters/starting_letter.txt") as f:
#     contents = f.read()
#     new_letter = contents.replace("[name]", "Sam")
#     print(new_letter)