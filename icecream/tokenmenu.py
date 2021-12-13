import re
import sre_yield
import random as rd
from sentences import sentences

group_names = [
    "hello1",
    "request_order1",
    "request_type1",
    "request_size1",
    "request_topping1",
    "request_payment1",

    "chocolate1",
    "vanilla1",
    "raspberry1",
    "banana1",
    "chocolate2",
    "vanilla2",
    "raspberry2",
    "banana2",

    "he1",
    "she1",

    "cone1",
    "cup1",

    "yes1",
    "no1",

    "one_scoop1",
    "two_scoops1",

    "cash1",
    "credit1",

]


class token_menu:
    def __init__(self):

        self.words = [
            "hello",
            # "request_order",
            # "request_type",
            # "request_size",
            # "request_topping",
            # "request_payment",

            "chocolate",
            "vanilla",
            "raspberry",
            "banana",

            # "he",
            # "she",

            "cone",
            "cup",

            "yes",
            "no",

            "one_scoop",
            "two_scoops",

            "cash",
            "credit",

        ]

        self.sentences = sentences
        self.reset()
        self.restart()

    def reset(self):
        self.state_seller = {
            "say_hi": False,
            "talker": 0.5,
            "flavors": [],
            "type": None,
            "size": None,
            "topping": None,
            "payment": None
        }
        self.state_buyer = {
            "say_hi": False,
            "talker": 1,
            "flavors": ["chocolate", "vanilla"],
            "type": "cup",
            "size": "two_scoops",
            "topping": "no",
            "payment": "cash",

            "request": None
        }
        self.turn = "seller"

    def restart(self):
        self.word_list = []
        self.selected_words = []
        self.removed_words = []
        self.sentence = ""
        self.sentence_match = []
        self.word_list = self.choose_words()
        self.seller_question = ""

        self.build_question()

    def choose_words(self, n=6):
        return rd.sample(self.words, n)

    def sample(self):
        tries = 0
        new_word = rd.choice(self.words)
        # while new_word in self.selected_words or new_word in self.removed_words or new_word in self.word_list:
        while new_word in self.selected_words or new_word in self.word_list:
            new_word = rd.choice(self.words)
            tries += 1
            if tries > 500:
                raise Exception("Can't find a new word")
        return new_word

    def select_sentence(self):
        frame = []
        match = self.selected_words
        frame += match
        self.sentence = self.find_sentence("buyer", match, frame)
        return self.sentence

    def find_sentence(self, actor, match, frame):
        selected = []
        for s in self.sentences:
            if s["actor"] == actor:
                selected.append(s)

        for sent in selected:
            for sp in sre_yield.AllStrings(sent["regex"]):
                matches = re.search(sent["regex"], sp)
                expected_count = len(match)
                matched_count = 0
                unwanted_count = 0
                already_found = []
                for group in group_names:
                    try:
                        c = matches.group(group)
                    except IndexError:
                        continue
                    if not c:
                        continue
                    if group[:-1] in match and group[:-1] not in already_found:
                        matched_count += 1
                        already_found.append(group[:-1])
                    if group in group_names:  # frame:
                        unwanted_count += 1
                if matched_count == expected_count and unwanted_count == matched_count:
                    self.sentence_match = already_found
                    return sp
        return "None"

    def select_word(self, id):
        word = self.word_list[id]
        self.word_list[id] = self.sample()
        self.selected_words.append(word)

    def more_words(self):
        self.removed_words += self.word_list
        for n in range(len(self.word_list)):
            self.word_list[n] = self.sample()

    def execute_sentence(self):
        for token in self.sentence_match:
            if token in ["cone", "cup"]:
                self.state_seller["type"] = token
            elif token in ["one_scoop", "two_scoops"]:
                self.state_seller["size"] = token
            elif token in ["chocolate", "vanilla", "raspberry", "banana"]:
                self.state_seller["flavors"].append(token)
            elif token in ["cash", "credit"]:
                self.state_seller["payment"] = token
            elif token in ["no", "yes"]:
                if self.state_buyer["request"] == "topping":
                    self.state_seller["topping"] = token
        print(self.state_seller)

    def build_question(self):
        # Seller answer
        frame = []
        if not self.state_seller["say_hi"]:
            match = ["hello"]
            self.state_seller["say_hi"] = True
        else:
            if len(self.state_seller["flavors"]) == 0:
                match = ["request_order"]
                self.state_buyer["request"] = "order"
            elif not self.state_seller["type"]:
                match = ["request_type"]
                self.state_buyer["request"] = "type"
            elif not self.state_seller["size"]:
                match = ["request_size"]
                self.state_buyer["request"] = "size"
            elif not self.state_seller["topping"]:
                match = ["request_topping"]
                self.state_buyer["request"] = "topping"
            elif not self.state_seller["payment"]:
                match = ["request_payment"]
                self.state_buyer["request"] = "payment"
            else:
                self.seller_question = "Here is your icecream!"
                return
        frame += match

        self.seller_question = self.find_sentence("seller", match, frame)
