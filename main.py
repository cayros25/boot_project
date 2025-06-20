#main
import sys
from stats import get_text, get_words , get_char , get_sorted

def main(file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_words(file_path)} total words")
    print("--------- Character Count -------")
    sort_get=get_sorted(file_path)
    for char,count in sort_get:
        print(f"{char}: {count}")
    print("============= END ===============")
if __name__=="__main__":
    if len(sys.argv)<2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)

    file_path=sys.argv[1]
    main(file_path)








