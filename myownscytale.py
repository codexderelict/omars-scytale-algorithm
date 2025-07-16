def separate_words(string, width):
    entries = [string[i:i+width] for i in range(0, len(string), width)]
    return entries
def get_width():
    width = int(input("Enter width (number): "))
    return width
 # Declare this inside the function, fuckface.
def scytale(entries, width): 
    combined_string = ""
    for i in range(width):
        for entry in entries:
            if i < len(entry): 
                combined_string += entry[i]
            else:
                combined_string += " "
    return combined_string
def main():
    original_text = input("Text to encrypt: ").upper().strip() 
    width = get_width()
    entries = separate_words(original_text, width)
    encrypted_text = scytale(entries, width)
    print(encrypted_text)
main()
