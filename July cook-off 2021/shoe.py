# Shoe Fit

if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        values_to_check = list(map(int, input().rstrip().split()))
        if 1 in values_to_check and 0 in values_to_check:
            print(1)
        else:
            print(0)
