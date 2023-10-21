class Quicksort:
    def __init__(self, array, choose_pivot=lambda array, left, right: array[left]):
        self.array = array
        self.comparisons = 0
        self.choose_pivot = choose_pivot

    def sort(self):
        self._sort(self.array, 0, len(self.array) - 1)
        return self.array

    def _sort(self, array, left, right):
        if left >= right:
            return

        pivot = self.median_of_three(array, left, right)

        array[left], array[pivot] = array[pivot], array[left]

        pivot_index = self.partition(array, left, right)

        self._sort(array, left, pivot_index - 1)
        self._sort(array, pivot_index + 1, right)

    def partition(self, array, left, right):
        self.comparisons += right - left

        pivot = array[left]

        i = left + 1
        for j in range(left + 1, right + 1):
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]
                i += 1

        array[left], array[i - 1] = array[i - 1], array[left]

        return i - 1

    def count(self):
        self._sort(self.array, 0, len(self.array) - 1)
        return self.comparisons

    def median_of_three(self, array, left, right):
        mid = (right + left) // 2

        first = array[left]
        last = array[right]
        middle = array[mid]

        if first < middle < last or last < middle < first:
            return mid

        if middle < first < last or last < first < middle:
            return left

        return right


def main():
    # read from file and convert to list of ints
    with open("quicksort_data.txt", "r") as f:
        array = [int(line) for line in f]

    print(Quicksort(array).count())
    # print(Quicksort(array).sort())


if __name__ == "__main__":
    main()
