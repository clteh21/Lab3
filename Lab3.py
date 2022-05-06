print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    for i in range(n):
        if type(arr[i])!= int:
            p=0
            return 3
        else:
            p=1

    if n == 10 and p == 1:
        # Traverse through all array elements
        for i in range(n - 1):
            # range(n) also work but outer loop will
            # repeat one time more than needed.

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                if sorting_order == SORT_ASCENDING:
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]


                if sorting_order == SORT_DESCENDING:
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

    else:
        if n>10 and p == 1:
            return 1
        if n<10 and n>0 and p == 1:
            return 2
        if n==0:
            return 0


    return arr_result

def main():

    arr = get_user_input()

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in ascending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)

    print("The average value: ")
    result = calc_average(arr)
    print(result)

def get_user_input():
    array = []

    # number of elements as input
    n = int(input("Enter number of elements : "))

    # iterating till the range
    for i in range(0, n):
        list = input()
        array.append(list)

    return array

def calc_average(arr):
    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)
    p = 0

    for i in range(n):
        p = p + arr[i]
        average = p/n

    return average

if __name__ == "__main__":
    main()


