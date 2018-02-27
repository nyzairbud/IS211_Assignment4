import time
import random


def sequential_search(a_list, item):
    begin = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    elapsed = end - begin

    if not found:
        pos = -1

    return (pos, elapsed)

def ordered_sequential_search(a_list, item):
    a_list.sort()
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = time.time()
    elapsed = end - start

    if not found:
        pos = -1

    return (pos, elapsed)


def binary_search_it(a_list, item):
    a_list.sort()
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midway = (first + last) // 2
        if a_list[midway] == item:
            found = True
        else:
            if item < a_list[midway]:
                last = midway - 1
            else:
                first = midway + 1
    end = time.time()
    elapsed = end - start

    if not found:
        midway = -1

    return (midway, elapsed)


def binary_search_rec(a_list, item):

    def binary_search_helper(a_list, item, begin_time, start, end):
        if start > end:
            return (-1, time.time() - begin)

        midpoint = (start + end) // 2

        if a_list[midpoint] == item:
            return (midpoint, time.time() - begin)
        else:
            if item < a_list[midpoint]:
                return binary_search_helper(a_list, item, begin_time, start,
                                            midpoint - 1)
            else:
                return binary_search_helper(a_list, item, begin_time,
                                            midpoint + 1, end)

    a_list.sort()
    begin = time.time()
    return binary_search_helper(a_list, item, begin, 0, len(a_list))

def generate_random_list(size):

    the_list = []
    for i in range(size):
        the_list.append(random.randint(0, 10000))
    return the_list

def main():
    num_list = 100
    sort_functions = [(sequential_search, "Sequential Search"),
                      (ordered_sequential_search, "Ordered Sequential Search"),
                      (binary_search_it, "Iterative Binary Search"),
                      (binary_search_rec, "Recursive Binary Search")]
    list_sizes = [500, 1000, 10000]

    for list_size in list_sizes:

        sum_of_search_time_list = []

        for i in range(len(sort_functions)):
            sum_of_search_time_list.append(0.0)

        print("List of size %d:"%(list_size))

        for i in range(num_list):

            a_list = generate_random_list(list_size)

            for j, function_tuple in enumerate(sort_functions):
                function, name = function_tuple
                result, duration = function(a_list, -1)
                sum_of_search_time_list[j] += duration

        for j, function_tuple in enumerate(sort_functions):
            function, name = function_tuple
            print("\t%s took %10.7f seconds"%(name,
                 (sum_of_search_time_list[j]/num_list)))

if __name__ == '__main__':
    main()