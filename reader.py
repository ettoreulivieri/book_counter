import argparse
from collections import Counter
from time import perf_counter
import unicodedata

start = perf_counter()

parser = argparse.ArgumentParser(
                                prog = "letter_frequency",
                                description = "Reads the book and prints letter's frequency," \
                                " Uppercase and lowercase are considered the same," \
                                " numbers and punctuation are ignored and also accents are removed,"
                                " can print a histogram of the frequencies," \
                                " total number of words and lines in the file",
                                epilog = "Thank you for using this program!"
                                )

parser.add_argument("file", help = "the file to read")

parser.add_argument("letter", help = "the letter you want frequency of")

parser.add_argument("--hist", action="store_true", help="print a histogram of the letter frequencies")

parser.add_argument("--words", action="store_true", help="print the total number of words in the file")

parser.add_argument("--lines", action="store_true", help="print the total number of lines in the file")

args = parser.parse_args()

if not args.file.endswith(".txt"):
    print("you must provide a .txt file")
    exit()
if not args.letter.isalpha() or len(args.letter) != 1:
    print("you must provide a single letter!")
    exit()


with open(args.file, "r") as file:
    content = file.read().lower()



text = unicodedata.normalize("NFD", "".join(filter(str.isalpha, content)))

text_without_accents = "".join(c for c in text if unicodedata.category(c) != "Mn")

counter = Counter(text_without_accents)

total_letters = sum(counter.values()) # per usare len dovrei fare lista di filter

words = len(content.split())

lines = content.count("\n")

def frequency_calculator(x):
    return counter[x] / total_letters

print(frequency_calculator(args.letter.lower()))

end = perf_counter()


def print_histogram(freq):
    percentage = freq * 100
    freq = freq * 100
    freq = freq // 1
    return f"{'█' * int(freq)} {percentage:.2f}%"

if args.hist:
    for letter, count in counter.most_common():
        freq = frequency_calculator(letter)
        histogram = print_histogram(freq)
        print(f"{letter}: {histogram}")

if args.words:
    print(f"Total words: {words}")

if args.lines:
    print(f"Total lines: {lines}")


print(f"Execution time: {end - start:.4f} seconds")
#hello


