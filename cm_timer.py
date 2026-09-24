
import time
from collections.abc import Generator
from contextlib import contextmanager
from typing import Any


class cm_timer_1():

    def __init__(self):

        self.start_time = 0.0

    def __enter__(self) -> Any:

        self.start_time = time.time()

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:

        end_time = time.time()

        elapsed_time = end_time - self.start_time

        print(f'time: {elapsed_time}')

@contextmanager
def cm_timer_2() -> Generator[None, Any, None]:

    start_time = time.time()

    try:

        yield

    finally:

        end_time = time.time()

        elapsed_time = end_time - start_time

        print(f'time: {elapsed_time}')


def main():

    print("--- Тест 1: Класс cm_timer_1")
    with cm_timer_1():
        time.sleep(1.5)

    print("\n--- Тест 2: Функция cm_timer_2")
    with cm_timer_2():
        time.sleep(2.0)

if __name__ == '__main__':
    main()

