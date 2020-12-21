
#!python
from sorting_iterative import bubble_sort
from sorting_iterative import is_sorted


def merge(items1, items2, new_list):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order."""
    if len(items1) == 0:
        return new_list + items2
    elif len(items2) == 0:
        return new_list + items1
    elif items1[0] <= items2[0]:
        new_list.append(items1[0])
        items1.pop(0)
        return merge(items1, items2, new_list)
    elif items1[0] >= items2[0]:
        new_list.append(items2[0]) 
        items2.pop(0)
        return merge(items1, items2, new_list)
# items1 = [1, 2, 3, 4]
# items2 = [1, 2, 3, 4]
# sorted = merge(items1, items2, [])
# print(sorted)
def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order."""
    mid = int(len(items) / 2)
    items1 = items[:mid]
    items2 = items[mid:]
    new_list = merge(bubble_sort(items1), bubble_sort(items2), [])
    return new_list
# items = [1, 8, 3, 7, 28, 100, 1032, 234, 839, 425]
# result = split_sort_merge(items)
# print(result)
def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order."""
    if len(items) == 1:
        return items 
    elif items != 1:
        mid = int(len(items) / 2)
        items1 = merge_sort(items[:mid])
        items2 = merge_sort(items[mid:])
        return merge(items1, items2, [])
# items = [20, 3, 34, 326, 345, 765, 35, 1]
# result  = merge_sort(items)
# print(result)
def partition(items, low, hi):
    pivot = items[low]
    li = low + 1
    hi = hi
    while True:
        while li <= hi and items[hi] >= pivot:
            hi = hi - 1
        while li <= hi and items[li] <= pivot:
            li = li + 1
        if li <= hi:
            items[li], items[hi] = items[hi], items[li]
        else:
            break
    items[low], items[hi] = items[hi], items[low]
    return hi
def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range."""
    if len(items) <= 1:
        return items 
    elif low == None and high == None:
        low = 0
        high = len(items) - 1
    if low < high:
        pivot = partition(items, low, high)
        quick_sort(items, low, pivot-1)
        quick_sort(items, pivot+1, high)
    return items
items = [90, 87, 32, 22, 53, 3, 2, 8, 89, 42, 1000, 142, 98, 32, 64, 33, 800, 720, 630, 37, 88, 87, 83, 74, 76]
result = quick_sort(items)
print(result)