# -*- coding: utf-8 -*-
def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if key == item:
            return index
    return -1


if __name__ == "__main__":
    items_origin = [5, 2, 8, 4, 9, 1]
    index_find = seq_search(items_origin, 1)
    print("查找的索引为{}".format(index_find))
