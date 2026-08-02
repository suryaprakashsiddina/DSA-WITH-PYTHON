def prefix_sum1(arr, n):
    res = [0] * n

    for i in range(1, n):
        res[i] = res[i - 1] + arr[i - 1]

    return res


def suffix_sum1(arr, n):
    res = [0] * n

    for i in range(n - 2, -1, -1):
        res[i] = res[i + 1] + arr[i + 1]

    return res


class Solution:
    def equilibrium(self, arr):
        n = len(arr)

        if n == 1:
            return True

        prefix_sum = prefix_sum1(arr, n)
        suffix_sum = suffix_sum1(arr, n)

        for i in range(n):
            if prefix_sum[i] == suffix_sum[i]:
                return "true"

        return "false"