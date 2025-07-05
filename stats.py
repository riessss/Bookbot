def count_words(book):
    words = book.split()
    return words

def count_characters(book):
    chars = list(book)
    count = {}
    for char in chars:
        if char.lower() not in count:
            count[char.lower()] = 1
        else:
            count[char.lower()] += 1
    return count

def create_list_char(char_dict):
    new_list = []
    for char in char_dict:
        new_input = {
            "char": char, "num": char_dict[char]
        }
        new_list.append(new_input) 
    return new_list