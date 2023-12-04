'''
Main Program File
'''
from distutils.command import clean
import logging
import re
from typing import Any, Iterator
from data_loader import DataLoader
from models import Day01Objects



def main() -> None:
    '''
    Main Program Loop
    '''
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logging.txt'
    )
    Day01Objects.day01_main('a')
    Day01Objects.day01_main('b')

if __name__ == '__main__':
    main()
