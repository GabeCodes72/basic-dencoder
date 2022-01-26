import base64
import string
def salad():
    shift = -3
    alphabet = string.ascii_letters
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)

    encoded = prompt.translate(table)
    print(encoded)
en_or_de = input("Do you want to encode or decode?")
if en_or_de == "encode":
    prompt = input("Type your message -> ")
    print("Ciphers: Caesar, Base")
    cipher = input("What type of cipher do you want? -> ")
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
elif en_or_de == "decode":
    def un_base():
        formatcc = input("Does it have numbers?")
        if formatcc == "no":
            print("Caesar Cipher")
            shift = 3
            alphabet = string.ascii_letters
            shifted = alphabet[shift:] + alphabet[:shift]
            table = str.maketrans(alphabet, shifted)
            encoded = prompt.translate(table)
            print(encoded)
        format64 = input("Does it have lowercase letters?")
        if format64 == "yes":
            print("Base64")
            decode64 = base64.b64decode(prompt)
            print(decode64)
            input("Hit enter to exit.")
            exit()
        elif format64 == "no":
            format32 = input("Are there equals signs at the end?")
            if format32 == "yes":
                print("Base32")
                decode32 = base64.b32decode(prompt)
                print(decode32)
                input("Hit enter to exit.")
                exit()
            elif format32 == "no":
                format16 = print("Is it just a mess of ALL CAPS and numbers?")
                if format16 == "yes":
                    print("Base16")
                    decode16 = base64.b16decode(prompt)
                    print(decode16)
                    input("Hit enter to exit.")
                    exit()
                elif format16 == "no":
                    print("This isn't anything. Just a mess of letters and numbers.")
                    input("Hit enter to exit.")
                    exit()
    un_base()
