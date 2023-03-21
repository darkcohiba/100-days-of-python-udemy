from art import *

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h","i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q","r","s","t","u","v","w","x","y","z"]
print(welcome)
print(title)
go = True
while go:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n")
    text = input("Type your message: \n")
    shift = int(input("Type your shift number: \n"))
    def caesar(shift, text, direction):
        message = ""
        if direction == "encode":
            for x in range(len(text)):
                if text[x].isalpha():
                    letter = text[x]
                    idx = alphabet.index(letter)
                    message += alphabet[idx + shift]
                else:
                    message += text[x]
            print(f"The encoded text is {message}.")
        elif direction == 'decode':
            for x in range(len(text)):
                if text[x].isalpha():
                    letter = text[x]
                    idx = alphabet.index(letter)
                    message += alphabet[idx - shift]
                else:
                    message += text[x]
            print(f"The decoded text is {message}.")
        else: 
            print("Please choose a viable direction")
    caesar(shift, text, direction)
    choice = input("Would you like to encode/decode again? (y/n): ")
    if choice == "n":
        print("Goodbye!")
        go = False


# def encrypt(shift, text):
#     # for i in range(len(alphabet)):
#     #     print(alphabet[i])
#     #     pass
#     message = ""
#     for x in range(len(text)):
#         letter = text[x]
#         idx = alphabet.index(letter)
#         message += alphabet[idx + shift]
#     # started with message as an array so the below line made it back into a string.
#     # message = "".join(message)
#     print(f"The encoded text is {message}.")

# def decrpyt(shift, text):
#     message = ""
#     for x in range(len(text)):
#         letter = text[x]
#         idx = alphabet.index(letter)
#         message += alphabet[idx - shift]
#     # below line made it back into a string
#     # message = "".join(message)
#     print(f"The decoded text is {message}.")


# if direction == "encode":
#     text = input("Type your message: \n")
#     shift = int(input("Type your shift number: \n"))
#     encrypt(shift, text)
# elif direction == "decode":
#     text = input("Type your message: \n")
#     shift = int(input("Type your shift number: \n"))
#     decrpyt(shift, text)
# else:
#     print("Please choose encode or decode direction.")

# solution from course

# def ceasar_two(start_text, shift, direction):
#     end_text = ""
#     if direction == "decode":
#         shift *= -1
#     for char in start_text:
#         # if char.isalpha():
#             # or 
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = position + shift
#             end_text = alphabet[new_position]
#         else:
#             end_text += char
