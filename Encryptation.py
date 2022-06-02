import math
import os
import random
import re
import sys


def readPrhase() -> str:
    phrase: str = input()
    return phrase


def removeSpaces(phrase) -> str:
    s: str = phrase.replace(" ", "")
    return s


def convert_str_to_list(string: str) -> list[str]:
    list1 = []
    list1[:0] = string
    return list1


def nested_list(rows:int, columns:int, list_string: list[str]) -> list[str]:
    list1: list[str] = [list_string[columns*i:columns*(i+1)] for i in range(0,rows)]
    return list1


def spaces_to_fill(rows:int, list1: list[str]) -> list[str]:
    complete_list: list[str] = []
    spaces_to_fill: int = 0
    spaces_to_fill = len(list1[rows-2]) - len(list1[rows-1])
    return spaces_to_fill


def fill_spaces(rows:int, spaces_to_fill: int, list1: list[str]) -> list[str]:
    complete_list = list1
    for i in range(0, spaces_to_fill): complete_list[rows-1].append(" ")
    return complete_list


def column_list(rows:int, j:int, list1: list[str]) -> list[str]:
    column_list: list[str] = []
    column_list = [list1[i][j] for i in range(0,rows)]
    return column_list


def convert_to_list_str_1(list1: list[str]) -> list[str]:
    list_str_1: list[str] = "".join(list1)
    return list_str_1


def organize_words(rows:int, columns:int, complete_list:list[str]):
    for j in range(0, columns):
        encrypted_list: list[str] = column_list(rows, j, complete_list) 
        list_str_1: list[str] = convert_to_list_str_1(encrypted_list)
        print(removeSpaces(list_str_1), end=" ")


    


if __name__ == '__main__':
    phrase: str = readPrhase()
    string: str = removeSpaces(phrase)
    list_string: list[str] = convert_str_to_list(string) 
    L: int = len(list_string)
    root: float = math.sqrt(L)
    rows: int = math.floor(root)
    columns: int = math.ceil(root)
    if rows * columns < L:
        rows += 1
    nested_list: list[str] = nested_list(rows, columns, list_string)
    spaces_to_fill: int = spaces_to_fill(rows, nested_list)
    complete_list: list[str] = fill_spaces(rows, spaces_to_fill, nested_list)
    organize_words(rows, columns, complete_list)

    # 2:00 pm  -- 5:00 pm
    # if man was meant to stay on the ground god would have given us roots