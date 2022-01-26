import base64
import string
prompt = input("Type your message -> ")
print("Ciphers: Caesar, Base")
cipher = input("What type of cipher do you want? -> ")
def salad():
    shift = -3
    alphabet = string.ascii_letters
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)

    encoded = prompt.translate(table)
    print(encoded)
if cipher == "base":
    bp = int(input("Base 16, 32, or 64? (Type a number) -> "))
    if bp == 16:
        encoded = base64.b16encode(prompt.encode())
    elif bp == 32:
        encoded = base64.b32encode(prompt.encode())
    elif bp == 64:
        encoded = base64.b64encode(prompt.encode())
    elif bp == 85:
        encoded = base64.b85encode(prompt.encode())
    print(encoded)
elif cipher == "caesar":
    salad()