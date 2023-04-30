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

