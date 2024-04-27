def create_list_of_dicts(letters_dict: dict[str, int]) -> list[dict[str, int]]:
    list_of_dicts = []
    for name, val in letters_dict.items():
        list_of_dicts.append({f'{name}': val})
    return list_of_dicts

def count_letters(txt: str) -> dict[str, int]:
    txt_lower = txt.lower()
    letter_dict = {}
    for letter in txt_lower:
        if letter.isalpha():
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    return letter_dict

def count_words(txt: str) -> int:
    words = txt.split()
    return len(words)
def create_report(txt: str) -> None:
    print("--- Begin report of books/frankenstein.txt --- ")
    print(f"{count_words(txt)} words found in the document")
    letters = create_list_of_dicts(count_letters(txt))
    letters.sort(reverse=True, key=sort_on)
    for letter in letters:
        letter_val = letters[letter]
        print(f"The '{letter}' character was found {letter_val} times")

def main():
    content = ""
    with open('books/frankenstein.txt', encoding='utf-8') as f:
        content = f.read()
    create_report(content)

if __name__ == '__main__':
    main()
