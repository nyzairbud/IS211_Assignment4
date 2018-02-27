import random
import time

def insertion_sort(a_list):

    start = time.time()
    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    return time.time() - start

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value

def shell_sort(a_list):

    start = time.time()

    sublist_counter = len(a_list) // 2
    while sublist_counter > 0:
        for start_position in range(sublist_counter):
            gap_insertion_sort(a_list, start_position, sublist_counter)

        sublist_counter = sublist_counter // 2
    return time.time() - start

def python_sort(a_list):

    start = time.time()
    a_list.sort()
    return time.time() - start

def generate_random_list(size):
    a_list = []
    for i in range(size):
        a_list.append(random.randint(0,10000))
    return a_list

if __name__ == '__main__':

    num_list = 100
    sort_functions = [(insertion_sort,"Insertion Sort"), (shell_sort,"Shell Sort"),
                         (python_sort,"Python Sort")]
    list_sizes = [500,1000,10000]

    for list_size in list_sizes:

        sum_of_search = []

        for i in range(len(sort_functions)):
            sum_of_search.append(0.0)

        print("List of size %d:"%(list_size))

        for i in range(num_list):

            a_list = generate_random_list(list_size)

            for j, function_tuple in enumerate(sort_functions):
                function, name = function_tuple
                list_copy = a_list[:]
                duration = function(list_copy)
                sum_of_search[j] += duration

        for j, function_tuple in enumerate(sort_functions):
            function, name = function_tuple
            print("\t%s took %10.7f second to run"%(name, (sum_of_search[j]/num_list)))