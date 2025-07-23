import math 
def process_string(string, width, length):
    string = string.upper().replace(" ","").ljust(width * length, "_")
    return string
def get_width(string):
    while True:
        try:
            width = int(input("Enter width here: "))
            if width > len(string):
                print("Width is longer than the string. Please input a number smaller than the string.")
                continue
            return width
        except ValueError:
            print("Input a NUMBER, please.")
def get_length(string, width):
        length = math.ceil(len(string) / width)
        return length

def get_grid(width, length):
    grid = [["" for _ in range(width)] for _ in range(length)]
    return grid
# Note to self: you don't need to create two grids for decryption and encryption. Multiplication is commutative so the string length doesn't really change.
def write_encryption(string, grid, width, length):
    i = 0 
    for y in range(length):
        for x in range(width):
            grid[y][x] = string[i] if i < len(string) else "*"
            i+=1
    return grid
def read_encryption(grid, width, length):
    combined_string = ""
    for x in range(width):
        for y in range(length):
            combined_string += grid[y][x] 
    return combined_string.rstrip("_")
def write_decryption(string, grid, width, length):
    i = 0 
    for x in range(width):
        for y in range(length):
            grid[y][x] = string[i] if i < len(string) else "*"
            i+=1
    return grid
def read_decryption(grid, width, length):
    combined_string = ""
    for y in range(length):
        for x in range(width):
            combined_string += grid[y][x]
    return combined_string.rstrip("_")
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

def init_scytale(string):
    width = get_width(string)
    length = get_length(string, width)
    grid = get_grid(width, length)
    string = process_string(string, width, length)
    return width, length, grid, string
def encrypt(string, grid, width, length):
    grid = write_encryption(string, grid, width, length)
    result = read_encryption(grid, width, length)
    return result
def decrypt(string, grid, width, length):
    grid = write_decryption(string, grid, width, length)
    result = read_decryption(grid, width, length)
    return result

def main():
    string = str(input("Enter string here: "))
    width, length, grid, string = init_scytale(string)
    mode = get_mode()
    if mode == "encrypt":
        result = encrypt(string, grid, width, length)
    elif mode == "decrypt":
            result = decrypt(string, grid, width, length)
    print(f"Original string: {string.rstrip("_")} \n Converted string: {result}")
if __name__ == "__main__":
    main()

