


alphabet = {}
alphabet_str = "abcdefghijklmnopqrstuvwxyz"
for i in range(0,len(alphabet_str)):
    alphabet[alphabet_str[i]] = str(i + 1)



    
def alphabet_position(text):
    position = ""
    first = True
    text = text.lower()
    for i in range(0,len(text)):
        if text[i] in alphabet:
            if first:
                position += alphabet[text[i]]
                first = False
            else:
                position += " " + alphabet[text[i]]
    return position




print("(%s)->(%s) " % ("######",alphabet_position("######")))
print("(%s)->(%s) " % ("The sunset sets at twelve o' clock.",alphabet_position("The sunset sets at twelve o' clock.")))

#print(alphabet)

