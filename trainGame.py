from sys import exit

def start():
    print "Hello and welcome to my game."
    print "Do you like trains?"

    answer = raw_input("> ")

    if answer.lower() == "yes":
        train_ride()
    elif answer.lower() == "no":
        quit_game("Well fine then.")
    else:
        print "Please answer either Yes or No."
        start()

def quit_game(reason):
    print reason, "You died."
    exit(0)

def train_ride():
    print "Would you like to ride the train?"

    answer = raw_input("> ")
    if answer.lower() == "no":
        quit_game("Well fine then.")
    else:
        while answer.lower() == "yes":
            print "You board the train. It is a pleasent, relaxing ride."
            print "You exit the train. Would you like to ride again?"

            answer = raw_input("> ")
        print "You arrive at your destination."
        exit(0)


start()
