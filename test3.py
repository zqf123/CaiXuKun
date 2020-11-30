import time
import sys
import matplotlib.pyplot as plt
import numpy as np
sys.setrecursionlimit(100000000)
def sort(lst):
    sortHelper(lst,0,len(lst)-1)

def sortHelper(lst,low,high):
    if low < high:
        indexOfMin = low
        min = lst[low]
        for i in range(low+1,high+1):
            if lst[i] < min:
                min = lst[i]
                indexOfMin = i

        lst[indexOfMin] = lst[low]
        lst[low] = min

        sortHelper(lst,low+1,high)
#
def mergeSort(nums):
    n = len(nums)
    if n > 1:
        m = n // 2
        nums1,nums2 = nums[:m],nums[m:]

        mergeSort(nums1)
        mergeSort(nums2)
        merge(nums1,nums2,nums)


def merge(left, right,nums):
    nums = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if (left[i] < right[i]):
            nums.append(left[i])
            i += 1
        else:
            nums.append(right[j])
            j += 1

    nums += left[i:]
    nums += right[j:]
    return nums

if __name__ == '__main__':
    sortnums = []
    mergenums = []
    for i in [100,200,300,400,500]:
        nums = [9,2,6,8,4]*i
        start = time.time()
        mergeSort(nums)
        end = time.time()
        mergenums.append(end-start)
        print('time cost : %.10f' %(end-start))

        start = time.time()
        sort(nums)
        end = time.time()
        sortnums.append(end-start)
        print('time cost : %.10f' % (end - start))
        print("=======================")
    print(sortnums)
    print(mergenums)

# max_len = 3000
# lst_len = list(np.arange(500, max_len, 250))
# select_time, merge_time = [], []
# for len_ in lst_len:
#     num = np.random.randint(1000, size=len_)
#     num_copy = num[:]
#     start_time = time()
#     sort(num, 0, len(num) - 1)
#     end_time = time()
#     select_time.append(end_time - start_time)
#
#     start_time = time()
#     mergeSort(num_copy)
#     end_time = time()
#     merge_time.append(end_time - start_time)
#
# plt.plot(lst_len, select_time, label='Selectsort')
# plt.plot(lst_len, merge_time, label='Mergesort')
# plt.xlabel('List Length')
# plt.ylabel('Time(seconds)')
# plt.legend();


