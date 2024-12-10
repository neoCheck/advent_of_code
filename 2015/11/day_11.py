#!/usr/bin/env python

def increment_password(password: str) -> str:
    increase_next = True
    new_password = ""

    for c in password[::-1]:
        if increase_next:
            if c == "z":
                new_c = "a"
                increase_next = True
            else:
                new_c = chr(ord(c) + 1)
                increase_next = False
        else:
            new_c = c

        new_password += new_c

    if increase_next:
        new_password += "a"

    return new_password[::-1]

def has_increasing_straight(password: str) -> bool:
    straight_list = [
        'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi',
        'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop',
        'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw',
        'vwx', 'wxy', 'xyz'
    ]

    for straight in straight_list:
        if straight in password:
            return True

    return False

def has_not_iol(password: str) -> bool:
    return "i" not in password and "o" not in password and "l" not in password

def has_double_pairs(password: str) -> bool:
    counter = 0
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if f"{letter}{letter}" in password:
            counter += 1
        if counter == 2:
            return True

    return False



def main() -> None:
    with open("input") as f:
        santa_password = f.read().strip()

    password = increment_password(santa_password)
    while True:
        password = increment_password(password)
        if has_not_iol(password) and has_increasing_straight(password) and has_double_pairs(password):
            print(password)
            return


if __name__ == "__main__":
    main()
