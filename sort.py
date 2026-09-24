

def sort_w_lambda(items: list[int]) -> None: 
    items.sort(key=lambda x: abs(x))

def sort_without_lamdba(items: list[int]) -> None:
    items.sort(key=abs)

def custom_bubble_sort_without_lamdba(items: list[int]) -> None:

    for _ in range(len(items)):
        for j in range(len(items) - 1):

            if (abs(items[j]) > abs(items[j + 1])):

                items[j], items[j + 1] = items[j + 1], items[j]

def custom_quicksort_inplace(items: list[int], start: int = 0, end: int = None) -> None:
    if end is None:
        end = len(items) - 1
        
    if start >= end:
        return

    pivot_abs = abs(items[end])
    i = start
    
    for j in range(start, end):
        if abs(items[j]) < pivot_abs:

            items[i], items[j] = items[j], items[i]
            i += 1
            
    items[i], items[end] = items[end], items[i]

    custom_quicksort_inplace(items, start, i - 1)
    custom_quicksort_inplace(items, i + 1, end)

def main():

    original_data = [3, -5, 1, 0, -2, 5, -1]
    print(f"Исходный список: {original_data}\n")

    data1 = original_data.copy()
    sort_w_lambda(data1)
    print(f"Результат sort_w_lambda: {data1}")

    data2 = original_data.copy()
    sort_without_lamdba(data2)
    print(f"Результат sort_without_lamdba: {data2}")

    data3 = original_data.copy()
    custom_bubble_sort_without_lamdba(data3)
    print(f"Результат custom_bubble_sort_without...: {data3}")

    data4 = original_data.copy()
    custom_quicksort_inplace(data4)
    print(f"Результат custom_quicksort: {data4}")

    if data1 == data2 == data3 == data4:
        print("\n Все реализации работают одинаково.")
    else:
        print("\n Результаты функций отличаются.")

if __name__ == '__main__':
    main()

