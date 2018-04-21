def paintHouse(costs):
    prev = costs[0]
    current = [0, 0, 0]

    for i in range(1, len(costs)):
        current[0] = min(prev[1], prev[2]) + costs[i][0]
        current[1] = min(prev[0], prev[2]) + costs[i][1]
        current[2] = min(prev[0], prev[1]) + costs[i][2]
        prev[:] = current[:]

    return min(prev)