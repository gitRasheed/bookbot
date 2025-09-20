def get_word_count(text):
    words = text.split()
    len_words = len(words)
    return len_words


def get_char_count(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def sort_on_num(dict_item):
    return dict_item["num"]


def sorted_char_dictionary(char_dict):
    char_list = []
    for k, v in char_dict.items():
        if k.isalpha():
            char_list.append({"char": k, "num": v})

    char_list.sort(reverse=True, key=sort_on_num)
    return char_list


def print_sorted_char_dictionary(char_dict):
    for item in char_dict:
        print(f"{item['char']}: {item['num']}")
