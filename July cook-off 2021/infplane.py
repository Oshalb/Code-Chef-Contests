# Chef In Infinite Plane

def count_pairs(a):
    sa = set(a)
    d = {}
    for i in sa:
        z = a.count(i)
        x = i//2
        d[i] = min(x, z)
    c = sum(d.values())
    return c


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        length_of_list = int(input())
        list_to_check = list(map(int, input().rstrip().split()))
        result = count_pairs(list_to_check)
        print(result)
