# False Number
# https://www.codechef.com/LTIME97C/problems/FALSNUM

def add_digit(s):
    if s[0] == '1':
        s[0] = "10"
    else:
        s[0] = "1" + s[0]
    return s


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        string_to_check = list(str(input()))
        result = add_digit(string_to_check)
        print(*result, sep="")
