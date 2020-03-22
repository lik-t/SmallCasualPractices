# This problem was asked by Airbnb.
# You come across a dictionary of sorted words in a language you've never
# seen before. Write a program that returns the correct order of letters in
# this language.
# For example, given
# ['xww', 'wyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y'].

import unittest
from collections import UserList


def update_table(table, current_letter, next_letter):
    """
    Update the table. Table is realized by using dictionary. The time to
    search an item in dictionary is constant, regardless of how many
    elements it has.
    :param table:
    :param current_letter:
    :param next_letter:
    :return:
    """
    if current_letter in table:
        table[current_letter][1].add(next_letter)
    else:
        table[current_letter] = [set(), {next_letter}]

    if next_letter in table:
        table[next_letter][0].add(current_letter)
    else:
        table[next_letter] = [{current_letter}, set()]

    return table


def search_to_fill_table(target, table):
    """
    Search through the target list and to record the information found in
    the table. The table has the form:
    | letter |  front  |  back   |
    | x      |         | y       |
    | y      |  w      |         |
    After the table is formed, x has no front-letter, its the first letter.
    Then eliminate the row contains x, and x in other rows. Then the letter
    without front-letter should come just after letter-x.
    :param target:
    :param table:
    :return:
    """
    if len(target) <= 1:
        return {}

    current_letter = ''

    i = 0
    # 使用While Loop搜索，因为在这过程中列表的长度会变化
    while 1:
        if current_letter == '':
            try:
                current_letter = target[0][0]
            except IndexError:
                return table

        next_letter = target[i][0]
        end_position = i

        if next_letter != current_letter:
            table = update_table(table, current_letter, next_letter)
            current_letter = next_letter

            for k in range(end_position):
                target[k] = target[k][1:]
            small_target = target[:end_position]
            target = target[end_position:]
            search_to_fill_table(small_target, table)
            i = 0

        elif i == len(target)-1:
            for k in range(end_position+1):
                target[k] = target[k][1:]
            small_target = target
            target = target[end_position:]
            # 此语句，相当于是决定了何时结束递归。
            # 递归结束的语句往往放在函数定义的开始，这需要深入思考一下
            search_to_fill_table(small_target, table)
            current_letter = ''
            i = 0
        else:
            i = i + 1

    return table


def parse_table(table, alphabet):
    """
    Parse the table formed by search_to_fill_table() method and return a
    list containing all the letters in order. The table is represented by
    embedded list.
    Information about the order of letters are collected by
    search_to_fill_method(). For each letter, we know all the letters before it
     and all letters after it. We notice that the 1st without any letter
     before it. We find it, put it into the list. Then we delete the 1st
     letter in the table, the 2nd letter has no letter before it. We find
     it, append it into the list. Repeat the above step until the table is
     empty.
     As implied in the above description, the process is recursive.
    :param alphabet:
    :param table: a table represented by embedded list. 1st column contains
    the letter, 2nd the letters before it and 3rd the letters after it.
    :return: a list, in which all letters stands in order.
    """

    if len(table) == 1:
        for kunci in table.keys():
            return [kunci]

    for key, value in table.items():
        if value[0] == set(alphabet):
            break
    del table[key]
    alphabet.append(key)
    result = parse_table(table, alphabet)
    return alphabet.extend(result)


def find_alphabet(words_sequence):
    return parse_table(search_to_fill_table(words_sequence, {}), [])


if __name__ == "__main__":
    import time
    import random
    import string

    all_lowercase_letters = list(string.ascii_lowercase)
    long_list = []
    for i in range(1000):
        string = ''
        j = random.randint(10, 50)
        for k in range(j):
            string += random.choice(all_lowercase_letters)
        long_list.append(string)
    long_list = sorted(long_list)

    test_target = ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']

    start = time.time()
    result1 = find_alphabet(test_target)
    print(f"total time used is { time.time() - start } ")
    print(result1)

    start = time.time()
    result2 = find_alphabet(long_list)
    total_time = time.time() - start
    print(f"total time used is {total_time}")
    print(result2)

