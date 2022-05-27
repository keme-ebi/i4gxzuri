# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from importlib.resources import contents


def read_file_content(filename):
    # [assignment] Add your code here
    with open("Reading-Text-Files\story.txt", "r") as filename:
        contents = filename.read()
        print(contents)
    return contents


def count_words():
    text = read_file_content("Reading-Text-Files\story.txt")
    # [assignment] Add your code here
    text = text.split(" ")
    dic = {}
    for word in text:
        if (len(word)) != 0:
            word = word.strip()
            word = word.strip("\n.,")
            if word in dic.keys():
                dic[word] += 1
            else:
                dic[word] = 1
    return dic


print(count_words())
