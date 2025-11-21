def sort_on(d):
    return d["count"]


def create_list_of_dicts(letters_dict: dict[str, int]) -> list[dict[str, int]]:
    list_of_dicts = []
    for name, val in letters_dict.items():
        list_of_dicts.append({"letter": name, "count": val})
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
