def get_book_text(filepath):
    full_text = " "

    with open(filepath) as f:
        full_text = f.read()

    return full_text

def main():
    frankenstein = "/home/hovey/workspace/github.com/hovey/bookbot/books/frankenstein.txt"

    print(get_book_text(frankenstein))

main()