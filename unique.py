from collections.abc import Generator
from typing import Any

from gen_random import gen_random


class Unique(object):


    def __init__(self, items: list[Any] | Generator[Any], **kwargs):

        self.items = iter(items)

        self.ignore_case: bool = kwargs.get('ignore_case', False)

        self.seen: set[Any] = set()


    def __next__(self):

        while True:

            item = next(self.items)

            if self.ignore_case:

                if isinstance(item, str):

                    if item.lower() not in self.seen:

                        self.seen.add(item.lower())

                        return item

                else:

                    if item not in self.seen:

                        self.seen.add(item)

                        return item

            else:

                if item not in self.seen:

                    self.seen.add(item)

                    return item


    def __iter__(self):

        return self

def main():
    print("--- Тест 1: Строки")
    words = ['яблоко', 'ЯБЛОКО', 'банан', 'яблоко', 'Банан']

    print(f"Вход: {words}")
    
    print("Без учета регистра (ignore_case=False):")

    for word in Unique(words, ignore_case=False):
        print(word)
        
    print("\nС учетом регистра (ignore_case=True):")

    for word in Unique(words, ignore_case=True):
        print(word)


    print("\n--- Тест 2: Числа")
    numbers = [1, 2, 2, 3, 1, 4, 3, 5]

    print(f"Вход: {numbers}")
    
    print("Только уникальные числа:")
    for num in Unique(numbers):
        print(num)


    print("\n--- Тест 3: Итератор (генератор) ---")
    # Используем генератор случайных чисел из прошлого задания.
    generator_nums = gen_random(num_count=10, begin=1, end=5)
    
    print("Уникальные числа из случайного генератора:")
    for num in Unique(generator_nums):
        print(num)


if __name__ == '__main__':
    main()
