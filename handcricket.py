import random

def game(batsman, bowler):
    throws=0
    while (throws<6):
        player1 = batsman.throw()
        player2 = bowler.throw()
        if player1==player2:
            print("{} throws {}, {} throws {}, {} is out".format(batsman.name, player1, bowler.name, player2, batsman.name))
            break
        else:
            batsman.runs(player1)
            print("{} throws {},{} throws {}, {}'s score is {}".format(batsman.name, player1, bowler.name, player2, batsman.name, batsman.score))
        throws+=1


class Player:
    def __init__(self, name, form):
        self.name = name
        self.form = form
        self.score=0

    def throw(self):
        if self.form=='NORMAL':
            return random.choice([0,1,2,3,4,6])
        elif self.form=='HITTER':
            return random.choice([4,6])
        else:
            return random.choice([0,1,2])
    
    def runs(self, score):
        self.score+=score


option1 = input("Who bats first?(A/B)?")
if option1=='A':
    option2='B'
else:
    option2='A'
form_p1 = input("What's {} form? ".format(option1))
form_p2 = input("What's {} form? ".format(option2))

player1 = Player(option1, form_p1)
player2 = Player(option2, form_p2)
rounds = 0
while rounds<2:
    game(player1,player2)
    player1,player2=player2,player1
    rounds+=1



if (player1.score>player2.score):
    print("Game winner is {}".format(player1.name))
else:
    print("Game winner is {}".format(player2.name))