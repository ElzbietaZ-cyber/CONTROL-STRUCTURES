###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    encrypted_char = ord(char) + 1
    # add one to the character's code
    ...
    # replace new character code with its
    # corresponding character (use chr())
    encrypted_char = chr(encrypted_char)
    # add encrypted character to encrypted text
    encrypted_text = encrypted_text + encrypted_char

print(plain_text)
print(encrypted_text)