
def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order."""
    for i in range(len(items)):
        if i == len(items) - 1:
            return True 
        elif items[i] > items[i + 1]:
            return False

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order."""
    new_items = list(items)
    while is_sorted(new_items) == False:
        for i in range(len(new_items)):
            if i + 1 == len(new_items):
                break  
            elif new_items[i] > new_items[i + 1]:
                new_items[i],new_items[i + 1] = new_items[i + 1],new_items[i]
    return new_items 

def find_least(items):
    """Finds smallest item in list and returns index."""
    sorted = bubble_sort(items)
    idx = items.index(sorted[0])
    return idx

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order."""
    new_items = items 
    while is_sorted(new_items) == False:
        for i in range(len(new_items)):
            if i + 1 == len(items):
                break  
            sliced = new_items[i:]

            least_idx = find_least(sliced)
            new_items[i],new_items[least_idx + i] = new_items[least_idx + i],new_items[i]
    return new_items

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order."""
    new_items = []
    for i in range(len(items)):
        least = items.pop(find_least(items))
        new_items.append(least)
    return new_items
    

