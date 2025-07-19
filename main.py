
import sys
from stats import number_of_words
from stats import number_of_characters
from stats import sort_list

args = sys.argv

if len(args) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    sort_list(args[1])
#sort_list()