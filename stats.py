def get_book_text(filepath):
    full_text = " "

    with open(filepath) as f:
        full_text = f.read()

    return full_text

def number_of_words(filepath):
    text = get_book_text(filepath)
    words = text.split()
    num_words = 0

    for i in range(len(words)):
        num_words = num_words + 1


    return num_words

def number_of_characters(filepath):
    text = get_book_text(filepath).lower()
    char_dict = {}
    total_chars = [(text[i:i+1]) for i in range (0, len(text), 1)]

    for i in total_chars:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1

    return char_dict


def sort_on(items):
    return items["num"]

def sort_list(filepath):
    text = get_book_text(filepath).lower()
    char_dict = {}
    total_words = number_of_words(filepath)

    bookbot_intro = f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...\n"
    word_count = f"----------- Word Count ----------\nFound {total_words} total words\n"
    character_count = f"--------- Character Count -------\n"

    total_chars = [(text[i:i+1]) for i in range (0, len(text), 1)]

    for i in total_chars:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1

    

    
    print(bookbot_intro, word_count, character_count)

    char_counts = []

    for char in char_dict:
        char_temp = {"char": char, "num": char_dict[char]}
        char_counts.append(char_temp)
        

    
    char_counts.sort(reverse=True, key=sort_on)
        

    for i in range(len(char_counts)):
        if char_counts[i]["char"].isalpha():
            char = char_counts[i]["char"]
            num = int(char_counts[i]["num"])
            print(f"{char}: {num}")