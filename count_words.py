import HashSet as hst
import os

def read_file(path, filename):
    lst = []
    with open(path+filename, "r", encoding="UTF-8") as file:
        for line in file:
            lst.append(line.strip())
    
    return lst



def main():
    path = os.getcwd()
    hash_set = hst.HashSet()
    hash_set.init()
    file_brian = "\\brian_13376_words.txt"
    file_news = "\\swe_news_14920022_words.txt"
    brian_words = read_file(path, file_brian)

    for word in brian_words:
        hash_set.add(word)

    # print(hash_set.to_string())
    print(f"Brian unique words: {hash_set.get_size()}")

if __name__ == "__main__":
    main()