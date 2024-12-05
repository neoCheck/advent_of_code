#!/usr/bin/env python


def parse(day_input: str) -> tuple[dict[str, list[str]], list[list[str]]]:
    orders, numbers = day_input.split("\n\n")

    orders_dict: dict[str, list[str]] = {}
    for order in orders.split("\n"):
        before, after = order.split("|")
        before_list = orders_dict.get(before) or []
        before_list.append(after)
        orders_dict[before] = before_list

    numbers_list: list[list[str]] = [
        num_list.split(",")
        for num_list in numbers.split("\n")
    ]

    return orders_dict, numbers_list

def is_num_list_ordered(num_list: list[str], orders_dict: dict[str, list[str]]) -> bool:
    for i in range(len(num_list)):
        my_number = num_list[i]
        before_my_number = num_list[:i]

        should_be_after = orders_dict.get(my_number) or []
        for b_num in before_my_number:
            if b_num in should_be_after:
                return False


    return True

def correct_num_list(num_list: list[str], orders_dict: dict[str, list[str]]) -> list[str]:
    i = 0
    while i < len(num_list):
        my_number = num_list[i]
        before_my_number = num_list[:i]
        after_my_number = num_list[i+1:]
        i += 1

        should_be_after = orders_dict.get(my_number) or []
        corrected_num_list = []
        for b_num in before_my_number:
            if b_num in should_be_after:
                # retry sorting
                i = 0
                after_my_number = [b_num] + after_my_number
            else:
                corrected_num_list.append(b_num)

        corrected_num_list.append(my_number)
        corrected_num_list += after_my_number
        num_list = corrected_num_list

    return num_list



def main() -> None:
    with open("input") as f:
        day_input = f.read().strip()

    orders_dict,  numbers_list = parse(day_input)

    incorrect_numbers_list = [
        num_list
        for num_list in numbers_list
        if not is_num_list_ordered(num_list, orders_dict)
    ]

    correct_numbers_list = []
    for i, num_list in enumerate(incorrect_numbers_list):
        print(f"{i}/{len(incorrect_numbers_list)}")
        new_num_list = correct_num_list(num_list, orders_dict)
        correct_numbers_list.append(new_num_list)
        # if is_num_list_ordered(new_num_list, orders_dict):
        #     print(f"✅ {num_list}")
        # else:
        #     print(f"🛑 {num_list}")

    middle_numbers = [int(num_list[int((len(num_list)-1)/2)]) for num_list in correct_numbers_list]
    print(sum(middle_numbers))


if __name__ == "__main__":
    main()
