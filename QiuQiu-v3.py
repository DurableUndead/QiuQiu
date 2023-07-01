import random

class QiuQiu:
    player = []
    player_value_card = [[]]
    player_cards    = [[]]
    cards           = [0,1,2,3,4,5,6,7,8,9]

    condition_Ai_choice = 5

    default_per_cards = 2

    player_barter = []
    point = 0

    def __init__(self, player=6):
        self.num_of_players = player

    def start(self):
        self.config()
        self.gameplay()
        self.conditionAI()

    def config(self):
        self.point = 0
        self.player_cards    = [[]]
        self.player_value_card = [[]]
        self.cards           = [0,1,2,3,4,5,6,7,8,9] * 4

        self.player_cards *= self.num_of_players
        self.player_value_card *= self.num_of_players

        random.shuffle(self.cards)

        for i in range(self.num_of_players):
            self.player.append(i)

            self.player_cards[i] = self.cards[:self.default_per_cards]
            del self.cards[:self.default_per_cards]
            
    def gameplay(self):
        for i in range(self.num_of_players):
            total_card = self.player_cards[i][0] + self.player_cards[i][1]
            if total_card >= 10:
                total_card -= 10
            self.player_value_card[i] = [total_card]

        for i in range(self.num_of_players):
            self.player_cards[i].sort(reverse=False)
            print(f"Kartu Player#{i} : {self.player_cards[i]} = {(self.player_value_card[i])}")

    def conditionAI(self, point_barter = 0):
        self.point += point_barter
        if self.point == 2:
            print(self.point)
        # if self.num_of_players == 2:
        else:
            for i in range(self.num_of_players - 1):
                if self.player_value_card[i+1] < [self.condition_Ai_choice]:
                    #print(f'Player{i+1}: "Saya ingin barter Kartu saya"')
                    self.player_barter.append(self.player[i+1])

            if len(self.player_barter) > 1:
                print(f"Player yang ingin barter kartu : {self.player_barter}")
            
                self.barter()
            else:
                print(f"Player yang ingin barter kartu : {self.player_barter}")
        
    def barter(self):
        random.shuffle(self.player_barter)
        print(self.player_barter)
        if len(self.player_barter) % 2 == 0:
            print("kondisi 1")
            for i in range(int(len(self.player_barter) / 2)):
                min_card_player1 = min(self.player_cards[self.player_barter[0]])
                min_card_player2 = min(self.player_cards[self.player_barter[1]])

                self.player_cards[self.player_barter[0]].append(min_card_player2)
                self.player_cards[self.player_barter[1]].append(min_card_player1)

                self.player_cards[self.player_barter[0]].remove(min_card_player1)
                self.player_cards[self.player_barter[1]].remove(min_card_player2)

                for i in range(2):
                    del self.player_barter[0]
                

        else:            
            if len(self.player_barter) == 3:
                print("kondisi 2")
                min_card_player1 = min(self.player_cards[self.player_barter[0]])
                min_card_player2 = min(self.player_cards[self.player_barter[1]])
                min_card_player3 = min(self.player_cards[self.player_barter[2]])
                self.player_cards[self.player_barter[0]].append(min_card_player3)
                self.player_cards[self.player_barter[1]].append(min_card_player2)
                self.player_cards[self.player_barter[2]].append(min_card_player1)

                self.player_cards[self.player_barter[0]].remove(min_card_player1)
                self.player_cards[self.player_barter[1]].remove(min_card_player2)
                self.player_cards[self.player_barter[2]].remove(min_card_player3)

                del self.player_barter[:]
                    
            else:
                print("Kondisi 3")
                while True:
                    min_card_player1 = min(self.player_cards[self.player_barter[0]])
                    min_card_player2 = min(self.player_cards[self.player_barter[1]])

                    self.player_cards[self.player_barter[0]].append(min_card_player2)
                    self.player_cards[self.player_barter[1]].append(min_card_player1)

                    self.player_cards[self.player_barter[0]].remove(min_card_player1)
                    self.player_cards[self.player_barter[1]].remove(min_card_player2)
                    
                    for i in range(2):
                        del self.player_barter[0]
                    
                    if len(self.player_barter) == 3:
                        print("kondisi 4")
                        
                        min_card_player1 = min(self.player_cards[self.player_barter[0]])
                        min_card_player2 = min(self.player_cards[self.player_barter[1]])
                        min_card_player3 = min(self.player_cards[self.player_barter[2]])
                        self.player_cards[self.player_barter[0]].append(min_card_player3)
                        self.player_cards[self.player_barter[1]].append(min_card_player2)
                        self.player_cards[self.player_barter[2]].append(min_card_player1)

                        self.player_cards[self.player_barter[0]].remove(min_card_player1)
                        self.player_cards[self.player_barter[1]].remove(min_card_player2)
                        self.player_cards[self.player_barter[2]].remove(min_card_player3)

                        del self.player_barter[:]
                        break

        print()
        self.gameplay()
        self.conditionAI(point_barter=1)


    def end(self):
        pass


if __name__ == "__main__":
    play = QiuQiu()
    play.start()