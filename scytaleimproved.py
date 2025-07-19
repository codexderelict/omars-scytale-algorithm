import math
def get_string():
        string = str(input("Enter string here (whitespaces will be removed and it will be capitalized) ")).upper().replace(" ","")
        return string
#The function above removes whitespaces and turns everything uppercase both for simplicity and realism to an actual scytale. 
def get_width(string):
    while True:
        try:
            width = int(input("Enter width here: "))
            if width > len(string): # If the number inputted is greater than the length of the string, the loop doesn't break. 
                print("Width is longer than the string. Please input a number smaller than the string.")
                continue
            return width
        except ValueError:
            print("Input a NUMBER, please.")
def get_length(string, width):
        length = math.ceil(len(string) / width)
        return length
# Divides the string by the width (because the width is all we have to go off of when decrypting) and if it doesn't divide fully, it rounds up. 
def get_grid(width, length):
    grid = [["" for _ in range(width)] for _ in range(length)]
    return grid
# Note to self: you don't need to create two empty grids for decryption and encryption. Multiplication is commutative so dimensions do not change.
# This initializes a width * length empty grid that will serve as the scytale. 
def write_encryption(string, grid, width, length):
    i = 0 
    for y in range(length):
        for x in range(width):
            grid[y][x] = string[i] if i < len(string) else " "
            i+=1
    return grid
# If the string doesn't divide fully, the remainder are padded with whitespaces. This function writes the string down row-wise (i.e. left to right with linebreaks)
def read_encryption(grid, width, length):
    combined_string = ""
    for x in range(width):
        for y in range(length):
            combined_string += grid[y][x] 
    return combined_string
# This function reads the grid when unraveled (i.e. top to bottom).
def write_decryption(string, grid, width, length):
    i = 0 
    for x in range(width):
        for y in range(length):
            grid[y][x] = string[i] if i < len(string) else " "
            i+=1
    return grid
def read_decryption(grid, width, length):
    combined_string = ""
    for y in range(length):
        for x in range(width):
            combined_string += grid[y][x]
    return combined_string
# These two do the opposite of the previous functions, so it writes top to bottom and reads left to right. 
def get_mode():
    while True:
        mode = str(input("Encrypt or decrypt? Input only the letter e for encryption and d for decryption.")).lower().strip()
        if mode == "e":
            return "encrypt"
        elif mode == "d":
            return "decrypt"
        else:
            print("Either one, e or d, nothing else.")
            continue 
# I chose just "e" and "d" for simplicity's sake, otherwise I'd have to make a list of acceptable inputs. 
def init_scytale(string):
    width = get_width(string)
    length = get_length(string, width)
    grid = get_grid(width, length)
    return width, length, grid
# This creates the width, length and empty grid. All that needs to be inputted is the width, and the length will be created based on it, and a grid based on both of them.
def encrypt(string, grid, width, length):
    grid = write_encryption(string, grid, width, length)
    result = read_encryption(grid, width, length)
    return result
# The grid is filled in with the letters and returned to the variable "grid", and then that grid is read as a string and returns to the variable "result"
def decrypt(string, grid, width, length):
    grid = write_decryption(string, grid, width, length)
    result = read_decryption(grid, width, length)
    return result
# Same exact thing, just inverted (see the write and read functions above)
def main():
    string = get_string() # The function returns and cleans up the string for processing. 
    width, length, grid = init_scytale(string) # This creates the variables.
    mode = get_mode() 
    if mode == "encrypt":
        result = encrypt(string, grid, width, length)
    elif mode == "decrypt":
        result = decrypt(string, grid, width, length)
    print(f"Original string: {string} \n Converted string: {result}")
if __name__ == "__main__":
    main()
