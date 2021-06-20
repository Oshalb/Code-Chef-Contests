# Binary String on Steroids

def calculate_ones(s, d):
    c = s.count('1')
    if (c == 2 and (s[0] == '1' and s[-1] == '1')) or c == 1:
        return 0
    elif c == 0:
        return 1
    elif (s[0] == '1' and s[-1] == '1') and (c > 2 and c != d):
        return c - 2
    else:
        return c - 1


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        length_of_string = int(input())
        string_to_check = (str(input()))
        result = calculate_ones(string_to_check, length_of_string)
        print(result)
