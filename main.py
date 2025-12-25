from stats import num_words, num_characters, num_characters_sorted
import sys

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    print(len(sys.argv))
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book at path: {book_path}...")
    print("----------- Word Count ----------")
    num_words_temp = num_words(book_text)
    char_dict = num_characters_sorted(book_text)
    print(f"Found {num_words_temp} total words")
    print("--------- Character Count -------")
    for char, count in char_dict.items():
        print(f"{char}: {count}")

    print("============= END ===============")
main()