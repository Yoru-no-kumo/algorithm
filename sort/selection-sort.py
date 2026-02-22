import random
from copy import deepcopy
from typing import List


def main() -> None:

    def maximum_selection_sort(arr: List[int]) -> int:

        compare_cnt: int = 0

        for li in range(random_list_length - 1, 0, -1):
            max_idx = li

            for i in range(li):

                if arr[max_idx] < arr[i]:
                    max_idx = i
                compare_cnt += 1

            arr[li], arr[max_idx] = arr[max_idx], arr[li]

        return compare_cnt

    def minimum_selection_sort(arr: List[int]) -> int:

        compare_cnt = 0

        for li in range(random_list_length - 1):
            min_idx = li

            for i in range(li + 1, random_list_length):

                if arr[min_idx] > arr[i]:
                    min_idx = i
                compare_cnt += 1

            arr[li], arr[min_idx] = arr[min_idx], arr[li]

        return compare_cnt

    select_run_solt = int(input("最大値ソート: 1, 最小値ソート: 2, 両方: 3\n"))
    random_list_length: int = int(input())

    random_numbers1 = random.sample(range(1, random_list_length + 1), random_list_length)

    if select_run_solt == 1:
        print(f"ソート前: {random_numbers1}")
        maximum_swap_count = maximum_selection_sort(random_numbers1)
        print(f"最大値ソート比較: {maximum_swap_count}回")
        print(f"最大値ソート結果: {random_numbers1}")
    elif select_run_solt == 2:
        print(f"ソート前: {random_numbers1}")
        minimum_swap_count = minimum_selection_sort(random_numbers1)
        print(f"最小値ソート比較: {minimum_swap_count}回")
        print(f"最小値ソート結果: {random_numbers1}")
    elif select_run_solt == 3:
        random_numbers2 = deepcopy(random_numbers1)
        print(f"最大値ソート前: {random_numbers1}")
        print(f"最小値ソート前: {random_numbers2}")
        maximum_swap_count = maximum_selection_sort(random_numbers1)
        minimum_swap_count = minimum_selection_sort(random_numbers2)
        print(f"最大値ソート比較: {maximum_swap_count}回")
        print(f"最大値ソート結果: {random_numbers1}")
        print(f"最小値ソート比較: {minimum_swap_count}回")
        print(f"最小値ソート結果: {random_numbers2}")


main()
