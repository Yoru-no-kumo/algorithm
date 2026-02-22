import random


def main() -> None:
    max_num: int = 1000
    random_numbers = random.sample(range(1, max_num + 1), max_num)

    for li in range(max_num - 1, 0, -1):
        for i in range(li):
            if random_numbers[i] > random_numbers[i + 1]:
                random_numbers[i], random_numbers[i + 1] = random_numbers[i + 1], random_numbers[i]

    print(random_numbers)


main()
