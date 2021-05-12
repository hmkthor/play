#https://edabit.com/challenge/Zerwo2AENbvRZTe83


#Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.


def next_edge(first_edge, second_edge):
    return first_edge + second_edge -1


print(next_edge(10,18))