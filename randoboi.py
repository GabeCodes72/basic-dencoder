import base64
prompt = input("Type your message -> ")
bp = int(input("Base 16, 32, or 64? (Type a number) -> "))
if bp == 16:
    encoded = base64.b16encode(str.encode(prompt))
elif bp == 32:
     encoded = base64.b32encode(str.encode(prompt))
elif bp == 64:
    encoded = base64.b64encode(str.encode(prompt))
print(encoded)