import urllib3
import getpass

http = urllib3.PoolManager()



def load_words(size):
    with open('C:/Users/{user}/Documents/GEM Games/CodeRandom2/words_alpha.txt'.format(user=getpass.getuser())) as word_file:
        words = set(word_file.read().split())

    valid_words = []
    for word in words:
        if len(word) == size:
            valid_words.append(word)
    return valid_words
