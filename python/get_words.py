import csv
import json
from nltk.corpus import stopwords
from nltk import download
download('stopwords')  # Download stopwords list.
stop_words = stopwords.words('english')

words = []
sentences = []


def preprocess(sentence):
    if False:
        sentence = sentence.replace("?", "")
        sentence = sentence.replace("!", "")
        sentence = sentence.replace(",", "")
        sentence = sentence.replace(".", "")
        sentence = sentence.replace("\"", "")
        sentence = sentence.replace("-", "")
        sentence = sentence.replace("'", " ")
        return [w for w in sentence.lower().split() if w not in stop_words]
    return sentence.lower().split()


if False:
    with open('simpsons_dataset.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
else:
    reader = [
        ["", "who are you ?"],
        ["", "where are you from ?"],
        ["", "my name is anna"],
        ["", "what time is it ?"],

        ["", "hi how are you doing ?"],
        ["", "im fine how about yourself ?"],
        ["", "im pretty good thanks for asking"],
        ["", "no problem so how have you been ?"],
        ["", "ive been great what about you ?"],
        ["", "ive been good im in school right now"],
        ["", "what school do you go to ?"],
        ["", "i go to pcc"],
        ["", "do you like it there ?"],
        ["", "its okay its a really big campus"],
        ["", "good luck with school"],
        ["", "thank you very much"],
        ["", "im doing well how about you ?"],
        ["", "never better thanks"],
        ["", "it looks like it may rain soon"],
        ["", "yes and i hope that it does"],
        ["", "why is that ?"],
        ["", "i really love how rain clears the air"],
        ["", "me too it always smells so fresh after it rains"],
        ["", "yes but i love the night air after it rains"],
        ["", "really ? why is it ?"],
        ["", "because you can see the stars perfectly"],

    ]

for row in reader:
    s = preprocess(row[1])
    if len(s) > 3:
        sentences.append([row[1], s])
        words += s

words = list(set(words))

with open("words.json", 'w') as fp:
    json.dump(words, fp, sort_keys=True, indent=4)

with open("sentences.json", 'w') as fp:
    json.dump(sentences, fp, sort_keys=True, indent=4)
