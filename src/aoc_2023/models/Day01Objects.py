'''
Day 01 Objects
'''
import logging
import re
from data_loader import DataLoader

def replace_digits(original_line:str) -> str:
    clean_line:str = original_line
    digits:dict[str,str] = {
        'one':'1','two':'2','three':'3','four':'4','five':'5',
        'six':'6','seven':'7','eight':'8','nine':'9'
    }
    
    if clean_line == '5vgftjvqkxj6pnctdcrktwoneq':
        pass

    # Find first match
    digit_list:str = '1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine'
    result = re.findall(rf'{digit_list}',clean_line)
    if result:
        if not result[0].isdigit():
            clean_line = clean_line.replace(
                result[0],
                digits[result[0]],
                1
            )
    # Find last match
    result = re.findall(rf'{digit_list[::-1]}',clean_line[::-1])
    if result:
        if not result[0].isdigit():
            reverse_line = clean_line[::-1].replace(
                result[0],
                digits[result[0][::-1]],
                1
            )
            clean_line = reverse_line[::-1]
    # Replace all non-digits in the string with null
    clean_line = re.sub(r'\D','',clean_line)
    return clean_line

def day01_main(part:str) -> None:
    '''
    Determine where the first number is:
        * It may be a digit
        * It may be spelled out
    Determine where the last number is:
        * It may be a digit
        * It may be spelled out

    Args:
        part (str): _description_
    '''
    for mode in ['test','actual']:
        filename:str
        if(part=='a' or mode=='actual'):
            filename = 'day01a'
        else:
            filename = 'day01b'
        data:list[str]|None = DataLoader.load_data(filename,mode)
        total_value:int = 0
        
        if(data):
            for data_line in data:
                if(part=='b'):
                    converted_line:str = replace_digits(data_line)
                else:
                    converted_line = data_line
                value:int = calculate_value(converted_line)
                total_value += value
                if(mode=='actual' and part=='b'):
                    logging.info(f'{data_line} -> {converted_line} -> {value}')
        print(f'Day 01-{part} {mode}: {total_value}')

def calculate_value(converted_line) -> int:
    first_digit:int = -1
    last_digit:int = -1
    value:int = -1
    # Look at each character/number in the string
    for item in converted_line:
        if(item.isdigit()):
            if(first_digit == -1):
                first_digit = int(item)
            last_digit = int(item)
    value = int(f'{first_digit}{last_digit}')
    if(value <= 10):
        print(f'negative value of {value}')
    return value