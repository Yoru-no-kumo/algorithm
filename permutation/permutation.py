from typing import List


def main() -> None:

    n, m = [int(x) for x in input().split(" ")]
    arr: List[str] = input().split(" ")

    is_visited: List[bool] = [False] * n
    comb_list: List[str] = [""] * m

    def permutation_with_visit_check(arr: List[str], cnt: int = 0) -> List[str]:
        results: List[str] = []

        if cnt == m:
            return [" ".join(comb_list)]

        for i in range(n):

            if not is_visited[i]:
                comb_list[cnt] = arr[i]
                is_visited[i] = True
                results.extend(permutation_with_visit_check(arr, cnt + 1))
                is_visited[i] = False

        return results

    result = permutation_with_visit_check(arr)
    print("\n".join(result))


if __name__ == "__main__":
    main()
