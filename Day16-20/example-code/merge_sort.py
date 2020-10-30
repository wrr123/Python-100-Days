# -*- coding: utf-8 -*-
def merge_sort(items, comp=lambda x, y: x <= y):
    """
    归并排序(分治法)
    :param items:
    :param comp:
    :return:
    """
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    # 二路归并排序
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    print("mid: %d, left: %d, right: %d" % (mid, len(left), len(right)))
    return merge(left, right, comp)


def merge(items1, items2, comp):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    print(items)
    items += items1[index1:]
    items += items2[index2:]
    print(items)
    return items


if __name__ == "__main__":
    items_origin = [5, 2, 8, 4, 9, 1, 19, 0, 13]
    merge_sort(items_origin)
