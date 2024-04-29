def sort_on(d):
    return d["count"]

def create_list_of_dicts(letters_dict: dict[str, int]) -> list[dict[str, int]]:
    list_of_dicts = []
    for name, val in letters_dict.items():
        list_of_dicts.append({'letter': name, 'count': val})
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
    print(f"{count_words(txt)} words found in the document\n")
    letters = create_list_of_dicts(count_letters(txt))
    letters.sort(reverse=True, key=sort_on)
    for letter_dict in letters:
        letter_val = letter_dict['count']
        letter_name = letter_dict['letter']
        print(f"The '{letter_name}' character was found {letter_val} times")
    print("--- End report ---")
def main():
    content = ""
    with open('books/frankenstein.txt', encoding='utf-8') as f:
        content = f.read()
    create_report(content)

if __name__ == '__main__':
    main()
