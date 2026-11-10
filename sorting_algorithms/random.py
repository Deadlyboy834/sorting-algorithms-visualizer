from utils import with_repr
from visualizer.visualizer import plot_bar_graph
from random import randint as r

@with_repr("Random Sort")
def random_sort(data: list[int]) -> None:
    plot_bar_graph(data)

    data_length: int = len(data)

    def is_sorted() -> bool:
        return all(data[i] < data[i + 1] for i in range(data_length - 1))

    def randomize_list() -> None:
        for i in range(data_length - 1, 0, -1):
            j: int = r(0, i)

            data[i], data[j] = data[j], data[i]

    while not is_sorted():
        randomize_list()
        plot_bar_graph(data)