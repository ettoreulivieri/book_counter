import argparse
from collections import Counter

parser = argparse.ArgumentParser(
                                prog = "letter_frequency",
                                description = "Reads the book and prints letter's frequency, Uppercase and lowercase are considered the same",
                                epilog = " this is all"
                                )

parser.add_argument("file", help = "the file to read")
args = parser.parse_args()

if not args.file.endswith(".txt"):
    print("Devi fornire un file .txt")
    exit()


with open(args.file, "r") as file:
    content = file.read()
    content = content.lower() 
    print (content)


for carattere in filter(str.isalpha, content):
    

    
    

