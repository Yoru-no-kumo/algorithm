from typing import List


def main() -> None:
    n: int = int(input())

    def fibonacci_recursive(n: int) -> int:
        if n == 1 or n == 2: return 1

        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

    recursive_result: int = fibonacci_recursive(n)

    fibo_list: List[int] = [-1 for _ in range(n)]
    fibo_list[0] = 1
    fibo_list[1] = 1

    def fibonacci_memoization(n: int) -> int:
        if fibo_list[n-1] != -1:
            return fibo_list[n-1]

        fibo_list[n-1] = fibonacci_memoization(n-1) + fibonacci_memoization(n-2)

        return fibo_list[n-1]

    memoization_result: int = fibonacci_memoization(n)
    
    print(memoization_result)
    print(recursive_result)

if __name__ == "__main__":
    main()
