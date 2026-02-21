from copy import deepcopy
import random
from typing import List


def main() -> None:
    
    max_num: int = int(input())

    random_numbers1 = random.sample(range(1, max_num + 1), max_num)
    random_numbers2 = deepcopy(random_numbers1)

    def maximum_selection_sort(arr: List[int]) -> None:

        for li in range(max_num - 1, 0, -1):
            for i in range(li):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]

    def minimum_selection_sort(arr: List[int]) -> None:
        for li in range(max_num - 1):
            for i in range(li + 1, max_num):
                if arr[li] > arr[i]:
                    arr[li], arr[i] = arr[i], arr[li]

    maximum_selection_sort(random_numbers1)
    minimum_selection_sort(random_numbers2)
    print(random_numbers1)
    print(random_numbers2)

main()
