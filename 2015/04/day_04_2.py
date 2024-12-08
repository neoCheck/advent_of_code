#!/usr/bin/env python
import hashlib


def main() -> None:
    day_input = "bgvyzdsv"

    i = 0
    while True:
        i += 1
        res = hashlib.md5(f"{day_input}{i}".encode("utf-8")).hexdigest()
        if res.startswith("000000"):
            print(f"{i}: {res}")
            break



if __name__ == "__main__":
    main()
