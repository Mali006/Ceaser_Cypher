def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Leave non-letter characters unchanged

    return result
message = "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the government for a redress of grievances."
shit = 3 
ceasar_encrpyt(message,shift)
