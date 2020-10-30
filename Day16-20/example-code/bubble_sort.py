def bubble_sort(items_origin, comp=lambda x, y: x > y):
    """
    高质量冒泡排序(搅拌排序)
    :return:
    """
    items = items_origin[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j - 1], items[j] = items[j], items[j - 1]
                    swapped = True
            if not swapped:
                break
    print(items)


if __name__ == "__main__":
    items_origin = [5, 2, 8, 4, 9, 1]
    bubble_sort(items_origin)