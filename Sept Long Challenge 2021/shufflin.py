"""
Shuffling Parties.
Odd even pairs.
"""


def check_sum(a, n):
    no_of_even = int(n/2)
    no_of_odd = n - no_of_even
    no_of_even_in_list = 0
    for i in a:
        if i % 2 == 0:
            no_of_even_in_list += 1
    no_of_odd_in_list = n - no_of_even_in_list
    print(no_of_odd, no_of_odd_in_list)
    print(no_of_even, no_of_even_in_list)
    total = min(no_of_odd_in_list, no_of_even) + min(no_of_odd, no_of_even_in_list)
    return total


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        length_of_list = int(input())
        list_to_check = list(map(int, input().rstrip().split()))
        result = check_sum(list_to_check, length_of_list)
        print(result)
