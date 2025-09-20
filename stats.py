def get_word_count(text):
    words = text.split()
    len_words = len(words)
    print(f"{len_words} words found in the document")
    return len_words
