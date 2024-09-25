import art 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def caesar(text, shift_amount, direction):
    result_text = ""

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = (position + shift_amount) % len(alphabet)
            elif direction == "decode":
                new_position = (position - shift_amount) % len(alphabet)
            new_letter = alphabet[new_position]
            result_text += new_letter
        else:
            result_text += letter
    print(f"The {direction}d text is: {result_text}")

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
