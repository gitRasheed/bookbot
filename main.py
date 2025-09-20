from stats import (
    get_word_count,
    get_char_count,
    sorted_char_dictionary,
    print_sorted_char_dictionary,
)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(
        "Found", get_word_count(get_book_text("books/frankenstein.txt")), "total words"
    )
    print("----------- Character Count ----------")
    print(
        print_sorted_char_dictionary(
            sorted_char_dictionary(
                get_char_count(get_book_text("books/frankenstein.txt"))
            )
        )
    )
    print("============= END ===============")


main()
