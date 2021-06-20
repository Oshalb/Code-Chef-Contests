# Chefland Visa
# https://www.codechef.com/COOK130C/problems/VISA

def check_visa_approval(x1, x2, y1, y2, z1, z2):
    if x2 >= x1:
        if y2 >= y1:
            if z1 >= z2:
                return "Yes"
    return "No"


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        data_to_use = list(map(int, input().rstrip().split()))
        result = check_visa_approval(data_to_use[0], data_to_use[1], data_to_use[2], data_to_use[3],
                                     data_to_use[4], data_to_use[5])
        print(result)
