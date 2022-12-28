#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for element in range(1, len(my_list) + 1):
        idx = element * -1
        print("{}".format(my_list[idx]))
