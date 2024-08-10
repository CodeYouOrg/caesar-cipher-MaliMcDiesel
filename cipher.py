# add your code here
def mycaesar_cipher(text, shift):
    result = ""
    for i in text:
        if i.isalpha():
            starting_letter = ord('A') if i.isupper() else ord('a')
            caesar_shift = (ord(i) - starting_letter - shift) % 26
            encripted_text = chr(starting_letter + caesar_shift)       
            result += encripted_text
        else:
            result += i
    return result


entered_message = input("Enter your message: ")
encrypted_message = mycaesar_cipher(entered_message, 5)
print("The encrypted sentence:", encrypted_message)