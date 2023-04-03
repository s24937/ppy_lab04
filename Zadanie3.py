

def caesar_cipher(message, key, alphabet="abcdefghijklmnoprstuwxyz"):
    message = message.lower()
    encoded = ""
    letters = ""
    for i in alphabet:
        letters = letters + i
    for j in message:
        if j in letters:
            index = letters.find(j)
            encoded = encoded + letters[(index + key) % len(alphabet)]
        else:
            encoded = encoded + j
    return encoded

print(caesar_cipher("The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll", 5))
