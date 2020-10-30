# -*- coding: utf-8 -*-
def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    items_origin = [5, 2, 8, 4, 9, 1]
    find_index = bin_search(items_origin, 9)
    print("查找到的索引为%s" % find_index)
