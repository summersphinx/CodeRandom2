import urllib3

http = urllib3.PoolManager()

def load_words(size):
    words = http.request('GET', 'https://gemgames.w3spaces.com/CodeRandom2/words_alpha.txt')
    words = eval(words.data)

    valid_words = []
    for word in words:
        if len(word) == size:
            valid_words.append(word)
    return valid_words
