from tokenmenu import token_menu

tm = token_menu()

while 1:
    print("\n###")
    selected = [tm.select_sentence()]
    print("\n> {}\n".format(selected[0]))

    text = "["
    for w in tm.selected_words:
        text += "{},".format(w)
    text += "]"
    print(text)

    text = "["
    for w in tm.removed_words:
        text += "{},".format(w)
    text += "]"
    print(text)

    id = 0
    for w in tm.word_list:
        print(id, w)
        id += 1

    string = input()
    if string in ["q", ""]:
        break

    if string == "x":
        tm.more_words()
    else:
        id = int(string[0])
        tm.select_word(id)
