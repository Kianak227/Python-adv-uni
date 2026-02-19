# Time Complexity Target:
# F(n) = 3n^2 + 4n - 8

# ---------- quadratic part : 3n^2 ----------
for x in range(n):
    for y in range(n):
        s = x + y      # 1
        d = x - y      # 2
        m = x * y      # 3
# total = 3 * n * n


# ---------- linear part : 4n ----------
for k in range(n):
    a = k      # 1
    b = k + 1  # 2
    c = k + 2  # 3
    d = k + 3  # 4
# total = 4n


# ---------- constant operations : -8 ----------
# (ثابت‌ها در مرتبه تاثیر ندارند ولی در تابع کامل می‌آیند)
p = 1
q = 2
r = 3
t = 4
u = 5
v = 6
w = 7
z = 8

# ---------------------------------------------
# Operation count:
# 3n^2  from nested loops
# 4n    from single loop
# -8    constant adjustment
#
# F(n) = 3n^2 + 4n - 8
# Big-O = Θ(n^2)