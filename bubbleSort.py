# Bobble sorting (Asending order)

#  in the most inefficient approach, bubble sort goes through n-1
#  iteration, looking at n-1 pairs of adjacent elements. this
#  gives in the time complexity O(n)^2


list = [1, 2, 3, 4, 6, 5]


def bubbleSort(list):
    swapp = True
    for n in range(len(list)-1):
        if swapp:
            swapp = False
            print(n+1, '---------------')
            for i in range(len(list)-1-n):
                if list[i] < list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
                    swapp = True
                    print(list)
                else:
                    print("no change")
            print('')
        else:
            break
    print('Sorted list:', list)


bubbleSort(list)
