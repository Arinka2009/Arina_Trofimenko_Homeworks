from typing import List, Tuple


# We assume that all lists passed to functions are the same length N

def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:  # Цикл повторяется по каждому элементу ровно один раз, что занимает время O(n)
        if el_first_list in second_list:  # in для проверки наличия элемента в second_list, в худшем случае займет
            # O(n) времени
            res.append(el_first_list)  # append добавляет элемент в список результатов, займет O(1) время
    return res  # O(n*n + 1) = O(n^2)


def question2(n: int) -> int:
    for _ in range(10):  # цикл с фиксированным числом итераций (10)
        n **= 3  # Единственная операция внутри цикла — операция с постоянным временем (возведение n в степень)
    return n  # O(1) - временная сложность цикла постоянна и не зависит от входного размера n


def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]  # копирование списка длинной N -  O(n)
    for el_second_list in second_list:  # Цикл повторяется по каждому элементу second_list, что занимает время O(n)
        flag = False
        for check in temp:  # Цикл сравнивает каждый элемент списка "temp" с элементом из second_list.
            # Каждый раз, при несовпадении элементов, кол-во элементов в списке "temp" будет увеличиваться на 1.
            # Т.е в худшем случае, если два списка абсолютно разные и одинаковой длинны, то O(2n)
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(el_second_list)
    return temp  # O(n) + O(n*2n) --> O(n+2n^2) --> сокращаю константу 2: O(n+n^2) --> убираю слагаемое "n": O(n^2), т.к.
    # по правилу неважной сложности, если в O есть сумма, то нас интересует самое быстрорастущее слагаемое


def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:  # Функция выполняет итерацию по всему списку один раз, кол-во выполняемых операций
        # пропорционально длинне входного списка --> O(n)
        if el > res:
            res = el
    return res


def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):  # O(n) - кол-во итераций пропорционально значению n
        for j in range(n):  # O(n)
            res.append((i, j))
    return res  # временная сложность функции: O(n*n) --> O(n^2)


def question6(n: int) -> int:
    while n > 1:  # В цикле while значение n делится на 2 на каждой итерации, пока оно не станет меньше или равным 1.
        n /= 2  # кол-во итераций = сколько раз нужно значение "n" делить на 2, чтоб получить 1 или меньше.
    return n  # Таким образом, O(log2(n)) --> O(log(n))
