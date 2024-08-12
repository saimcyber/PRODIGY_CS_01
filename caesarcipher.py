alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
#This are the alphabets for which we will find index vaalue and add or sub shift key from it for encryption and decryprion respectively
def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        position=alphabet.index(char)
        new_position=(position+shift_key)%26 #MOD 26 BECAUSE WE HAVE ONLY 26 CHARACTERS AND WANT TO STAY WITHIN RANGE
        cipher_text +=alphabet[new_position]
    print(f"Here is the text after encryption: {cipher_text}")
#HERE THE ENCRYPTION FUNCTION IS COMPLETED.

def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        position=alphabet.index(char)
        new_position=(position-shift_key)%26 #MOD 26 BECAUSE WE HAVE ONLY 26 CHARACTERS AND WANT TO STAY WITHIN RANGE
        plain_text +=alphabet[new_position]
    print(f"Here is the text after decryption: {plain_text}")
#DECRYPTION FINCTION FINALLY COMPLETED




what_to_do=input("type 'encrypt' for encryption and type 'decrypt' for decryption:\n")
text=input("Type your message:\n")
shift=int(input("Enter shift key:\n"))
if what_to_do=="encrypt":
    result=encryption(plain_text=text,shift_key=shift)
elif what_to_do=="decrypt":
    decryption(text,shift)