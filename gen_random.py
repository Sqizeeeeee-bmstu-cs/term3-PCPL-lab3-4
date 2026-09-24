import random
from collections.abc import Generator


def gen_random(num_count: int, begin: int, end: int) -> Generator[int, None, None]:

    for _ in range(num_count):

        yield random.randint(begin, end)

def main():

    count = 10
    low = 10
    high = 50

    print(f"Генерируем {count} случайных чисел от {low} до {high}:")
    
    my_generator = gen_random(count, low, high)
    
    generated_count = 0
    for number in my_generator:
        print(f"Получено число: {number}")
        
        assert low <= number <= high, f"Ошибка: число {number} вышло за границы"
        
        generated_count += 1
        
    assert generated_count == count, f"Ошибка: ожидалось {count} чисел, но получено {generated_count}"
    
    print("Тест пройден")


if __name__ == '__main__':
    main()