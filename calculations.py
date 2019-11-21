import math


def divide_binary(number, length):
    result = ''
    for _ in range(length):
        number *= 2
        number, whole = math.modf(number)
        result += str(int(whole))
    return result


def calculate_code_length(prob):
    float_part = math.log2(1 / prob)
    return math.floor(float_part) + 1


def calculate_single_code(midprob, code_length):
    return divide_binary(midprob, code_length)


def calculate_midprob(prob, total_prob):
    return total_prob - 0.5 * prob


def calculate_codes(entries):
    codes = []
    total_prob = 0

    for symbol, prob in entries:
        total_prob += prob
        midprob = calculate_midprob(prob, total_prob)
        code_length = calculate_code_length(prob)
        code = calculate_single_code(midprob, code_length)
        codes.append((symbol, code))

    return codes
