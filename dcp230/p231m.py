# Problem #231 [Easay]. This problem is asked by IBM.
# Given a string with repeated characters, rearrange the string so that no
# two adjacent characters are the same. If this is not possible, return `None`.
# For example, given "aaabbc", you could return "ababac". Given "aaab",
# return `Noe`.

import unittest


def rearrange_r1(in_str):
    """

    :param in_str:
    :return:
    """
    # Ideas:
    # step-0: If string has only one character, return itself.
    #       If string has two character, return  `None`.
    # step-1: fetch a character from the string, put it into a list A
    # step-2: fetch a character from B (Point I), and put it into list A.
    # step-3: fetch next character from the string (Point II), compare it with
    # the last character in list A.
    #       2.1: if not same, put it into list A.
    #           repeat step-2
    #       2.2: if same, put it into list B.
    #           repeat step-3
    #       II: If string is over, but B is not, return `None`.
    # ------------------------
    # step-0
    if len(in_str) <= 1:
        return in_str
    if len(in_str) == 2 and in_str[0] == in_str[1]:
        return None
    # step-1
    list_a = [in_str[0]]
    list_b = []
    for char in in_str[1:]:
        if char == list_a[-1]:  # step 2.2
            list_b.append(char)
        else:  # step 2.1
            list_a.append(char)
            if list_b:
                list_a.append(list_b[-1])
                del list_b[-1]
    if list_b:
        return None
    else:
        return ''.join(list_a)


class CheckResults(unittest.TestCase):

    def test_rearrange_r1(self):
        # input string is empty, return `None`
        self.assertEqual(rearrange_r1(''), '')
        # if string has only one letter, return itself
        self.assertEqual(rearrange_r1('a'), 'a')
        # if string has two repeated letter, return `None`
        self.assertEqual(rearrange_r1('aa'), None)
        # test the example
        self.assertEqual(rearrange_r1("aaab"), None)
        self.assertEqual(rearrange_r1("aaabbc"), "ababac")
        self.assertEqual(rearrange_r1("aaaabbc"), "ababaca")


if __name__ == "__main__":
    unittest.main()