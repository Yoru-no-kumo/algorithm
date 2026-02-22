import time
from typing import List


def main() -> None:
    n: int = int(input())

    def fibonacci_recursive(n: int) -> int:
        if n == 1 or n == 2:
            return 1
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

    fibo_list: List[int] = [-1 for _ in range(n)]
    fibo_list[0] = 1
    fibo_list[1] = 1

    def fibonacci_memoization(n: int) -> int:
        if fibo_list[n - 1] != -1:
            return fibo_list[n - 1]

        fibo_list[n - 1] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
        return fibo_list[n - 1]

    start_without_memoiation: float = time.time()
    result_without_memoiation: int = fibonacci_recursive(n)
    end_without_memoiation: float = time.time()

    start_with_memoiation: float = time.time()
    result_with_memoiation: int = fibonacci_memoization(n)
    end_with_memoiation: float = time.time()

    print(f"{result_without_memoiation}, {end_without_memoiation-start_without_memoiation}s")
    print(f"{result_with_memoiation}, {end_with_memoiation-start_with_memoiation}s")


if __name__ == "__main__":
    main()
