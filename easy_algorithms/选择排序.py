"""
选择排序:每一轮选择的都是数组中的最小值，添加到新的数组中
"""
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


if __name__ == '__main__':
    print(selectionSort([5, 3, 6, 12, 7, 5]))
