# Problem #232  [easy]. This problem is asked by Google.
# Implement a `PrefixMapSum` class with the following methods:
# - `insert(key: str, value: int)`: Set a given key's value in the map. If
# the key already exists, overwrite the value.
# - `sum(prefix: str)': Return the sum of all values of keys that begin with
# a given prefix.
# For example, you should be able to run the following code:
#   mapsum.insert("columnar", 3)
#   assert mapsum.sum("col") == 3
#
#   mapsum.insert("column", 2)
#   assert mapsum.sum("col") == 5


class PrefixMapSum:

    def __init__(self):
        self.elements = {}

    def insert(self, key, value):
        self.elements[key] = value

    def sum(self, prefix):
        temp_sum = 0
        for key, value in self.elements.items():
            if key.startswith(prefix):
                temp_sum += value
        return temp_sum


if __name__ == "__main__":
    mapsum = PrefixMapSum()
    mapsum.insert("column", 3)
    assert mapsum.sum("col") == 3
    mapsum.insert("columnar", 2)
    assert mapsum.sum("col") == 5