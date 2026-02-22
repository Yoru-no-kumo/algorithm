from typing import List


def main() -> None:
    n: int = int(input())
    matrix: List[List[int]] = [[1 for _ in range(n)] for _ in range(n)]
    is_visited: List[bool] = [False for _ in range(n)]
    cnt = 0

    def dfs(depth: int) -> None:
        nonlocal cnt
        if depth == n:
            cnt += 1
            return

        for i in range(n):
            if check_chess(depth, i) and not is_visited[i]:
                matrix[depth][i] = 0
                is_visited[i] = True

                dfs(depth + 1)

                matrix[depth][i] = 1
                is_visited[i] = False

    def check_chess(depth: int, idx: int) -> bool:
        left = idx - 1
        right = idx + 1
        for dep in range(depth - 1, -1, -1):

            if left >= 0:

                if matrix[dep][left] == 0:
                    return False
                left -= 1

            if right < n:

                if matrix[dep][right] == 0:
                    return False
                right += 1

        return True

    dfs(0)
    print(cnt)


main()
