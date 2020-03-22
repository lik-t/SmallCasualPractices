# Problem #235 [Hard]: This problem is asked by Facebook.
# Given an array of numbers of length `N`, find both the minimum and maximum
# using less than `2 * (N - 2)` comparisons.


def find_mnm_mxm(array):
    """Return both the minimum and the maximum number of an array.
    """
    mnm = mxm = array[0]
    j = 0               # record how many comparison are used
    for i in range(1, len(array)):
        if array[i] > mxm:
            j += 1
            mxm = array[i]
        else:
            if array[i] < mnm:
                j += 1
                mnm = array[i]
    return mnm, mxm, j, len(array)


array = [10, 11, 9, 12, 8, 13, 7, 14, 6, 15, 5, 16, 4, 17, 3, 18, 2, 19, 1,
         20]
result = find_mnm_mxm(array)
print(result)

array = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
         27, 28, 29]
result = find_mnm_mxm(array)
print(result)

array = [-10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6,
         -7, -8, -9]
result = find_mnm_mxm(array)
print(result)