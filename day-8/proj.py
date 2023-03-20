alphabet = ["a", "b", "c", "d", "e", "f", "g", "h","i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q","r","s","t","u","v","w","x","y","z"]

direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n")
def encrypt(shift, text):
    # for i in range(len(alphabet)):
    #     print(alphabet[i])
    #     pass
    message = ""
    for x in range(len(text)):
        letter = text[x]
        idx = alphabet.index(letter)
        message += alphabet[idx + shift]
    # started with message as an array so the below line made it back into a string.
    # message = "".join(message)
    print(f"The encoded text is {message}.")

def decrpyt(shift, text):
    message = ""
    for x in range(len(text)):
        letter = text[x]
        idx = alphabet.index(letter)
        message += alphabet[idx - shift]
    # below line made it back into a string
    # message = "".join(message)
    print(f"The decoded text is {message}.")


if direction == "encode":
    text = input("Type your message: \n")
    shift = int(input("Type your shift number: \n"))
    encrypt(shift, text)
elif direction == "decode":
    text = input("Type your message: \n")
    shift = int(input("Type your shift number: \n"))
    decrpyt(shift, text)
else:
    print("Please choose encode or decode direction.")
