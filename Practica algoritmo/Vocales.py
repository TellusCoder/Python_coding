# Indicar al usuario que ingrese una palabra
user_word =input("ingrese una palabra: ")
user_word = user_word.upper()

# y asignarlo a la variable user_word.
for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    
    print(letter)
    

