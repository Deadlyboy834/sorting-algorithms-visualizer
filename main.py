import time
from collections.abc import Callable
from copy import deepcopy

from sorting_algorithms.bubble import bubble_sort
from sorting_algorithms.insertion import insertion_sort
from sorting_algorithms.quick import quicksort
from sorting_algorithms.random import random_sort
from visualizer.visualizer import init_visualizer

ALGORITHMS_LIST: list[Callable] = [bubble_sort, insertion_sort, random_sort, quicksort]
ALGORITHMS_PROMPT: str = f"Choose an algorithm to implement. Choose an integer from 1-{len(ALGORITHMS_LIST)}: "
ALGORITHMS_ERROR_PROMPT: str = f"Please enter an integer from 1-{len(ALGORITHMS_LIST)}"

unsorted_list: list[int] = [42, 7, 89, 23, 56, 12, 94, 31, 68, 3, 77, 15, 84, 50, 91, 6, 38, 62, 27, 49]

def print_sorting_algorithms():
    for i in range(len(ALGORITHMS_LIST)):
        print(f"{i + 1}. {ALGORITHMS_LIST[i]}")

def main() -> None:
    while True:
        print("Enter 'QUIT' to stop")

        print_sorting_algorithms()
        print()

        if (user_choice := input(ALGORITHMS_PROMPT).lower()) == "quit":
            break

        try:
            user_choice: int = int(user_choice)
        except ValueError:
            print(ALGORITHMS_ERROR_PROMPT)
            continue

        if 1 <= user_choice <= 4:
            start_time: float | int = time.perf_counter()

            init_visualizer(deepcopy(unsorted_list))
            current_algorithm: Callable[[list[int]], None] = ALGORITHMS_LIST[user_choice - 1]
            current_algorithm(deepcopy(unsorted_list))

            elapsed_time: float | int = time.perf_counter() - start_time
            print(f"{current_algorithm} finished in {elapsed_time:.2f} seconds.")
            input("Press Enter to return to the main menu...")
            print()
            continue
        else:
            print(ALGORITHMS_ERROR_PROMPT)
            continue

if __name__ == '__main__':
    main()