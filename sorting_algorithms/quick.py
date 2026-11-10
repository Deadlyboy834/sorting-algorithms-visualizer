from visualizer.visualizer import plot_bar_graph
from random import randint as r
from utils import with_repr

@with_repr("QuickSort")
def quicksort(data: list[int]) -> None:
    plot_bar_graph(data)
    stack: list[tuple[int, int]] = [(0, len(data) - 1)]

    def swap(index1: int, index2: int) -> None:
        data[index1], data[index2] = data[index2], data[index1]

    while True:
        if len(stack) == 0:
            plot_bar_graph(data)
            break

        left: int
        right: int

        left, right = stack.pop()

        left_pointer: int = left - 1
        swap(r(left, right), right)
        plot_bar_graph(data)

        pivot: int = data[right]

        for traveler in range(left, right):
            if pivot > data[traveler]:
                left_pointer += 1
                swap(left_pointer, traveler)
                plot_bar_graph(data)

        pivot_id: int = left_pointer + 1
        swap(pivot_id, right)

        if pivot_id - 1 > left:
            stack.append((left, pivot_id - 1))

        if pivot_id + 1 < right:
            stack.append((pivot_id + 1, right))

        plot_bar_graph(data)