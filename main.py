from sys import argv, exit
from stats import count_characters, count_words, sort_stats

def get_book_text(path):
    with open(path) as f:
        return f.read()

def pretty_print(num_words, sorted_stats):
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f"Found {num_words} total words")
    print('----------- Character Count ----------')
    
    for stat in sorted_stats:
        char, count = stat.items()
        if char[1].isalpha():
            print(f"{char[1]}: {count[1]}")

    print('============= END ===============')


def main():
    if len(argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        exit(1)

    text = get_book_text(argv[1])
    num_words = count_words(text)
    characters = count_characters(text)
    sorted_stats = sort_stats(characters)

    pretty_print(num_words, sorted_stats)

main()