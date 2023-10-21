class CountInv:
    def __init__(self, array):
        self.array = array

    def count(self):
        return self._sort(self.array)

    def sort(self):
        return self._sort(self.array)[0]

    def _sort(self, array) -> tuple:
        if len(array) == 1:
            return array, 0

        mid = len(array) // 2
        left, left_split_inv = self._sort(array[:mid])
        right, right_split_inv = self._sort(array[mid:])
        combined, combined_split_inv = self.merge(left, right)

        return combined, (left_split_inv + right_split_inv + combined_split_inv)

    @staticmethod
    def merge(left, right):
        len_left = len(left)
        len_right = len(right)

        result = []

        left_index = 0
        right_index = 0
        split_inv = 0

        while left_index < len_left and right_index < len_right:
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

                split_inv += len_left - left_index

        if left_index < len_left:
            result.extend(left[left_index:])
        else:
            result.extend(right[right_index:])

        return result, split_inv


def main():
    # read from file and convert to list of ints
    with open("count_inv_test.txt", "r") as f:
        array = [int(line) for line in f]

    print(list(CountInv(array).count()))


if __name__ == "__main__":
    main()
