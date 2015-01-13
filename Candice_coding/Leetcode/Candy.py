'''There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?'''

def candy(ratings):
    n = len(ratings)
    dist = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            dist[i] = dist[i-1] + 1
    for j in range(n-2, -1, -1):
        if ratings[j] > ratings[j+1] and dist[j] <= dist[j+1]:
            dist[j] = dist[j+1] + 1
    return sum(dist)

if __name__ == '__main__':
    ratings = [8,1,2,4,6,10,3]
    print candy(ratings)