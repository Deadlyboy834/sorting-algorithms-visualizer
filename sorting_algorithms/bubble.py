from utils import with_repr
from visualizer.visualizer import plot_bar_graph

@with_repr("Bubble Sort")
def bubble_sort(data :list[int]) -> None:
    def swap(index1: int, index2: int):
        temp: int = data[index1]
        data[index1] = data[index2]
        data[index2] = temp

    plot_bar_graph(data)

    while True:
        has_swap: bool = False

        for index in range(len(data) - 1):
            if data[index] >= data[index + 1]:
                swap(index, index + 1)
                has_swap = True
                plot_bar_graph(data)

        if not has_swap:
            break