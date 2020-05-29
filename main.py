class Toad:
    def __init__(self, name):
        self.name = name
        self.coins = 0


class Game(Toad):
    def __init__(self, name):
        super().__init__(name)
        self.choiceMap = {
            'BE': {
                "a": "EHHHHH GET OFF MY FACE!!!! Fine!! take this all the coin I got and be gone!!!!",
                "b": "Good luck to you little one!! surely you wont't need it with that kind of confidence",
                "c": "Going back to your home huh?? I guess the exciting and scary wonders of adventure will have to wait until another day then.",
                "d": "Well what are you waiting for??? I'll give you a hint you can either exit to whatever is waiting to meet you outside or you can go back to your little cushy cozy borrow and continue life as normal. The choice is yours litle one.",
                }
            }

    def fork(self, decision, setting):
        choice = decision.lower().strip(' ')
        if choice in ['a', 'b', 'c', 'd']:
            print(self.choiceMap.get(setting).get(choice))
        else:
            print(f"{decision} is not valid input, choose a letter for each option above")


    def begin(self):
        print(f"Ahah, Now that's the spirit {self.name}! or at least it is a sign you are unbelievable bored and proabaly need to get a... well lets just hop in shall we?")
        print(f"Now I know you are just a small little toad and... well lets just say you haven't much experienced the world outside your small little burrow but todays the day little {self.name} gets to experience the wonder (or misery) of what the wrold has to offer hahahah.")
        print(f"Well then, what would you like to do little {self.name}??")
        print("\nTip: Enter the key associated with the action you want to perform\n")
        print("a: Hop onto mysterious mans face (I'm sure he'll love that)\nb: Exit the borrow a proud and valiant toad ready to begin his journey\nc: hop back down to the base of your borrow (the outside world is scarry)\nd: sit in place and wait for mr big dog to give you more advice")
        self.fork(input("\nDecision: "), 'BE')


def main():
    print("~~~~Welcome to Toad Quest~~~~")
    print("Ahh a new toad ehh? Don't see many of you folk around here so often. Whats your name laddy???")
    game = Game(input("Name: "))
    print(f"{game.name} eh?!?! don't sound like much of a toads name to me, but then again who am I to judge ehheehehe")
    print("ENTER y TO CONTINUE ANY OTHER KEY WILL EXIT (I would not judge if that intro is your decision to get out while you still can)")
    if input('Continue? ') == 'y':
        game.begin()
    return

main()