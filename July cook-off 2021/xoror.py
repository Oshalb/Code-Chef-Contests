# xor-ored

def min_xor(a):
    sa = set(a)
    dict_of_count = {}
    for i in sa:
        c = a.count(i)
        if c not in dict_of_count:
            dict_of_count[c] = [i]
        else:
            dict_of_count[c].append(i)
    d = max(dict_of_count)
    x_or = 0
    c = float('inf')
    for j in dict_of_count[d]:
        x_or = j
        a_xor = [i ^ x_or for i in a]
        a_or = 0
        for i in a_xor:
            a_or |= i
        if a_or < c:
            c = a_or
    return [x_or, c]


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        length_of_list = int(input())
        list_to_check = list(map(int, input().rstrip().split()))
        result = min_xor(list_to_check)
        print(*result, sep=' ')
