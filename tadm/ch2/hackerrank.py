# https://www.hackerrank.com/challenges/the-power-sum/problem
# The below solution is a O(2^n) solution which will be improved with back tracking
def powerSum(X, N):
    nth_root = math.floor(pow(X, (1 / N)))

    square_list = [pow(x, N) for x in range(1, nth_root + 1)]

    total = 0
    print("nth root: ", nth_root, pow(2, nth_root))
    for num in range(1, pow(2, nth_root)):
        tmp = []
        for i in range(0, nth_root):
            if (1 & num >> i) == 1:
                tmp.append(i)
        square_sum = 0
        for index in tmp:
            square_sum += square_list[index]

        # print("tmp: ", tmp)
        # print("square_sum: ", square_sum)
        if square_sum == X:
            total += 1
    print(total)
    return total


# https://www.hackerrank.com/challenges/magic-square-forming/problem
# yet to be implemented


# https://www.hackerrank.com/challenges/pangrams/problem
def pangrams(s):
    a = set()

    # O(n)
    for letter in s:
        if letter != " ":
            a.add(letter.lower())
            if len(a) == 26:
                return "pangram"
    return "not pangram"