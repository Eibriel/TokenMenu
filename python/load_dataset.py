# Import and download stopwords from NLTK.
from nltk.corpus import stopwords
from nltk import download
import gensim.downloader as api


# download('stopwords')  # Download stopwords list.
stop_words = stopwords.words('english')
model = api.load('word2vec-google-news-300')


def preprocess(sentence):
    return [w for w in sentence.lower().split() if w not in stop_words]


sentence_obama = 'Obama speaks to the media in Illinois'
sentence_president = 'The president greets the press in Chicago'

sentence_obama = preprocess(sentence_obama)
sentence_president = preprocess(sentence_president)

print("calculating")
distance = model.wmdistance(sentence_obama, sentence_president)
print('distance = %.4f' % distance)
