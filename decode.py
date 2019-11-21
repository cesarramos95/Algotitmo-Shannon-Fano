#!/usr/bin/env python3

from calculations import calculate_codes


def decode(code_sequence, codes):
    decoded = []
    codes_dict = {code: symbol for symbol, code in codes}

    for code in code_sequence:
        symbol = codes_dict.get(code)
        if symbol is None:
            raise Exception(f"Invalid code: {code}")
        decoded.append(symbol)

    decoded = ' '.join(decoded)
    return decoded


def main():
    raw_symbols = input("Enter symbols that were encoded: ")
    symbols = raw_symbols.split()

    raw_probs = input("Enter their probabilities: ")
    probs = [float(prob) for prob in raw_probs.split()]

    if len(symbols) != len(probs):
        raise Exception("Amount of probabilities should be equal"
                        "to amount of symbols")

    message = input("Enter the message to decode (e.g. '100 1001 101'): ")
    code_sequence = message.split()

    codes = calculate_codes(zip(symbols, probs))
    decoded = decode(code_sequence, codes)
    print("Decoded message:", decoded)


if __name__ == '__main__':
    main()
