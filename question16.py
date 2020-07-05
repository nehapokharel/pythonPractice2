class super_mario:
    def __init__(self):
        print("Welcome!!")

    def game_info(self):
        player_option = input("Enter player option: ")
        self.opt = player_option
        return self.opt

    def total_score(self, name):
        self.player = name
        return self.player
    


z = super_mario()
print(z.game_info())
p = z.total_score('Zoya')
print("Start game!!! " + p)