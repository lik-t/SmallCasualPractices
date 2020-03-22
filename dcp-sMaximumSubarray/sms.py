import math

# Brute force method. Time complexity is $\Theta(n^2)$
def search_max_subar_r1(array):
    """

    :param array:
    :return:
    """
    # get the length for later iteration
    length = len(array)
    # initialize the maxsum and max_subar
    maxsum = array[0]
    max_subar = array[:1]
    # start outter loop
    # Algorithm is as follows:
    # 1. A start pointer, `i`, points the index [0]
    for i in range(length):
        # 2. If the value of index [i} >= maxsum, assign its value to
        # maxsum, and assign array of index[i:i+1] to max_subar.
        if array[i] >= maxsum:
            maxsum = array[i]
            max_subar = array[i:i+1]
        # 3. Check the value after index [i] one by one. If it's value >= 0,
        # add it to the temsum.
        # 4. If the temsum >= maxsum, update the maxsum and max_subar.
        # 5. If the it's value < 0, but after added, the temsum still > 0.
        # Keep searching.
        # 6. If the temsum < 0, stop searching.
        temsum = array[i]
        for j in range(i+1, length):
            if array[j] >= 0:
                temsum += array[j]
                if temsum >= maxsum:
                    maxsum = temsum
                    max_subar = array[i:j+1]
            else:       # array[j] < 0
                if (temsum + array[j]) < 0:
                    break
                else:
                    temsum += array[j]

    return max_subar


# Method in Execise 4.5-1. Time complexity is $\Theta(n)$
def search_max_subar_r2(array):
    """

    :param array:
    :return:
    """
    # Ideas description:
    # Step-1: 将最大子数组max_sum初始化为array[0:1]
    #       将暂时最大子数组temp_sum初始化为array[0:1]
    # Step-2: 从数组第2个数开始检查：
    #       2.1: 如果数组的第1个数是负数，那么检查用第2个数与第1个数比较：
    #           2.1.1: 如果第2个数大于第1个数，将临时最大子数组设为array[1:2]
    #       2.2：如果数组的第一个数是正数：
    #           2.2.1：
    for i, num in enumerate(array):
        if not i:    # When i == 0
            temp_sum = array[0]
            max_sum = array[0]
            temp_sub = array[0:1]
            max_sub = array[0:1]
        else:    # When i != 0
            # 中间夹的负数子数列的和太小，使其前面的最大序列变为了负，在此断开再搜
            # 相当于是重新初始化了一个temp_sum去开始记录新的子数列
            if temp_sum == -100000:
                temp_sum = num
                temp_sub = array[i:i+1]
            else:
                # 当到目前为止的最大子数组小于0时，如果发现比它大的，就替换
                if temp_sum < 0:
                    if num > temp_sum:
                        temp_sum = num
                        temp_sub = array[i:i+1]
                else:
                    if num > 0:
                        temp_sub.append(num)
                        temp_sum += num
                    else:
                        if temp_sum + num > 0:
                            temp_sub.append(num)
                            temp_sum += num
                        else:
                            temp_sum = -100000
                            temp_sub = []
            if temp_sum > max_sum:
                max_sum = temp_sum
                max_sub = temp_sub.copy()

    return max_sub


def find_max_crossing_subarray(array, low, mid, high):
    max_left = 0
    max_right = 0
    left_sum = - 100000
    sump = 0
    for i in range(low, mid + 1).__reversed__():
        sump += array[i]
        if sump > left_sum:
            left_sum = sump
            max_left = i
    right_sum = -100000
    sump = 0
    for j in range(mid + 1, high + 1):
        sump += array[j]
        if sump > right_sum:
            right_sum = sump
            max_right = j

    return max_left, max_right, left_sum + right_sum


# Divide and conquer paradigm. Time complexity is $\Theta(nlg(n))$
def find_maximum_subarray(array, low, high):
    if high == low:
        return low, high, array[low]    # base case: only one element
    else:
        mid = math.floor((low + high) / 2)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(
            array, low, mid, high)
        (left_low, left_high, left_sum) = find_maximum_subarray(
            array, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(
            array, mid + 1, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def search_max_subar_r3(array):
    low, high, sum = find_maximum_subarray(array, 0, len(array) - 1)
    return array[low:high + 1]


if __name__ == "__main__":
    A = [-1, -12, 3, -2, 100, 4, 4, -10, 5, 1, 9]
    print(search_max_subar_r1(A))
    B = [-10, -1, -5]
    print(search_max_subar_r1(B))
    C = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(search_max_subar_r1(C))
    # print(search_max_subar_r2(A))
    # print(search_max_subar_r2(B))
    # print(search_max_subar_r2(C))
    print(search_max_subar_r3(A))
    print(search_max_subar_r3(B))
    print(search_max_subar_r3(C))

