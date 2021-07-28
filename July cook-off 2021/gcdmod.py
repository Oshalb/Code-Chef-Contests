# Chef and GCD

def check_mod(x, y):
    if max(x, y) % min(y, x) == 0:
        return 0
    else:
        c = float('inf')
        for i in range(2):
            z = x
            b = y
            f = 0
            while max(z, b) % min(z, b) != 0:
                if i == 0:
                    z += 1
                    f += 1
                elif i == 1:
                    b += 1
                    f += 1
            if f < c:
                c = f
        return c


if __name__ == "__main__":
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        first_value, second_value = map(int, input().rstrip().split())
        result = check_mod(first_value, second_value)
        print(result)
