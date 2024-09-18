# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vig_encode(text, keyword):
  typeshi = (keyword * (len(text) // len(keyword) + 1))[:len(text)]
  str=""
  for i in range(len(text)):
    text_index=alpha.find(text[i])
    key_index=alpha.find(typeshi[i])
    real_index=(text_index+key_index)%26
    str+=alpha[real_index]
  return str



def vig_decode(text, keyword):
  rahhhh= (keyword * (len(text) // len(keyword) + 1))[:len(text)]
  str1=""
  for i in range(len(text)):
    text_index=alpha.index(text[i])
    key_index=alpha.index(rahhhh[i])
    real_index=(text_index-key_index)%26
    str1+=alpha[real_index]
  return str1


  return ""


test = "THEBRAVESSUCK"
vig_key = "WHIT"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!