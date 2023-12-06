'''
Day 03 Objects
'''

import logging
from math import prod
import re
from typing import Tuple
from data_loader import DataLoader

class EngineGear:
    '''
    _summary_
    '''
    def __init__(self,x:int,y:int) -> None:
        self.x:int = x
        self.y:int = y
        self.parts:list[int] = []

    def is_valid_gear(self) -> bool:
        '''
        A valid gear must have exactly two parts

        Returns:
            True if the gear is a valid gear, false otherwise.
        '''
        return len(self.parts) == 2

    def gear_ratio(self) -> int:
        '''
        _summary_

        Returns:
            _description_
        '''
        if self.is_valid_gear():
            return prod(self.parts)
        return 0

class EngineSchematic:
    '''
    _summary_
    '''
    def __init__(self) -> None:
        self.grid:list[str] = []
        self.gears:list[EngineGear] = []

    def update_gear(self,x:int,y:int,part:int) -> None:
        '''
        Check to see if a gear exists with the same x,y coordinates.
        If no, createa new gear first.
        Finally add the part to gear you found or the new gear.

        Arguments:
            x -- x coordinate
            y -- y coordinate
            part -- Integer number of the part
        '''
        found_gear:EngineGear|None = None
        for gear in self.gears:
            if gear.x == x and gear.y == y:
                found_gear = gear
        if found_gear is None:
            found_gear = EngineGear(x,y)
            self.gears.append(found_gear)
        found_gear.parts.append(part)

    def check_is_part(self,span:Tuple[int,int],y:int,part_number:int) -> bool:
        '''
        _summary_

        Arguments:
            span -- The span [start,end) of the number.
            y -- The row of the grid being processed.

        Returns:
            Is the number represented by the span on line y a valid part?
        '''
        is_part:bool = False
        # Match anything that is not alphanumeric or a period.
        pattern:re.Pattern[str] = re.compile(r'([^\w,.])')
        # The start index is either the position of start of span or 0 to
        # ensure the index is valid.
        start_index:int = max(span[0]-1,0)
        # The end index is either the position of the end index + 1 (span are non-inclusive),
        # or the last index of the row.
        end_index:int = min(span[1]+1,len(self.grid[0]))
        # Check Above
        if y > 0 and not is_part:
            check_row:str = self.grid[y-1]
            check_string:str = check_row[start_index:end_index]
            for matched in re.finditer(pattern,check_string):
                is_part = True
                if matched.group() == '*':
                    self.update_gear(matched.span()[0]+start_index,y-1,part_number)
        # Check Right
        if not is_part:
            for matched in re.finditer(pattern,self.grid[y][end_index-1]):
                is_part = True
                if matched.group() == '*':
                    self.update_gear(matched.span()[0]+end_index-1,y,part_number)
        # Check Bottom
        if y < len(self.grid)-1 and not is_part:
            check_row:str = self.grid[y+1]
            check_string:str = check_row[start_index:end_index]
            for matched in re.finditer(pattern,check_string):
                is_part = True
                if matched.group() == '*':
                    self.update_gear(matched.span()[0]+start_index,y+1,part_number)
        # Check Left
        if not is_part:
            for matched in re.finditer(pattern,self.grid[y][start_index]):
                is_part = True
                if matched.group() == '*':
                    self.update_gear(matched.span()[0]+start_index,y,part_number)
        return is_part

    def process_grid(self) -> Tuple[int,int]:
        '''
        _summary_

        Returns:
            _description_
        '''
        score:int = 0
        gear_ratio:int = 0
        pattern:re.Pattern[str] = re.compile(r'\d+')
        for y, row in enumerate(self.grid):
            for matched in re.finditer(pattern,row):
                value:int = int(matched.group())
                is_part:bool = self.check_is_part(matched.span(),y,value)
                if is_part:
                    score += value
        for gear in self.gears:
            gear_ratio += gear.gear_ratio()
        return (score,gear_ratio)

def day03_main() -> None:
    '''
    _summary_

    Arguments:
        part -- _description_
    '''
    for mode in ['test','actual']:
        filename:str
        filename = 'day03a'
        data:list[str]|None = DataLoader.load_data(filename,mode)
        schematic:EngineSchematic = EngineSchematic()
        if data:
            for line in data:
                schematic.grid.append(line)
        results:Tuple[int,int] = schematic.process_grid()
        print(f'Day 03-a {mode}: Power Score={results[0]}')
        print(f'Day 03-b {mode}: Gear Ratio={results[1]}')
