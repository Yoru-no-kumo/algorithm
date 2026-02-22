import random
from typing import List


def main() -> None:
    max_num: int = 100
    random_numbers = random.sample(range(1, max_num + 1), max_num)

    def merge_sort(random_numbers: List[int], low: int, high: int) -> None:
        if low >= high:
            return

        mid: int = (low + high) // 2

        merge_sort(random_numbers, low, mid)
        merge_sort(random_numbers, mid + 1, high)
        merge(random_numbers, low, mid, high)

    def merge(random_numbers: List[int], low: int, mid: int, high: int) -> None:

        tmp = [0] * (high - low + 1)
        i: int = low
        j: int = mid + 1
        k: int = 0

        while i <= mid and j <= high:
            if random_numbers[i] > random_numbers[j]:
                tmp[k] = random_numbers[j]
                j += 1
            else:
                tmp[k] = random_numbers[i]
                i += 1
            k += 1

        while i <= mid:
            tmp[k] = random_numbers[i]
            i += 1
            k += 1
        while j <= high:
            tmp[k] = random_numbers[j]
            j += 1
            k += 1

        for t in tmp:
            random_numbers[low] = t
            low += 1

    merge_sort(random_numbers, 0, len(random_numbers) - 1)
    print(random_numbers)


main()
