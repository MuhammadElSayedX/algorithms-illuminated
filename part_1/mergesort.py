class Mergesort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        return self._sort(self.array)

    def _sort(self, array):
        if len(array) == 1:
            return array

        mid = len(array) // 2
        left = self._sort(array[:mid])
        right = self._sort(array[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        len_left = len(left)
        len_right = len(right)

        result = []

        left_index = 0
        right_index = 0

        while left_index < len_left and right_index < len_right:
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        if left_index < len_left:
            result.extend(left[left_index:])
        else:
            result.extend(right[right_index:])

        return result


def main():
    array = [1, 3, 5, 2, 4, 6]
    print(list(Mergesort(array).sort()))


if __name__ == "__main__":
    main()
