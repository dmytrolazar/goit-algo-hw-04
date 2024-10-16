import copy
import random
import timeit

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

numbers1 = [random.randint(1,10) for _ in range(10000)]
numbers2 = [random.randint(1,100) for _ in range(10000)]
numbers3 = [random.randint(1,1000) for _ in range(10000)]
numbers4 = [random.randint(1,10000) for _ in range(10000)]
numbers5 = [i for i in range(10000)]
print(f"Сортування набору даних 1 вставками зайняло {timeit.timeit(lambda: insertion_sort(copy.copy(numbers1)), number=1)} секунд.")
print(f"Сортування набору даних 2 вставками зайняло {timeit.timeit(lambda: insertion_sort(copy.copy(numbers2)), number=1)} секунд.")
print(f"Сортування набору даних 3 вставками зайняло {timeit.timeit(lambda: insertion_sort(copy.copy(numbers3)), number=1)} секунд.")
print(f"Сортування набору даних 4 вставками зайняло {timeit.timeit(lambda: insertion_sort(copy.copy(numbers4)), number=1)} секунд.")
print(f"Сортування набору даних 5 вставками зайняло {timeit.timeit(lambda: insertion_sort(copy.copy(numbers5)), number=1)} секунд.")
print(f"Сортування набору даних 1 злиттям зайняло {timeit.timeit(lambda: merge_sort(copy.copy(numbers1)), number=1)} секунд.")
print(f"Сортування набору даних 2 злиттям зайняло {timeit.timeit(lambda: merge_sort(copy.copy(numbers2)), number=1)} секунд.")
print(f"Сортування набору даних 3 злиттям зайняло {timeit.timeit(lambda: merge_sort(copy.copy(numbers3)), number=1)} секунд.")
print(f"Сортування набору даних 4 злиттям зайняло {timeit.timeit(lambda: merge_sort(copy.copy(numbers4)), number=1)} секунд.")
print(f"Сортування набору даних 5 злиттям зайняло {timeit.timeit(lambda: merge_sort(copy.copy(numbers5)), number=1)} секунд.")
print(f"Сортування набору даних 1 алгоритмом Timsort зайняло {timeit.timeit(lambda: sorted(copy.copy(numbers1)), number=1)} секунд.")
print(f"Сортування набору даних 2 алгоритмом Timsort зайняло {timeit.timeit(lambda: sorted(copy.copy(numbers2)), number=1)} секунд.")
print(f"Сортування набору даних 3 алгоритмом Timsort зайняло {timeit.timeit(lambda: sorted(copy.copy(numbers3)), number=1)} секунд.")
print(f"Сортування набору даних 4 алгоритмом Timsort зайняло {timeit.timeit(lambda: sorted(copy.copy(numbers4)), number=1)} секунд.")
print(f"Сортування набору даних 5 алгоритмом Timsort зайняло {timeit.timeit(lambda: sorted(copy.copy(numbers5)), number=1)} секунд.")
