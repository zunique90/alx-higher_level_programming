#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    sum1 = sum(tup[0] * tup[1] for tup in my_list)
    sum2 = sum(tup[1] for tup in my_list)
    return sum1/sum2
