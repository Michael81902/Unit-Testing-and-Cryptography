# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    newstr=""
    for let in text:
        rahhh=alpha.index(let)
        newstr+=codebet[rahhh]
    return newstr


def sub_decode(text, codebet):
    newest=""
    for let in text:
        index=cipher_alphabet.index(let)
        newest+=alpha[index]
    return newest




test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
