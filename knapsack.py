def knapsack(weights, values, capacity):
    n = len(values)
    # Create a table to store the maximum values at each subproblem
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the dp table
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Find the items to include in the knapsack
    included_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    return dp[n][capacity], included_items

# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
max_value, items_in_knapsack = knapsack(weights, values, capacity)
print("Maximum value:", max_value)
print("Items included:", [i for i in items_in_knapsack])
