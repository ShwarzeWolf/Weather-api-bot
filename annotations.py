from typing import Any, List, Callable, Optional, Union
# int float complex bool str
# List[str]


def triple(num: Union[int, str]) -> Union[int, str]:
    """Returns number multiplied by 3"""
    # Написать отдельно обработку типов
    return num * 3


print(triple(4))
print(triple("some_string"))


def process_strings(strings: List[str], func: Callable) -> None:
    for string in strings:
        print(func(string))


process_strings(["hello", "world"], str.capitalize)


def optional_example(val: int) -> Optional[int]:
    if val % 2 == 0:
        return val

    return None


class Bird:
    pass


class Duck(Bird):
    def do_something(self):
        print('quack')


def catch_bird(bird: Bird) -> None:
    pass


def catch_duck(duck: Duck) -> None:
    duck.do_something()


bird = Bird()
duck = Duck()

catch_bird(bird)
catch_bird(duck)

catch_duck(bird)
catch_duck(duck)


# int, float, complex
