def part(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

    tmp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = tmp
    return i + 1
    # i = low
    # j = high - 2
    # while i < j:
    #     while arr[i] <= pivot:
    #         i += 1
    #     while arr[j] > pivot:
    #         j -= 1
    #
    #     if i < j:
    #         tmp = arr[i]
    #         arr[i] = arr[j]
    #         arr[j] = tmp
    #
    # tmp = arr[low]
    # arr[low] = arr[j]
    # arr[j] = tmp
    # return j


def quickSort(arr, low, high):
    if low < high:
        pivot = part(arr, low, high)

        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)


def main():
    arr = [44, 88, 77, 22, 66, 11, 99, 55, 0, 33]
    # arr = [1, 2, 3, 10, 1, 2, 3]
    print(len(arr))
    quickSort(arr, 0, len(arr) - 1)
    print(arr)


if __name__ == "__main__":
    main()
