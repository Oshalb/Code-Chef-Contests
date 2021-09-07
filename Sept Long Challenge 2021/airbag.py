"""
Check the weight limit of the bags allowed in a flight.
"""
import string


def check_limit(w):
    c = ""
    if (w['A'] + w['B'] <= w['D']) and w['C'] <= w['E']:
        c += "YES"
    elif (w['C'] + w['B'] <= w['D']) and w['A'] <= w['E']:
        c += "YES"
    elif (w['A'] + w['C'] <= w['D']) and w['B'] <= w['E']:
        c += "YES"
    else :
        c += "NO"
    return c


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        weight_to_check = {}
        for i, j in zip(string.ascii_uppercase, map(int, input().rstrip().split())):
            weight_to_check[i] = j
        result = check_limit(weight_to_check)
        print(result)
