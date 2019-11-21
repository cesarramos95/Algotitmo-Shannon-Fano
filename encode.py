#!/usr/bin/env python3

from calculations import calculate_codes


def encode(symbol_sequence, codes):
    encoded = []
    codes_dict = dict(codes)

    for symbol in symbol_sequence:
        code = codes_dict.get(symbol)
        if code is None:
            raise Exception(f"Invalid symbol: {symbol}")
        encoded.append(code)

    encoded = ' '.join(encoded)
    return encoded


def main():
    raw_symbols = input("Enter symbols that should be encoded: ")
    symbols = raw_symbols.split()

    raw_probs = input("Enter their probabilities: ")
    probs = [float(prob) for prob in raw_probs.split()]

    if len(symbols) != len(probs):
        raise Exception("Amount of probabilities should be equal"
                        "to amount of symbols")

    message = input("Enter the message to encode (e.g. 'A B C D'): ")
    symbol_sequence = message.split()

    codes = calculate_codes(zip(symbols, probs))
    encoded = encode(symbol_sequence, codes)
    print("Encoded message:", encoded)


if __name__ == '__main__':
    main()
