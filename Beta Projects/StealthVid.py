import os
import sys
import random
# @hidden_cell
def colorful_pattern_large():
    text = "STUBANX"
    colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m']
    reset_color = '\033[0m'
    
    # Define ASCII art for each letter
    ascii_art = {
        'S': [
            "  ____ ",
            " / ___|",
            "| |___ ",
            " \\___ |",
            "  ___||",
            " |____|"
        ],
        'T': [
            " _____ ",
            "|_   _|",
            "  | |  ",
            "  | |  ",
            "  | |  ",
            "  |_|  "
        ],
        'U': [
            " _   _ ",
            "| | | |",
            "| | | |",
            "| | | |",
            "| |_| |",
            " \\___/ "
        ],
        'B': [
            " ____  ",
            "|  _ \\ ",
            "| |_) |",
            "|  _ < ",
            "| |_) |",
            "|____/ "
        ],
        'A': [
            "     _     ",
            "    /\\     ",
            "   /..\\    ",
            "  /___ \\   ",
            " //   \\_\\ ",
            "//     \\_\\"
        ],
        'N': [
            " _   _ ",
            "| \\ | |",
            "|  \\| |",
            "| |\\  |",
            " | | \\ |",
            " |_|  \\|"
        ],
        'X': [
            " ",
            " X   X ",
            "  X X  ",
            "   X   ",
            "  X X  ",
            " X   X "
        ]
    }
    
    # Print each letter with color
    for row in range(6):  # 6 rows per letter
        for char in text:
            color = colors[text.index(char) % len(colors)]
            letter_art = ascii_art[char]
            print(f"{color}{letter_art[row]}{reset_color}", end='')
        print()  # Move to the next line after printing a row of letters

colorful_pattern_large()
print("\n           Stealth.Vid()")

task=int(input('''\n\n
                  ( 1 ) Encrypt a message
                  ( 2 ) Decrypt a message
                  ( 0 ) Close the program\n\n Enter response here:'''))

if task==1:
    code=int(input('''
                      ( 1 ) Create Security code manually
                      ( 2 ) Let the machine create it
                    \n\n Enter response here:'''))
    if code ==1:
        A=int(input("Enter an Eight digit Security code: "))
    if code ==2:
        A=random.randint(10000000,99999999)
    else:
        sys.exit(0)
    
    print(f"Your Eight digit Security code: {A}  \n(copy & save it.)")
    A=A%53
    A=(A*7)//11
    message=input('''To convert a file ask the admin for master code, message coversion is free.
                    Enter your message here: ''')
    message=message[::-1]
    words=message.split()
    new=[]
    print('Encryption process started...')
    for word in words:
        letters=[]
        print('processing...')
        for letter in word:
            letters.append(chr(ord(letter)-A)+chr(random.randint(40,120)))
            print('...')
        word="".join(letters)
        new.append(word)
        message=" ".join(new)
    print('process successfully done...')
    file=input('Enter filename here:')
    filename=file+'.txt'
    f=open(filename,'w')
    f.write(message)
    f.close()
    encrypted_filename=file+'Xstuban.mp4'
    os.rename(filename,encrypted_filename)
    print(f'Encrypted file is saved by name {encrypted_filename}')

elif task==2:
    filename=input('Enter the encrypted filename here:')
    os.rename(filename,'message4u.txt')
    f=open('message4u.txt','r')
    A=int(input("Enter Eight digit Security code:"))%53
    A=(A*7)//11
    message=f.read()
    words=message.split()
    new=[]
    print('Decryption process started...')
    for word in words:
        letters=[]
        print('processing...')
        for letter in range(0,len(word),2):
            letters.append(chr(ord(word[letter])+A))
            print('...')
        word="".join(letters)
        new.append(word)
    message=" ".join(new)
    message=message[::-1]
    print('process done')
    print('Decrypted message: ',message)
    f.close()
    os.rename('message4u.txt',filename)

elif task==0:
    print("Program closed.")
else:
    print('Invalid entry')