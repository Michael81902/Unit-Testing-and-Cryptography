# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    new_str=""
    for let  in text:
        if let.upper() in alpha:
            index=alpha.find(let.upper())
            new_str+=alpha[(index+n)%26]
        else:
            new_str+=let
    return new_str
def caesar_decode(text, n):
    new_str = ""
    for let in text:
        if let.upper() in alpha:
            index = alpha.find(let.upper())
            new_str += alpha[(index - n) % 26]
        else: new_str += let
    return new_str


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!

 