# -------------------------------
# BFS: جستجوی سطحی
# -------------------------------
def BFS(graph, start):
    queue = [start]
    visited = {start}  # مجموعه گره‌های بازدید شده
    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")  # چاپ گره در هنگام بازدید
        for ne in graph[vertex]:
            if ne not in visited:  # فقط اگر بازدید نشده
                visited.add(ne)
                queue.append(ne)
    return visited

# -------------------------------
# DFS: جستجوی عمقی بازگشتی
# -------------------------------
def DFS(graph, start, visited):
    visited[start] = True
    print(start, end=" ")  # چاپ گره در هنگام بازدید
    for ne in graph[start]:
        if not visited[ne]:
            DFS(graph, ne, visited)

# -------------------------------
# Selection Sort (مرتب‌سازی انتخابی)
# -------------------------------
def sort1(A):
    B = []
    A = A.copy()  # کپی لیست اصلی برای حفظ داده‌ها
    n = len(A)
    for i in range(n):
        min_val = float("inf")
        k = -1
        for j in range(len(A)):
            if A[j] < min_val:
                min_val = A[j]
                k = j
        B.append(min_val)
        A[k] = float("inf")  # حذف عنصر انتخاب شده
    return B

# -------------------------------
# Bubble Sort (حبابی)
# -------------------------------
def Bubble(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-1-i):  # بهینه‌سازی: بخش مرتب شده را بررسی نکن
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

# -------------------------------
# نمونه استفاده
# -------------------------------

# گراف نمونه
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

print("BFS از گره 0:")
BFS(graph, 0)
print("\nDFS از گره 0:")
visited = {k: False for k in graph}
DFS(graph, 0, visited)

# مرتب‌سازی
A = [64, 25, 12, 22, 11]
print("\n\nSelection Sort:", sort1(A))

B = [64, 34, 25, 12, 22, 11, 90]
Bubble(B)
print("Bubble Sort:", B)