def c_words(words):
    words = words.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def c_letters(text):
    letters = {}
    for letter in text.lower():
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sort_on(dict):
    return dict["num"]

def dic_to_list(letter_dict):
    letter_list = []
    for letter in letter_dict:
        tmp_dict = {"name": letter, "num": letter_dict[letter]}
        letter_list.append(tmp_dict)
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list

def print_dict(dicts):
    for dict in dicts:
        print(f"The '{dict["name"]}' character was found {dict["num"]} times")

        

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{c_words(file_contents)} words found in the document")
        print()
        print_dict(dic_to_list(c_letters(file_contents)))
        print("--- End report ---")

main()
