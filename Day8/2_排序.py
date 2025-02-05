"""
Created on 2025-02-05
"""

# Your code starts here
import random


class Sort:
    def __init__(self, n):
        self.arr = [0]*n  # 必须要初始化才能用i索引赋值
        self.len = n

    def init_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0, 99)
        print(self.arr)

    def partition(self, low, high):
        pivot = self.arr[low]
        while low < high:
            if self.arr[high] >= pivot:
                high -= 1
            self.arr[low] = self.arr[high]
            if self.arr[low] <= pivot:
                low += 1
            self.arr[high] = self.arr[low]
        self.arr[low] = pivot
        return low

    def quick_sort(self, low, high):
        if low >= high:
            return
        mid = self.partition(low, high)
        self.quick_sort(low, mid - 1)
        self.quick_sort(mid + 1, high)

    def adjust_heap(self, start, end):
        i = start
        j = 2 * i + 1
        while j <= end:
            if j+1 <= end and self.arr[j] < self.arr[j+1]:
                j += 1
            if self.arr[j] > self.arr[i]:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i = j
                j = 2*i+1
            else:  # 缺少这个else会导致死循环
                break

    def build_heap(self):
        for i in range(self.len//2-1, -1, -1):
            self.adjust_heap(i, self.len-1)

    def heap_sort(self):
        self.build_heap()
        for i in range(self.len-1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.adjust_heap(0, i-1)


if __name__ == '__main__':
    sort = Sort(10)
    sort.init_data()
    # sort.quick_sort(0, 9)
    sort.heap_sort()
    print(sort.arr)
