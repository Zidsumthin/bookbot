def get_book_text(filepath):
    full_text = " "

    with open(filepath) as f:
        full_text = f.read()

    return full_text

def number_of_words():
    text = get_book_text("/home/hovey/workspace/github.com/hovey/bookbot/books/frankenstein.txt")
    words = text.split()
    num_words = 0

    for i in range(len(words)):
        num_words = num_words + 1


    return num_words

def number_of_characters():
    text = get_book_text("/home/hovey/workspace/github.com/hovey/bookbot/books/frankenstein.txt").lower()
    char_dict = {}
    total_chars = [(text[i:i+1]) for i in range (0, len(text), 1)]

    for i in total_chars:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    
    return char_dict



    
    

