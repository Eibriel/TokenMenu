import json
import random as rd

with open("words.json", 'r') as fp:
    words = json.load(fp)

with open("sentences.json", 'r') as fp:
    sentences = json.load(fp)


def choose_words(n=5):
    return rd.sample(words, n)


def sample():
    tries = 0
    new_word = rd.choice(words)
    while new_word in selected_words or new_word in removed_words or new_word in word_list:
        new_word = rd.choice(words)
        tries += 1
        if tries > 500:
            raise Exception("Can't find a new word")
    return new_word


def select_sentence():
    if len(selected_words) == 0:
        return rd.choice(sentences)
    else:
        max_weight = 0
        current_sentence = sentences[0]
        for s in sentences:
            weight = 0
            for w in selected_words:
                if w in s[1]:
                    weight += 1
            for w in removed_words:
                if w in s[1]:
                    weight -= .5
            if weight > max_weight:
                max_weight = weight
                current_sentence = s
        return current_sentence


while 1:
    word_list = []
    selected_words = []
    removed_words = []
    sentence = rd.sample(sentences, 1)[0]
    word_list = choose_words()

    string = ""
    while 1:
        print("\n###")
        print(sentence[0])
        selected = select_sentence()
        print("\n> {}\n".format(selected[0]))
        text = "["
        for w in selected_words:
            text += "{},".format(w)
        text += "]"

        print(text)

        text = "["
        for w in removed_words:
            text += "{},".format(w)
        text += "]"

        print(text)

        id = 0
        for w in word_list:
            print(id, w)
            id += 1

        string = input()
        if string in ["q", ""]:
            break

        if string == "x":
            removed_words += word_list
            for n in range(len(word_list)):
                word_list[n] = sample()
        else:
            id = int(string[0])
            word = word_list[id]
            word_list[id] = sample()
            if len(string) > 1:
                removed_words.append(word)
            else:
                selected_words.append(word)
    if string == "":
        print("SELECTED: ", selected)
    elif string == "q":
        break
