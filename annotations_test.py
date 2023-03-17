from typing import List, Callable, Any, Optional


def triple(num: Any) -> Any:
    return num * 3


def square(num: int) -> int:
    return num ** 2


print(square(2))


def process_strings(strings: List[str], func: Callable) -> None:
    for string in strings:
        print(func(string))


process_strings(["hello", "there"], str.capitalize)


def optional_example(val: int) -> Optional[int]:
    if val % 2 == 0:
        return val


print(optional_example(4))
print(optional_example(5))