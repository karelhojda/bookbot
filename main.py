def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_num_words(text)
    letter_dict = {}

    for word in words:
        letters = get_letters(word)
        for letter in letters:
            if letter.isalpha():
                lowered_letter = letter.lower()
                letter_value = letter_dict.get(lowered_letter, 0)
                letter_dict.update({lowered_letter:letter_value + 1})

    sorted_dict = dict(sorted(letter_dict.items(), key=lambda item: item[1], reverse=True))

    print(f"--- Begin report of {book_path} ---")
    print(f"{len(words)} words found in the document\n")

    for letter in sorted_dict:
        # print(letter)
        print(f"The '{letter}' character was found {letter_dict[letter]} times")

    print(f"--- End report ---")

def get_num_words(text):
    words = text.split()
    return words


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_letters(word):
    letters = list(word)
    return letters


main()