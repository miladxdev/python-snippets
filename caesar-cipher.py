# Caesar Cipher
# to decrypt use -shift

def encrypt(text, shift):
    cypher = ''
    for i in text:
        if i.isalpha():
            cypher += chr((ord(i.lower()) + shift - 97) % 26 + 97)
        else:
            cypher += chr(ord(i)+shift)
    print('Encrypted:', cypher, '\n')


message = input('Message: ')
shift = int(input('Shift: '))
encrypt(message, shift)
