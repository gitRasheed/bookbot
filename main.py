def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    len_words = len(words)
    print(f"{len_words} words found in the document")
    return len_words


def main():
    print(get_book_text("books/frankenstein.txt"))
    print(get_word_count(get_book_text("books/frankenstein.txt")))


main()
