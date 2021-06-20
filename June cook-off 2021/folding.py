# XOR Folding

def xor_operation(n, m, g):
    for _ in range(2):
        j, k = n, m
        c = g[j][k]
        if n > m:
            counter = 0
        else:
            counter = 1
        for i in range(n+m):
            if counter == 1:
                c ^= g[j][k-1]
                k -= 1
                counter -= 1
            else:
                c ^= g[j-1][k]
                j -= 1
                counter += 1
            if k == 0 or j < 0:
                if counter == 1:
                    return "Yes"
                else:
                    return "No"


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        rows_of_grid, column_of_grid = map(int, input().split(" "))
        grid_to_check = []
        for i in range(rows_of_grid):
            grid_to_check.append(str(input()))
        result = xor_operation(rows_of_grid, column_of_grid, grid_to_check)
