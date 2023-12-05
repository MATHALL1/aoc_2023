'''
Main Program File
'''
import logging
from models import Day01Objects, Day02Objects, Day03Objects

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
    # Day01Objects.day01_main('a')
    # Day01Objects.day01_main('b')
    # Day02Objects.day02_main('a')
    # Day02Objects.day02_main('b')
    Day03Objects.day03_main('a')

if __name__ == '__main__':
    main()
