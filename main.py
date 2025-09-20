from stats import get_word_count, get_char_count


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    print(get_book_text("books/frankenstein.txt"))
    print(get_word_count(get_book_text("books/frankenstein.txt")))
    print(get_char_count(get_book_text("books/frankenstein.txt")))


main()
