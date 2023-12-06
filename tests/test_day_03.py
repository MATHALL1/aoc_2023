'''
Testing Day 3
'''

from typing import Tuple
import Day03Objects
def test_day_03_manual() -> None:
    '''
    Testing Day_03-Part_A scoring functions.
    '''
    data_01:list[str] = [
        '..........'
    ]
    data_02:list[str] = [
        '.100......',
        '.100......',
        '.100......',
    ]
    data_03:list[str] = [
        '#100......',
        '..........',
        '..........',
    ]
    data_04:list[str] = [
        '.100#......',
        '..........',
        '..........',
    ]
    data_05:list[str] = [
        '.100......',
        '#.........',
        '..........',
    ]
    data_06:list[str] = [
        '.100......',
        '.#........',
        '..........',
    ]
    data_07:list[str] = [
        '.100......',
        '....#.....',
        '..........',
    ]
    data_08:list[str] = [
        '.100#.....',
        '..........',
        '..........',
    ]
    data_09:list[str] = [
        '..#.......',
        '.100......',
        '..........',
    ]
    data_10:list[str] = [
        '..#.......',
        '.100......',
        '.100......',
    ]
    data_11:list[str] = [
        '..........',
        '.100......',
        '#100......',
    ]
    data_12:list[str] = [
        '.100......',
        '.100#.....',
        '.100......',
    ]
    data_13:list[str] = [
        '#100#.....',
        '#100#.....',
        '#100#.....',
    ]
    data_14:list[str] = [
        '..........',
        '.........#',
        '.......100',
    ]
    data_15:list[str] = [
        '..........',
        '......100.',
        '.........#',
    ]
    data_16:list[str] = [
        '.........#',
        '......100.',
        '..........',
    ]
    data_17:list[str] = [
        '..........................................389.314.................206......................449.523..................138.....................',
        '.........+.....954......723..........................................*.............687.....*..........692..........*........................',
        '121......992...............*.......%585....814............936.......102..#353.........*.....140.........*..434..301..................%..315.'
    ]

    day_03_manual(data_01,0)
    day_03_manual(data_02,0)
    day_03_manual(data_03,100)
    day_03_manual(data_04,100)
    day_03_manual(data_05,100)
    day_03_manual(data_06,100)
    day_03_manual(data_07,100)
    day_03_manual(data_08,100)
    day_03_manual(data_09,100)
    day_03_manual(data_10,100)
    day_03_manual(data_11,200)
    day_03_manual(data_12,300)
    day_03_manual(data_13,300)
    day_03_manual(data_14,100)
    day_03_manual(data_15,100)
    day_03_manual(data_16,100)
    day_03_manual(data_17,5368)

def day_03_manual(data:list[str],expected_score:int) -> None:
    '''
    Testing Day_03-Part_A scoring functions.
    '''
    schematic:Day03Objects.EngineSchematic = Day03Objects.EngineSchematic()
    for line in data:
        schematic.grid.append(line)
    results:Tuple[int,int] = schematic.process_grid()
    assert results[0] == expected_score
