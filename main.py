import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    
def anaylyze_book(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    book_str = get_book_text(path)
    num_words = get_num_words(book_str)
    char_counts = get_char_counts(book_str)
    sorted_char_counts = sort_char_counts(char_counts)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_char_counts:
        char = dict["char"]
        count = dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    anaylyze_book(path)

main()
