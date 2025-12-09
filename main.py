import sys
from stats import wordcount
from stats import count_chars
from stats import sorted_dict

def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
        return contents

def main():
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = get_book_text(path)
    counted_characters = count_chars(file)
    num_words = wordcount(file)
    sorted = sorted_dict(counted_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print(f"Found {num_words} total words")
    print("----------- Word Count ----------")
    for item in sorted:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha():
            print(f"{ch}: {count}")
        
    
   

main() 

 