###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char.isalpha():
        if char.islower():  
            new_char_code = ord(char) + 1
            if new_char_code > ord('z'):
                new_char_code -= 26
        elif char.isupper():  
            new_char_code = ord(char) + 1
            if new_char_code > ord('Z'):
                new_char_code -= 26
        
        encrypted_char = chr(new_char_code)
        
        encrypted_text += encrypted_char
    else:
        encrypted_text += char

print("Plain text:", plain_text)
print("Encrypted text:", encrypted_text)
