#stats
def get_text(file_path):
    with open(file_path) as text:
     content = text.read()
    return content

def get_words(file_path):
    full_text = get_text(file_path)
    words = full_text.split()
    words_num = len(words)
    return words_num

def get_char(file_path):
    context = get_text(file_path)
    char_dir={}
    for char in context.lower():
        char_dir[char]=char_dir.get(char,0)+1
    return char_dir
def get_sorted(file_path):
    char_list = get_char(file_path)
    sorted_list=sorted(char_list.items(),key=lambda item:item[1],reverse=True)
    return sorted_list