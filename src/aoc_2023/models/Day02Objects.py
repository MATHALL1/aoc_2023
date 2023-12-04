'''
Day 02 Objects
'''

class DiceGame:
    
    def __init__(self,_id:int) -> None:
        self._id:int = _id
        self.dice:dict[str,int] = {}
