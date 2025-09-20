def get_word_count(text):
    words = text.split()
    len_words = len(words)
    print(f"{len_words} words found in the document")
    return len_words


def get_char_count(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars
