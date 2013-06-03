"""TRAIN ADVENTURES!"""
insult = "Your mother was a hamster and your father smelt of elderberries"
train_ride = "You board the train. You ride the train. You exit the train."
again = "Want to ride the train again?!?"

print("Hello and welcome to my game.")
trainQ = raw_input("Do you like trains?")
while trainQ.lower() != "yes" and trainQ.lower() != "no":
    print("Please answer either Yes or No.")
    trainQ = raw_input("Do you like trains?")
if trainQ.lower() == "yes":
    ride_train = raw_input("Would you like to ride the train?")
    if ride_train.lower() == "yes":
        print(train_ride)
        ride_again = raw_input(again)
        rides = 0
        while ride_again.lower() == "yes":
            print(train_ride)
            ride_again = raw_input(again)
            rides += 1
            if rides == 1:
                print("SWAG OVERLOAD!")
            if rides == 3:
                print("DO A BARREL ROLL!")
            if rides == 5:
                print("WHY ARE YOU STILL RIDING THE TRAIN?!")
        print(insult)
    else:
        print(insult)
elif trainQ.lower() == "no":
    print(insult)
print("Thanks for playing")

