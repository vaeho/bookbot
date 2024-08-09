def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    character_count = get_character_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    sort_charcount(character_count)
    print("--- End report ---")

def sort_charcount(char_count):
    chardict_list = []

    for char, count in char_count.items():
        chardict_list.append({'char': char, 'count': count})

    sorted_chardict_list = sorted(chardict_list, key=lambda x: x['count'], reverse=True)

    for chardict in sorted_chardict_list:
        if chardict["char"].isalpha():
            print(f"The '{chardict['char']}' character was found {chardict['count']} times")

def get_character_count(text):
    text_lower = text.lower()
    char_count = {}
    for char in text_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

main()
