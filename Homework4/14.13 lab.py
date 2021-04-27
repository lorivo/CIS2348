# Lori Vo 1852113

# Global variable
num_calls = 0


# TODO: Write the partitioning algorithm - pick the middle element as the
#       pivot, compare the values using two index variables l and h (low and high),
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary
def partition(user_ids, i, k):
    l = i - 1
    pivot = user_ids[k]

    for n in range(i, k):
        if user_ids[n] <= pivot:
            l += 1
            temp = user_ids[n]
            user_ids[n] = user_ids[l]
            user_ids[l] = temp
    temp = user_ids[k]
    user_ids[k] = user_ids[l + 1]
    user_ids[l + 1] = temp
    return l + 1


# TODO: Write the quicksort algorithm that recursively sorts the low and
#       high partitions. Add 1 to num_calls each time quicksort() is called
def quicksort(user_ids, i, k):
    global num_calls
    num_calls = num_calls + 1
#    print(num_calls)
    if i < k:
        p_index = partition(user_ids, i, k)
        quicksort(user_ids, i, p_index - 1)
        quicksort(user_ids, p_index + 1, k)


if __name__ == "__main__":
    num_calls = 0
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids, 0, len(user_ids) - 1)

    num_calls = 0
    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
