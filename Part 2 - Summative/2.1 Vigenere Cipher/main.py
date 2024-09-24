# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#this function encodes a word, given a key which are the parameters. It will check to see if the character is in the alphabet, if it is not it skip pass the encoding
#process and go directly to the string. Otherwise it will be encoded adding the indexes from the key, and the word together and taking the corresponding letter in the alpahebet.
def vig_encode(text, keyword):
  typeshi = ""
  keyword_index = 0
  for   char in text:
    if char.upper() in alpha:
      typeshi += keyword[keyword_index % len(keyword)].upper()
      keyword_index += 1
    else:
      typeshi += char
  str=""
  text=text.upper()
  for i in range(len(text)):
    if text[i] in alpha:
      text_index=alpha.find(text[i])
      key_index=alpha.find(typeshi[i])
      real_index=(text_index+key_index)%26
      str+=alpha[real_index]
    else:
      str+=text[i]
  return str


#This function decodes what has already been encoded, which is the Enc variable, it checks to see if the character is in the Alphabet. If it is not, it will be directly
#added to the string, the rest will undergo the decoding process, which adds the indexes of the corresponding letter of the key, and finds the index gotten in the alphabet
# if needed it will use modolus to cycle back through..
def vig_decode(text, keyword):
  rahhhh = ""
  keyword_index = 0
  for char in text:
    if char.upper() in alpha:
      rahhhh += keyword[keyword_index % len(keyword)].upper()
      keyword_index += 1
    else:
      rahhhh += char
  str1=""
  text=text.upper()
  for char in range(len(text)):
    if text[char] in alpha:
      text_index=alpha.find(text[char])
      key_index=alpha.find(rahhhh[char])
      real_index=(text_index-key_index)%26
      str1+=alpha[real_index]
    else:
      str1+=text[char]
  return str1





test = "T HE  BR AV ES S U C K "
vig_key = "WHIT"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!