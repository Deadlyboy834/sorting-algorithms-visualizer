from utils import with_repr
from visualizer.visualizer import plot_bar_graph

@with_repr("Insertion Sort")
def insertion_sort(data :list[int]) -> None:
    plot_bar_graph(data)

    for index1 in range(1, len(data)):
        for index2 in range(0, index1):
            if data[index2] >= data[index1]:
                data.insert(index2, data.pop(index1))
                plot_bar_graph(data)
                break