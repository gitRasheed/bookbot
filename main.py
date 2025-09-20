from stats import (
    get_word_count,
    get_char_count,
    sorted_char_dictionary,
    print_sorted_char_dictionary,
)
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at", path_to_book)
    print("----------- Word Count ----------")
    print("Found", get_word_count(get_book_text(path_to_book)), "total words")
    print("----------- Character Count ----------")
    print(
        print_sorted_char_dictionary(
            sorted_char_dictionary(get_char_count(get_book_text(path_to_book)))
        )
    )
    print("============= END ===============")


main()
