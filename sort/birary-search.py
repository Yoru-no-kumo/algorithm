from typing import List


def main() -> None:

    arr: List[int] = [x for x in range(1, pow(10, 3) + 1)]
    target: int = int(input())

    def binary_search(arr: List[int], target: int) -> int:
        start: int = 0
        end: int = len(arr) - 1

        while start <= end:
            idx: int = int((start + end) / 2)

            if target == arr[idx]:
                return idx
            elif target > arr[idx]:
                start = idx + 1
            elif target < arr[idx]:
                end = idx - 1

        return -1

    result_idx: int = binary_search(arr, target)
    print(arr[result_idx])


main()
