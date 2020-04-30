#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    valid_operators = "+-*/"
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div}

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, b, op = int(argv[1]), int(argv[3]), argv[2]

    if op not in valid_operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {} {:d} = {:d}".format(a, op, b, operations[op](a, b)))
