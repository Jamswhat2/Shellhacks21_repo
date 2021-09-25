import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer_ = PorterStemmer

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer_.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag w/ 0 for each word..
    bag = np.zeros(len(words), dtype=np.float32)
    for i, w in enumerate(words):
        if w in sentence_words:
            bag[i] = 1
    
    return bag