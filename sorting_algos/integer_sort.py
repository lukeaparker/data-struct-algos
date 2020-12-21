
from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list."""
    count = []
    [ count.append((x, 0)) for x in range(min(numbers), max(numbers) + 1)]
    for i in range(len(numbers)):
        if i <= len(numbers):
            location = [idx for idx, val in enumerate(count) if val[0] == numbers[i]][0]
            old_value = count[location]
            new_value = (old_value[0], old_value[1] + 1)
            count[location] = new_value
            print(i, numbers[i], location)
    sorted = []
    for item in count:
        if item[1] != 0:
            for i in range(item[1]):
                sorted.append(item[0])
    return sorted 
  

        







numbers = [2, 8, 3, 9, 3, 12, 18, 2, 14, 13, 28, 72, 22, 33, 48, 93, 19, 2, 4, 5, 5, 9]
test = counting_sort(numbers)
print(test)


def bucket_sort(numbers, slots=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in count order."""
    buckets = []
    [ buckets.append(list()) for x in range(slots)]
    for num in numbers:
        buckets[int(num * slots)].append(num)

    sorted = []
    for bucket in buckets:
        if len(bucket) > 0:
            bucket = insertion_sort(bucket)
            [ sorted.append(bucket[x]) for x in range(len(bucket))]
    
    return sorted
    
    






# numbers = [0.12, 0.97, 0.2, 0.92, .83, .72, .22, .38, .92, .47, .89, .36]
# test = bucket_sort(numbers)
# print(test)


