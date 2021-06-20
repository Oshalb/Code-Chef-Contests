# The Wave

def pol_function(a, x):
    p, n = 0, 0
    """for i in a:
        p *= x - i"""
    if x in a:
        return 0
    else:
        for i in a:
            if x < 0:
                return "POSITIVE"
            elif x < i:
                n += 1
            elif x > i:
                p += 1
        if n % 2 != 0 and n != 0:
            return "NEGATIVE"
        else:
            return "POSITIVE"


if __name__ == "__main__":
    length_of_a_values, number_of_queries = map(int, input().split())
    values_of_a = list(map(int, input().rstrip().split()))
    for _ in range(number_of_queries):
        result = pol_function(values_of_a, int(input()))
        print(result)
