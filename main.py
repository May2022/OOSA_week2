from searchObject import dataSorter
import matplotlib.pyplot as plt

def main():
    data_sorter_1 = dataSorter(10)
    sorted_array = data_sorter_1.sortArray()
    # print(type(sorted_array))
    min = sorted_array.min()
    max = sorted_array.max()
    print(data_sorter_1.sortArr)
    index = data_sorter_1.binary_sort(sorted_array[2], 0, sorted_array.shape[0] - 1)
    plt.xlabel('x')
    plt.ylabel('y')
    x = []
    for i in range(0, sorted_array.shape[0]):
        x.append(i)
    print(x)
    plt.plot(x, sorted_array)
    plt.vlines(index, min, max, colors='black')
    plt.show()
    print(sorted_array[2])

    print(index)


if __name__ == '__main__':
    main()
