def get_dicts():
    with open("base_dictionary", "r") as dic1, open("advanced_dictionary", "r") as dic2:
        src = dic1.readlines() + dic2.readlines()
        dictionary = {}

        for i in src:
            if len(i.split(' = ')) == 2:
                dictionary.update({i.split(' = ')[0]: i.split(' = ')[1]})
            else:
                i = i.split("\n")[0]
                print(f"Syntax error on the line '{i}' in the source dictionaries")
        # print(f"\nThe dictionary is :\n{dictionary}")
        return dictionary


def translate():
    dictionary = get_dicts()
    entry = input("Enter a french word to be translated in the 'Taki' language :\n\t==>\t")
    if entry in dictionary.keys():
        print(f"OK! The traduction of '{entry}' in the 'Taki' language is :\n\t-->\t{dictionary[entry]}")
    else:
        print(
            f"Oops!... We couldn't find '{entry}' in our dictionary!\n"
            "\t-->\tAre you sure you wrote it fine?\n"
            "\t-->\tMaybe this word doesn't exist yet... It's time to create it!\n"
              )


def new_word():
    creating = True
    dictionary = get_dicts()
    meaning_entry = input(
        "Enter the meaning of the new word by giving several nouns already registered in the dictionary separated "
        "by a space ('noun1 noun2 noun3'):\n\t==>\t"
                          )
    french_entry = input("Enter the french translation of the new word\n\t==>\t")
    words = meaning_entry.split(' ')
    taki_words = []
    for word in words:
        if creating:
            if word in dictionary.keys():
                taki_words.append(dictionary[word].split('\n')[0])
            else:
                print(f"Sorry, the word '{word}' does not exist in the dictionary")
                creating = False

    new_taki_word = ""
    if creating:
        new_taki_word = "".join('-' + i for i in taki_words)
        new_taki_word = new_taki_word.split('-', 1)[1]
        print(f"Wow! You just created the word '{new_taki_word}', which means'{french_entry}' in french!\n")
    else:
        print("Oops!... There have been an error... Try again!")
    with open("advanced_dictionary", "a") as dic:
        dic.writelines(french_entry + " = " + new_taki_word + '\n')


def run():
    print("Welcome on our next-gen 'Taki' dictionnary!")
    while True:
        print("Do you want to : \n"
              "\t-->\t 1/ Translate a word from french\n"
              "\t-->\t 2/ Create a new word\n")
        entry = input("Your choice ('1' or '2') :")
        if entry == '1':
            translate()
        elif entry == '2':
            new_word()
        else:
            print("You can only write '1', or '2'...\nTry again!")


run()
