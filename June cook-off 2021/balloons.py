# ICPC Balloons
# https://www.codechef.com/COOK130C/problems/BALLOON

def check_questions(a):
    c = 0
    ques = [1, 2, 3, 4, 5, 6, 7]
    for i, q in enumerate(a):
        if q in ques:
            c += 1
        if c == 7:
            return i + 1


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        number_of_question = int(input())
        list_of_question = list(map(int, input().rstrip().split()))
        result = check_questions(list_of_question)
        print(result)
