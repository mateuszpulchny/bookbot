def get_num_words(text_from_book):
    num_words = len(text_from_book.split())
    print(f"{num_words} words found in the document")



def count_characters(text_from_book):
    chars = {}
    for c in text_from_book:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
