def separate_words(string, width): # Separate the inputted sentence into substrings that are as wide as the scytale. 
    entries = [string[i:i+width] for i in range(0, len(string), width)]
    return entries
def get_width(): # Returns input of how wide the scytale should be. 
    while True: 
        try: # Exception made to make sure a number is inputted, not a string. It'll loop until a number is inputted. 
            width = int(input("Enter width (number): "))
            return width
        except ValueError:
            print("Give me a NUMBER.")

def scytale(entries, width): 
    combined_string = "" # This is where the encrypted text will go. 
    for i in range(width):
        for entry in entries: # I think of them as "entries" rather than "rows" as it is more intuitive to me personally. 
            if i < len(entry):
# Because the length of the inputted string may not divide fully into the width (leaving some remainder), this check is made to see if the substring's length matches the width (i.e. fills it)
                combined_string += entry[i]
            else:
                combined_string += " " # Whitespace if it doesn't in lieu of an IndexError
    return combined_string 
def main():
    original_text = input("Text to encrypt: ").upper().strip() 
    width = get_width() 
    entries = separate_words(original_text, width) 
    encrypted_text = scytale(entries, width) 
    print(encrypted_text)
main()
