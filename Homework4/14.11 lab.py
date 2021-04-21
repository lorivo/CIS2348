# Lori Vo 1852113
def selection_sort_descend_trace(nums):
    for o in range(0, len(nums)):
        nums[o] = int(nums[o])
    for i in range(len(nums)-1):
        index_big = i
        for j in range(i+1, len(nums)):
            if nums[j] > nums[index_big]:
                index_big = j
        temp = nums[i]
        nums[i] = nums[index_big]
        nums[index_big] = temp
        print(*nums, sep=' ', end=' \n')


if __name__ == "__main__":
    numbers = input().split(' ')
    selection_sort_descend_trace(numbers)
