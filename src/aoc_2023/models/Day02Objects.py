'''
Day 02 Objects
'''

from data_loader import DataLoader

class DiceSet:

    def __init__(self) -> None:
        self.dice:dict[str,int] = {}

class DiceGame:
    
    def __init__(self,_id:int) -> None:
        self._id:int = _id
        self.sets:list[DiceSet] = []
        self.dice_bag:dict[str, int] = {
            'red': 12,
            'green': 13,
            'blue': 14
        }
    
    def is_valid_game(self) -> bool:
        valid_game:bool = True
        for set in self.sets:
            for colour,count in set.dice.items():
                if self.dice_bag[colour] < count:
                    valid_game = False
        return valid_game
    
    def minimum_dice_score(self) -> int:
        score:int = 0
        dice_bag:dict[str, int] = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for set in self.sets:
            for colour,count in set.dice.items():
                if dice_bag[colour] < count:
                    dice_bag[colour] = count
        return (dice_bag['red']*dice_bag['green']*dice_bag['blue'])

def day02_main(part:str) -> None:
    for mode in ['test','actual']:
        filename:str
        if part=='a' or mode=='actual':
            filename = 'day02a'
        else:
            filename = 'day02b'
        data:list[str]|None = DataLoader.load_data(filename,mode)
        games:list[DiceGame] = []
        if data:
            for line in data: 
                items:list[str] = line.split(': ')
                game:DiceGame = DiceGame(int(items[0].split(' ')[1]))
                sets:list[str] = items[1].split('; ') 
                for set in sets:
                    dice_set:DiceSet = DiceSet()
                    for dice in set.split(', '): 
                        die:list[str] = dice.split(' ')
                        dice_set.dice[die[1]] = int(die[0])
                    game.sets.append(dice_set)
                games.append(game)
        if part=='a':
            valid_games:int = 0
            valid_score:int = 0
            for game in games:
                valid_games += 1 if game.is_valid_game() else 0
                valid_score += game._id if game.is_valid_game() else 0
            print(f'Day 02-{part} {mode}: Games={valid_games}, Score={valid_score}')
        else:
            score:int = 0
            for game in games:
                score += game.minimum_dice_score()
            print(f'Day 02-{part} {mode}: Power Score={score}')
