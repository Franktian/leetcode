def solve_knapsack(profits, weights, capacity):
  # Bottom up Dynamic programming
  n = len(profits)

  dp = [[0 for x in range(capacity + 1)] for y in range(n)]

  # Base case
  for c in range(capacity + 1):
    if weights[0] <= c:
      dp[0][c] = profits[0]

  for i in range(1, n):
    for c in range(1, capacity + 1):
      p1, p2 = 0, 0

      if weights[i] <= c:
        p1 = profits[i] + dp[i - 1][c - weights[i]]

      p2 = dp[i - 1][c]
      dp[i][c] = max(p1, p2)

  return dp[-1][-1]

if __name__ == '__main__':
  assert solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7) == 22
  assert solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6) == 17
