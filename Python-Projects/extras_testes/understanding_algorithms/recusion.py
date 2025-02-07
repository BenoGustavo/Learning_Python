from copy import deepcopy

def sum(array:list[int]) -> int | float:

    if len(array) == 1:
        return array.pop()
    
    return array.pop() + sum(array)

def lenght(array: list) -> int:
    try:
        array[0]
    except(IndexError):
        return 0

    return 1 + lenght(array[:-1])

def major_value(array:list, max : int = 0) -> int | float:
    if len(array) == 0:
        return max

    if array[0] > max :
        return major_value(array[1:],array[0])

    return major_value(array[1:],max)

def binary_search(arr: list[int], value : int, value_index : int = 0) -> int:
    index = round(len(arr) / 2)

    if arr[index] == value:
        if value_index < 0:
            return (value_index + index) * -1
        return value_index + index

    if arr[index] < value:
        return binary_search(arr[index:], value, value_index + index)
    return binary_search(arr[:index], value, value_index - index)

def quick_sort(arr : list[int| float]) -> list[int | float]:
    if len(arr) < 2:
        return arr
    pivo = arr[0]
    lowers = [i for i in arr[1:] if i <= pivo]
    majors = [i for i in arr[1:] if i > pivo]
    return quick_sort(lowers) + [pivo] + quick_sort(majors)

if __name__ == "__main__":
    ARR = [1,2,3,4,5,6,56]

    print(ARR[:3])
    print(f"Sum: of {ARR} {sum(deepcopy(ARR))}")
    print(f"length of {ARR} {lenght(deepcopy(ARR))}")
    print(f"Major value of {ARR} {major_value(deepcopy(ARR))}")
    print(f"Binary search {ARR} {deepcopy(binary_search(ARR,3))}")
    print(f"Quicksort algorithm {[10,5,2,3]} {quick_sort([10,5,2,3])}")