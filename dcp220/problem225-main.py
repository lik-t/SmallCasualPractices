# This problem is asked by Bloomberg.
# There are `N` prisoners standing in a circle, waiting to be executed. The
# executions are carried out starting with the `k`th person, and removing
# every successive `k`th person going clock wise until there is no one left.
# ----
# Given `N` and `k`, write an algorithm to determine where a prisoner should
# stand in order to be the last survivor.
# ----
# For example, if `N = 5` and `k = 2`, the order of executions would be
# `[2, 4, 1, 5, 3]`, so you should return `3`.

import unittest


def last_survivor(n, k):

    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("Only integers are valid inputs!")

    if n <= 0 or k <= 0:
        raise ValueError("N and k cannot be zero or minus!")

    circle = list(range(1, n+1))
    killed = 0
    for i in range(n-1):
        killed += k - 1
        if killed + 1 > n - i:
            killed %= (n-i)
        del circle[killed]

    return circle[0]

# the following is the code to test


class CheckResults(unittest.TestCase):

    def test_k_le_N(self):
        self.assertEqual(last_survivor(5, 1), 5)
        self.assertEqual(last_survivor(5, 2), 3)
        self.assertEqual(last_survivor(5, 3), 4)
        self.assertEqual(last_survivor(5, 4), 1)
        self.assertEqual(last_survivor(10, 1), 10)

    def test_k_eq_N(self):
        self.assertEqual(last_survivor(5, 5), 2)
        self.assertEqual(last_survivor(6, 6), 4)

    def test_k_la_N(self):
        self.assertEqual(last_survivor(5, 6), 4)
        self.assertEqual(last_survivor(5, 7), 4)
        self.assertEqual(last_survivor(4, 8), 3)


if __name__ == "__main__":
    unittest.main()