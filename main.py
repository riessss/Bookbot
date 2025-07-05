import sys
from stats import count_words, count_characters, create_list_char


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    try:
        url = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(url)
    words = count_words(book)
    nr_of_char = count_characters(book)
    char_list = create_list_char(nr_of_char)
    char_list.sort(key=lambda entry: entry["num"], reverse=True)
    print(f'''
============ BOOKBOT ============
Analyzing book found at {url}...
----------- Word Count ----------
Found {len(words)} total words
--------- Character Count -------
      ''')
    for entry in char_list:
        if entry["char"].isalpha() == True:
            char = entry["char"]
            num = entry["num"]
            print(f"{char}: {num}")


main()