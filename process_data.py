
import json
import sys
from typing import Any

from cm_timer import cm_timer_1
from gen_random import gen_random
from unique import Unique


def f1(data: list[dict[Any]]) -> list[str]:

    return sorted(list(Unique((job['job-name'] for job in data), ignore_case=True)), key=str.lower)

def f2(data: list[str]) -> list[str]:

    return list(filter(lambda f: str(f).lower().startswith('программист'), data))

def f3(data: list[str]) -> list[str]:

    return list(map(lambda f: f + ' с опытом Python', data))


def f4(data: list[dict[Any]], sorted_data: list[str]) -> None:

    number_prof = len(sorted_data)

    salaries = gen_random(number_prof, 100000, 200000)

    res = zip(sorted_data, salaries)

    for item1, item2 in res:

        print(f"{item1}, зарплата {item2} руб.")

def main():

    try:

        path = sys.argv[1]

    except IndexError:

        print('Небходимо передать аргумент путь к файлу (например: data_light.json)')

    except Exception as e:

        print(f'Неизвестная ошибка {e}')

    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    with cm_timer_1():
        f4(data, f3(f2(f1(data))))

if __name__ == '__main__':
    main()
