import asyncio
import collections
import math
from functools import cache


def find_duplicates(array: list) -> str:
    """
    Write a python function that finds the duplicate items in any given array.
    :param array: list
    :return: The list with the duplicate items
    """
    # Easy way (less performance)
    method_one = [
        item for item, count in collections.Counter(array).items() if count > 1
    ]

    # Faster code
    helper = set()
    method_two = set(x for x in array if x in helper or helper.add(x))

    assert method_one == list(method_two)

    return f"Duplicate items -> {method_one}"


async def printer(array: list) -> None:
    """
    Async function to print elements using specific timings:
    ex: for [“a”,” b, “c, “d”], “a” is printed in 1 sec, “b” is printed in 2
    seconds, “c” is printed in 4 seconds, ...
    :param array: list
    """
    array.sort()
    prev_idx = None
    for idx, item in enumerate(array):
        if idx < 2:
            idx += 1
        elif not prev_idx:
            prev_idx = idx

        if prev_idx:
            idx = prev_idx + prev_idx
            prev_idx = idx

        print(f"Printing using {idx} seconds as timing")
        await asyncio.sleep(idx)
        print(f"Value -> {item}")


def exec_async_func(function):
    """
    Executor to call an async function
    :param function: def(params)
    :return: return from passed function
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(function)
    loop.close()


def multiple_brackets(str_item: str) -> str:
    """
    Write an efficient method that tells us whether or not an input string brackets
    ("{", "}", "(", ")", "[", "]") opened and closed properly.
    Example: “{[]}” => true, “{(])}” => false, “{([)]}” => false
    :param str_item: str
    :return: Result from the analysis
    """
    fail = False
    all_brackets = ["(", "}", "]", "[", ")", "{"]
    close_brackets = {")": "(", "]": "[", "}": "{"}
    found_open_brackets = []

    for item in str_item:
        # check if some item is in all of the brackets and is a open one
        if item in all_brackets and item not in close_brackets:
            found_open_brackets.append(item)
        elif item in all_brackets:
            # checking if this close bracket was open before
            if len(found_open_brackets) == 0:
                fail = True
                break
            else:
                # removing the last open bracket
                val = found_open_brackets.pop()
                # checking if the bracket is correct in relation to the item that closes
                if val != close_brackets[item]:
                    fail = True
                    break

    return f" '{str_item}' => {True if len(found_open_brackets) == 0 and not fail else False}"


@cache
def two_egg_drop(floor: int) -> int:
    """
    A building has 100 floors. One of the floors is the highest floor an egg can be dropped from
    without breaking. If an egg is dropped from above that floor, it will break. If it is dropped
    from that floor or below, it will be completely undamaged and you can drop the
    egg again. Given two eggs, find the highest floor an egg can be dropped from without breaking,
    with as few drops as possible on the worst-case scenario.
    :param floor: int
    :return: result of the solution
    """
    if floor == 1 or floor == 2:
        return floor
    ans = math.inf
    for i in range(1, floor + 1):
        ans = min(ans, 1 + max(i, two_egg_drop(floor - i - 1)))
    return ans


def animate_text(text: str) -> None:
    """
    Write the code that animates “Zeno's Paradox of Achilles and the Tortoise” on an
    interface(terminal for python)(we would like to see the paradox demonstrated).
    :param text: str
    :return: Output animated
    """
    lines = text.split(" ")

    from time import sleep
    import sys

    for line in lines:  # for each line of text (or each message)
        for c in line:  # for each character in each line
            print(c, end='')  # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            sleep(0.1)  # wait a little to make the effect look good.
        print('')


def get_max_value(carrot_types: list, max_capacity: int) -> int:
    """
    Think that you have an unlimited number of carrots, but a limited number of carrot types. Also,
    you have one bag that can hold a limited weight. Each type of carrot has a weight and a price.
    Write a function that takes carrotTypes and capacity and return the maximum value the bag can
    hold.
    :param carrot_types: list
    :param max_capacity: Result of the bag's maximum capacity
    :return:
    """
    val = [item.get("price") for item in carrot_types]
    wt = [item.get("kg") for item in carrot_types]
    n = len(val)

    matrix = [[0 for _ in range(max_capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(max_capacity + 1):
            if i == 0 or w == 0:
                matrix[i][w] = 0
            elif wt[i - 1] <= w:
                matrix[i][w] = max(
                    val[i - 1] + matrix[i - 1][w - wt[i - 1]], matrix[i - 1][w]
                )
            else:
                matrix[i][w] = matrix[i - 1][w]

    return matrix[n][max_capacity]


if __name__ == "__main__":
    print(find_duplicates([1, 2, 3, 2, 1, 5, 6, 5, 5, 5]))
    exec_async_func(printer(["a", "b", "c", "d", "e", "f"]))
    print(multiple_brackets("{[]}"))
    print(multiple_brackets("{(])}"))
    print(two_egg_drop(100))
    carrotTypes = [
        {"kg": 5, "price": 100},
        {"kg": 7, "price": 150},
        {"kg": 3, "price": 70},
    ]
    capacity = 36
    print(get_max_value(carrotTypes, capacity))
    animate_text("Zeno's Paradox of Achilles and the Tortoise")
