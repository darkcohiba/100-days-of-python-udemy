from sqlalchemy import Column

end_conversation = False

while not end_conversation:
    action = input("have you ever used outside CO before? type 1 for yes, 2 for no: ")
    if action == "1":
        name = input("what is your name?: " )
        print(f"Hello {name}, thank you for coming by! ")
        print('''
        1: add an hike
        2: view hikes
        3: view camping trips
        4: delete hikes
        ''')
    if action == "exit":
        end_conversation = True

print("thanks for camping with brandi, your hikes are safe!")

# user stories
# ask user for username
# if no username ask to login
# if username give menu options