class Move_Tutor:
    def __init__(self):
        self.available_moves = []

    def teach_move(self, move):
        self.available_moves.append(move)

class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.moves = []

    def learn_move(self, move):
        self.moves.append(move)

    def display_moves(self):
        print(f"{self.name}'s Moves:")
        for move in self.moves:
            print(move)

move_tutor = Move_Tutor()

move_tutor.teach_move("Fire Blast")
move_tutor.teach_move("Thunderbolt")
move_tutor.teach_move("Ice Beam")

pokemon = Pokemon("Charizard", 50)

pokemon.learn_move("Flamethrower")
pokemon.learn_move("Dragon Claw")

for move in move_tutor.available_moves:
    pokemon.learn_move(move)

pokemon.display_moves()