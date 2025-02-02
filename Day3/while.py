"""
Created on 2025-01-05
"""


# Your code starts here


def use_while():
    i = 0
    result = 0
    while True:
        if i == 101:
            break
        if i % 2 == 1:
            i += 1
            continue
        result += i
        i += 1
    print(f"result={result}")


use_while()
