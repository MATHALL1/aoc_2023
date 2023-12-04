'''
Load data
'''
import logging

class DataLoader:
    '''
    Statc class that helps loading data.
    '''
    @classmethod
    def load_data(cls,filename:str,mode:str='test') -> list[str]|None:
        '''
        _summary_

        Args:
            filename (str): _description_
            mode (str, optional): _description_. Defaults to 'test'.
        '''
        folder:str = 'test_data' if mode == 'test' else 'actual_data'
        filepath:str = f'./src/aoc_2023/data/{folder}/{filename}.txt'
        try:
            with open(filepath,encoding='utf-8') as infile:
                data_lines:list[str] = infile.readlines()
                clean_lines:list[str] = [line.strip() for line in data_lines]
                return clean_lines
        except FileNotFoundError:
            logging.error(f'Error: File {filepath} not found.')
            return None
        except Exception as e:
            logging.error(f'Error: {e}')
            return None
