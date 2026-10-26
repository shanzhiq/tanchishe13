"""快速排序 (Quick Sort) 实现

时间复杂度:
    - 平均: O(n log n)
    - 最坏: O(n^2)（数组已有序且固定选首元素为基准时）
空间复杂度: O(log n)（递归栈）
稳定性: 不稳定
"""

import random


def quick_sort(arr):
    """简洁版：返回新的排序列表（非原地）。"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """原地快排：Lomuto 分区方案。"""
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = _partition(arr, low, high)
        quick_sort_inplace(arr, low, p - 1)
        quick_sort_inplace(arr, p + 1, high)
    return arr


def _partition(arr, low, high):
    # 随机选取基准，避免最坏情况
    r = random.randint(low, high)
    arr[r], arr[high] = arr[high], arr[r]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5, 3, 3, -2, 0]
    print("原始数组:", data)
    print("简洁版结果:", quick_sort(data))

    arr = data.copy()
    quick_sort_inplace(arr)
    print("原地版结果:", arr)

    # 简单测试
    for _ in range(1000):
        t = [random.randint(-1000, 1000) for _ in range(random.randint(0, 50))]
        assert quick_sort(t) == sorted(t)
        a = t.copy()
        quick_sort_inplace(a)
        assert a == sorted(t)
    print("随机测试全部通过 ✓")
