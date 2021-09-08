"""
Travel Pass.
Calculate the amount of time it takes to travel.
"""


def calculate_time(a, b, s):
    ones = s.count('1')
    zeros = s.count('0')

    return (zeros * a) + (ones * b)


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        length_of_string, inter_district_time, inter_state_time = \
            map(int, input().rstrip().split())
        string_to_check = str(input())
        result = calculate_time(inter_district_time, inter_state_time, string_to_check)
        print(result)
