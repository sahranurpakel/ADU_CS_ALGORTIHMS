def climb_stairs(n):
    ways = [1, 1]
    for i in range(2, n + 1):
        ways.append(ways[i - 1] + ways[i - 2])
    return ways[n]

result = climb_stairs(5)
print(result)
