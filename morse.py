#!/usr/bin/python3

import os

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.', ' ': ' ' 
        }


def encode():
    text = input(f"\nEnter text to encode into morse >: ")
    print(f"\n")
    for char in text:
        print(CODE[char.upper()], end="")
    print(f"\n")

def clean():
    path = input(f"\nEnter the path to a text file containing morse code >: ")
    clean = r"sed -r 's/ /\n/g' " + path + " > morse_lines.txt"
    os.system(clean)
    print(f"\n")

def decode():
    INV_CODE = {v: k for k, v in CODE.items()}
    f = open('morse_lines.txt')
    f_list = f.readlines()
    for line in f_list:
        line = line.rstrip()
        print(INV_CODE.get(line), end="")
    print("\n")    

def execute():
    option = input(f"\nType 'e' to encode text to morse or 'd' to decode morse to text >: ")
    if option == 'e':
        encode()
    else:
        clean()
        decode()

execute()
