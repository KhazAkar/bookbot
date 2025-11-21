import sys

from stats import count_letters, count_words, create_list_of_dicts, sort_on


def create_report(txt: str) -> None:
    print("--- Begin report of books/frankenstein.txt --- ")
    print(f"Found {count_words(txt)} total words\n")
    letters = create_list_of_dicts(count_letters(txt))
    letters.sort(reverse=True, key=sort_on)
    for letter_dict in letters:
        letter_val = letter_dict["count"]
        letter_name = letter_dict["letter"]
        print(f"{letter_name}: {letter_val}")
        # print(f"The '{letter_name}' character was found {letter_val} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main(path_to_file):
    content = get_book_text(path_to_file)
    create_report(content)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    main(path_to_file)
