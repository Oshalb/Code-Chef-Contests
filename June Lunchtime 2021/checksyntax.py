# HTML Tags
# https://www.codechef.com/LTIME97C/problems/HTMLTAGS

def check_string(s):
    if s[0] == '<':
        if s[1] == '/':
            if s[-1] == '>':
                del s[0]
                del s[0]
                del s[-1]
    else:
        return "Error"
    f = 0
    if len(s) == 0:
        return "Error"
    else:
        for i in s:
            if ord(i) in range(97, 123) or ord(i) in range(48, 58):
                pass
            else:
                f += 1
        return "Success" if f == 0 else "Error"


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        string_to_check = list(str(input()))
        result = check_string(string_to_check)
        print(result)
