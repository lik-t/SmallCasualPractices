# Problem #230 [Medium]. This problem is asked by Goldman Sachs.
# You are given `N` identical eggs and access to a building with `k` floors.
# Your task is to find the lowest floor that will case an egg to break,
# if dropped from that floor. Once an egg breaks, it cannot be dropped
# again. If an egg breaks, it cannot be dropped again. If an egg breaks when
# dropped from `x-th` floor, you can assume it will also break when dropped
# from any floor greater than `x.
# --------------------------------------------------------------------------
# ??? Write an algorithm that finds the minimum number of trial drops it
# will take, in the worst case, to identify this floor.
# --------------------------------------------------------------------------
# For example, if `N = 1` and `k = 5`, we will need to try dropping the egg
# at every floor, beginning with the first, until we reach the fifth floor,
# so our solution will be `5'.

import unittest


def break_or_not(floor_num):
    return True if floor_num >= 70 else False


def find_break_floor_r1(num_of_floor):
    """
    This realization use the direct loop method to check one by one. This
    method is very intuitive, with a very simple code. The time complexity is
    O(n). The space complexity is O(1).
    :param num_of_floor:
    :return:
    """
    for i in range(1, num_of_floor + 1):
        if break_or_not(i):
            return i
    return None


def df(start_floor, end_floor):
    """
    Divide-and-conquer paradigm:
    Divide the problem into a number of subproblems that are smaller
    instances of the same problem. Notice, the subproblems may be said to be
    the same as the original problems, except it is generally smaller in size.
    Conquer the subproblems by solving them recursively. If the subproblem
    size are small enough, however, just solve the subproblems in a
    straightforward manner.
    Combine the solutions to the subproblems into the solution for the
    original problem.
    :param start_floor:
    :param end_floor:
    :return:
    """
    if not break_or_not(end_floor):
        return None
    elif break_or_not(start_floor):
        return start_floor
    else:
        middle = start_floor + end_floor
        middle = int((middle % 2 + middle) / 2)
        if not break_or_not(middle):    # not break
            return df(middle + 1, end_floor)    # try in higher floor
        else:                           # break
            return df(start_floor + 1, middle)  # try at lower floor


def find_break_floor_r2(num_of_floor):
    """
    This implementation uses the divide-and-conquer (分而治之) paradigm, mainly
    realized by df() method.
    :param num_of_floor:
    :return:
    """
    return df(1, num_of_floor)


class CheckResults(unittest.TestCase):

    def test_find_break_floor_r1(self):
        import random
        num_of_floor = 100
        self.assertEqual(find_break_floor_r1(num_of_floor), 70)

    def test_find_break_floor_r2(self):
        import random
        num_of_floor = 100
        self.assertEqual(find_break_floor_r2(num_of_floor), 70)


if __name__ == '__main__':
    unittest.main()

# Comments:
#
