'''
There are M cities and M-1 city connections.
An array is used to express this graph of cities.
If A[x] = y, then city x and city y are connected.
If A[x] = x, then city x is the capital city.
Please count separately the number of cities that have 
1, 2, 3,..., M-1 distance from the capital.
Your algorithm should have O(M) time complexity and
O(M) space complexity
'''

from collections import deque


def capitalDistance(graph_ls):
    connect_dict = {}
    distance_count = [0] * len(graph_ls)
    capital = None
    for i in xrange(len(graph_ls)):
        j = graph_ls[i]
        if j == i:
            capital = i
        elif j not in connect_dict:
            connect_dict[j] = [i]
        else:
            connect_dict[j].append(i)
    city_q = deque([capital])
    distance = 0
    current_level = 1
    next_level = 0
    while city_q:
        tmp = city_q.popleft()
        current_level -= 1
        distance_count[distance] += 1
        if tmp in connect_dict:
            for each_city in connect_dict[tmp]:
                city_q.append(each_city)
                next_level += 1
        if not current_level:
            distance += 1
            current_level = next_level
            next_level = 0
    return distance_count[1:]


if __name__ == '__main__':
    graph_ls = [1,3,3,3,5,6,2,6]  
    print capitalDistance(graph_ls)    
        
