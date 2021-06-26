# Richie Rich
# https://www.codechef.com/LTIME97C/problems/CHFRICH

def get_time(a, b, x):
    if a >= b:
        return 0
    else:
        c = b - a
        return int(c/x)


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        current_worth, highest_worth, increase_in_worth = map(int, input().rstrip().split())
        result = get_time(current_worth, highest_worth, increase_in_worth)
        print(result)
