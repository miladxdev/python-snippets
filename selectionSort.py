# ascending selection sort

list = [6, 5, 4, 3, 2, 1]


def selection_sort(arr):
    for n in range(len(arr)-1):
        min = arr[n]
        print(n+1, arr)
        print('-----------------')
        for i in range(n+1, len(arr)):
            if arr[i] < min:
                arr[i], arr[n] = arr[n], arr[i]
                print('*', arr)
            else:
                print('#', 'no changes')

        print('\n')


selection_sort(list)


def optimized_selection_sort(arr):
    swapped = True
    for n in range(len(arr)-1):
        if swapped:
            swapped = False
            min = arr[n]
            for i in range(n+1, len(arr)):
                if arr[i] < min:
                    arr[i], arr[n] = arr[n], arr[i]
                    swapped = True
    return arr


print(optimized_selection_sort(list))
