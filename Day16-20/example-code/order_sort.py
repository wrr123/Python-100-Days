# -*- coding: UTF-8 -*-
def seq_search(origin_items, comp=lambda x, y: x < y):
    """顺序查找"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


if __name__ == '__main__':
    items_origin = [5, 2, 8, 4, 9, 1]
    result = seq_search(items_origin)
    print(result)
