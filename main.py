import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    with open(book_path) as f:
        text = f.read()
    
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_list = chars_dict_to_sorted_list(chars_dict)

    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sorted_on(item):
    return item["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sorted_on)
    return sorted_list


main()