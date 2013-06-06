"""TRAIN ADVENTURES!"""
insult = "Your mother was a hamster and your father smelt of elderberries"
train_ride = "You board the train. The smell of urine overwhelms your poor, innocent nostrils. Vomit fights to arise from your stomach throughout the ride as you rock back and forth. The lights flicker on and off in an ominous pattern and as you arrive at your stop, you fear for your life."
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
            if rides == 0:
                print ("Thankfully, the train you boarded this time was very well maintained. You take a seat near the window and gaze lovingly outside at the entrancing sight of the city zipping by you. The silence of the train is calming as it takes you to your exit.")
                ride_again = raw_input(again)
                rides += 1
            if rides == 1:
                print ("SWAG OVERLOAD!")
                ride_again = raw_input(again)
                rides += 1
            if rides == 2:
                print ("DO A BARREL ROLL!")
                ride_again = raw_input(again)
                rides += 1
            if rides == 3:
                print ("WHY ARE YOU STILL RIDING THE TRAIN?!")
                ride_again = raw_input(again)
                rides += 1
        print("Well fine then. Fuck you too. Jerk.")
    else:
        print(insult)
elif trainQ.lower() == "no":
    print("Well fine then. Fuck you too. Jerk.")
print("Thanks for playing")

