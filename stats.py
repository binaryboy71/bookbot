def num_words(book_text):
    num_words_local = len(book_text.split())
    return num_words_local

def num_characters(book_text):
    character_dict = {}
    for character_num in book_text:
        character = character_num.lower()
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def num_characters_sorted(book_text):
    character_dict = {}
    for character_num in book_text:
        character = character_num.lower()
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    sorted_char_dict = dict(sorted(character_dict.items(), key=lambda item: item[1], reverse=True))
    for key in list(sorted_char_dict.keys()):
        if key == " " or key == "\n" or not key.isalpha():
            del sorted_char_dict[key]
    return sorted_char_dict