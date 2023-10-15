# handling exceptions
# try:
#     file = open("data.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["sadf"])
# except FileNotFoundError as e:
#     file = open("data.txt", "w")
#     file.write(f"Inside the exception!!... {e} ")
# except KeyError as key:
#     print(f'The key {key} does not exist')
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("Bad Type?")

# interactive challenge
#
# fruits = eval(input())
# # 🚨 Do not change the code above
#
# # TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#       fruit = fruits[index]
#     except IndexError as e:
#       print(f"Fruit pie")
#     else:
#       print(fruit + " pie")
#
#
# # 🚨 Do not change the code below
# make_pie(1)


# second interactive challenge

# eval() function will create a list of dictionaries using the input
# facebook_posts = eval(input())
#
# total_likes = 0
# # TODO: Catch the KeyError exception
# for post in facebook_posts:
#     try:
#       total_likes = total_likes + post['Likes']
#     except KeyError:
#       total_likes = total_likes + 0
# print(total_likes)