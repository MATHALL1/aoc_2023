'''
Day 03 Objects
'''

import re
from typing import Tuple
from data_loader import DataLoader

class EngineSchematic:
    '''
    _summary_
    '''
    def __init__(self) -> None:
        self.grid:list[str] = []
        self.symbols:list[str] = ['*','+','#','$']

    def check_cell(self,span:Tuple[int,int],y:int) -> bool:
        '''
        _summary_

        Arguments:
            span -- _description_
            y -- _description_

        Returns:
            _description_
        '''
        is_part:bool = False
        pattern:re.Pattern[str] = re.compile(r'(^\w|^.)')
        start_index:int = max(span[0]-1,0)
        end_index:int = min(span[1]+1,len(self.grid[0])-1)
        #print(f'Checking start={start_index}, end={end_index}')
        # Check Above
        if y > 0 and not is_part:
            check_row:str = self.grid[y-1]
            check_string:str = check_row[start_index:end_index]
            matches:re.Match[str]|None = re.search(pattern,check_string)
            if matches:
                is_part = True
        # Check Right
        if re.search(pattern,self.grid[y][end_index-1]) and not is_part:
            is_part = True
        # Check Bottom
        if y < len((self.grid[0]))-1 and not is_part:
            check_row:str = self.grid[y+1]
            check_string:str = check_row[start_index:end_index]
            matches:re.Match[str]|None = re.search(pattern,check_string)
            if matches:
                is_part = True
        # Check Left
        if re.search(pattern,self.grid[y][start_index]) and not is_part:
            is_part = True
        return is_part

    def process_grid(self) -> int:
        '''
        _summary_

        Returns:
            _description_
        '''
        pattern:re.Pattern[str] = re.compile(r'\d+')
        score:int = 0
        for y, row in enumerate(self.grid):
            for matched in re.finditer(pattern,row):
                is_part:bool = self.check_cell(matched.span(),y)
                if is_part:
                    # print(f'Value:{matched.group()}')
                    score += int(matched.group())
        return score

def day03_main(part:str) -> None:
    '''
    _summary_

    Arguments:
        part -- _description_
    '''
    for mode in ['test','actual']:
        filename:str
        if part=='a' or mode=='actual':
            filename = 'day03a'
        else:
            filename = 'day03b'
        data:list[str]|None = DataLoader.load_data(filename,mode)
        schematic:EngineSchematic = EngineSchematic()
        if data:
            for line in data:
                schematic.grid.append(line)
        score:int = schematic.process_grid()
        print(f'Day 03-{part} {mode}: Power Score={score}')
