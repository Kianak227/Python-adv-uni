# Time complexity analysis

# loop with step = 3
for i in range(0, n+3, 3):
    t = t + 5     # operation 1
    l = 2 * l     # operation 2


# --------------------------------------
# iteration count:
# i increases by 3 each time
# number of executions ≈ (n+3) / 3
#
# operations per iteration = 2
#
# F(n) = 2 * (n+3) / 3
# F(n) ≈ (2/3)n + 2
#
# Big-O : Θ(n)