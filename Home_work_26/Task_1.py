from random import sample


a = sample(range(1, 15), 10)
a.sort()


def binary_search_recursive(lst: list, element: int, low: int, high: int):  # O(log n)
    if low > high:
        return None

    mid = (low + high) // 2

    if lst[mid] == element:
        return mid
    elif lst[mid] > element:
        return binary_search_recursive(lst, element, low, mid - 1)
    else:
        return binary_search_recursive(lst, element, mid + 1, high)


def fibonacci_search(lst, element):
    size = len(lst)
    start = -1

    fib_prev = 0
    fib_curr = 1
    fib_next = 1
    while fib_next < size:
        fib_prev = fib_curr
        fib_curr = fib_next
        fib_next = fib_curr + fib_prev

    while fib_next > 1:
        index_ = min(start + fib_prev, size - 1)
        if lst[index_] < element:
            fib_next = fib_curr
            fib_curr = fib_prev
            fib_prev = fib_next - fib_curr
            start = index_
        elif lst[index_] > element:
            fib_next = fib_prev
            fib_curr = fib_curr - fib_prev
            fib_prev = fib_next - fib_curr
        else:
            return index_
    if fib_curr and lst[size - 1] == element:
        return size - 1
    return None


if __name__ == '__main__':
    search_element = int(input('Enter number from 1 - 15 >>> '))
    low_i, high_i = 0, len(a) - 1
    index = binary_search_recursive(a, search_element, low_i, high_i)
    index_2 = fibonacci_search(a, search_element)

    print(a, '\n')

    if index is not None:
        print(f'Binary search found Element "{search_element}" at index: {index}')
    else:
        print(f'Binary search not found Element "{search_element}" in list!')

    if index_2 is not None:
        print(f'Fibonacci search found Element "{search_element}" at index: {index_2}')
    else:
        print(f'Fibonacci search not found Element "{search_element}" in list!')
        
        
