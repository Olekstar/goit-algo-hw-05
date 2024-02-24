def binary_search(arr, value):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        # Знайдено шукане значення
        if arr[mid] == value:
            upper_bound = arr[mid]
            break
        # Шукане значення менше за серединне, звужуємо до лівої частини
        elif arr[mid] < value:
            left = mid + 1
        # Шукане значення більше за серединне, звужуємо до правої частини
        else:
            right = mid - 1
            upper_bound = arr[mid]  # Запам'ятовуємо поточний елемент як верхню межу

    # Якщо не знайдено точного співпадіння та верхню межу, значення більше за всі елементи масиву
    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]

    return iterations, upper_bound

# Приклад використання:
arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
value = 3.5
result = binary_search(arr, value)
print(f"Ітерацій: {result[0]}, Верхня межа: {result[1]}")
