from stats import get_num_words
from stats import count_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
       file_contents = f.read()
    return file_contents

def main():
    print(get_num_words(get_book_text("./books/frankenstein.txt")))
    print(count_characters(get_book_text("./books/frankenstein.txt")))
    print("Found 75767 total words")
    print("e: 44538")
    print("t: 29493")
     
main()