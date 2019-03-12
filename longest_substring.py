'''
Find the longest substring in 2 strings
Find the length of longest substring in 2 strings
'''


def length_max_substring(s1, s2, i, j, count):
    if i == 0 or j == 0:
        return count
    if s1[i - 1] == s2[j - 1]:
        count = length_max_substring(s1, s2, i - 1, j - 1, count + 1)

    count = max(count, max(length_max_substring(s1, s2, i, j - 1, 0), length_max_substring(s1,s2,i - 1, j, 0)))
    return count


if __name__ == '__main__':
    X = "abcdxyz"
    Y = "xyzabcd"
    i = len(X)
    k = len(Y)
    print(length_max_substring(X, Y, i, k, 0))
