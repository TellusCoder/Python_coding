﻿word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
user_word = input ("ingrese una palabra: " )
# y asignarla a la variable user_word.
user_word = user_word.upper()

for letter in user_word:
   # Completa el cuerpo del bucle.
    if letter == "A" or letter == "E" or letter == "I" or letter== "O" or letter== "U":
        continue
    word_without_vowels += letter
# Imprimir la palabra asignada a word_without_vowels.
print (word_without_vowels)