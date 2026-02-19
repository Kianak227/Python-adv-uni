# -------------------------------
# تعریف گره درخت دودویی
# -------------------------------
class Tree_Node:
    def __init__(self, x):
        self.Data = x
        self.Lchild = None
        self.Rchild = None

# -------------------------------
# تعداد برگ ها
# -------------------------------
def Count_leaves(root):
    if root is None:
        return 0
    if root.Lchild is None and root.Rchild is None:
        return 1
    return Count_leaves(root.Lchild) + Count_leaves(root.Rchild)

# -------------------------------
# تعداد گره های درجه یک
# -------------------------------
def Count_1Deg(root):
    if root is None:
        return 0
    cnt = 0
    if (root.Lchild is None) != (root.Rchild is None):  # XOR: فقط یکی موجود
        cnt = 1
    return cnt + Count_1Deg(root.Lchild) + Count_1Deg(root.Rchild)

# -------------------------------
# تعداد گره های درجه دو
# -------------------------------
def Count_2Deg(root):
    if root is None:
        return 0
    cnt = 1 if root.Lchild and root.Rchild else 0
    return cnt + Count_2Deg(root.Lchild) + Count_2Deg(root.Rchild)

# -------------------------------
# مجموع داده های درخت
# -------------------------------
def sum_Tree(root):
    if root is None:
        return 0
    return root.Data + sum_Tree(root.Lchild) + sum_Tree(root.Rchild)

# -------------------------------
# تعداد کل گره ها
# -------------------------------
def Count(root):
    if root is None:
        return 0
    return 1 + Count(root.Lchild) + Count(root.Rchild)

# -------------------------------
# پیمایش پیش‌سفارش (preorder)
# -------------------------------
def pre(root):
    if root is None:
        return
    print(root.Data, end=" ")
    pre(root.Lchild)
    pre(root.Rchild)

# -------------------------------
# جستجوی مقدار در درخت
# -------------------------------
def search(root, t):
    if root is None:
        return False
    if root.Data == t:
        return True
    return search(root.Lchild, t) or search(root.Rchild, t)

# -------------------------------
# بیشترین مقدار در درخت
# -------------------------------
def max_t(root):
    if root is None:
        return float("-inf")
    return max(root.Data, max_t(root.Lchild), max_t(root.Rchild))

# -------------------------------
# نمونه استفاده
# -------------------------------
root = Tree_Node(10)
root.Lchild = Tree_Node(5)
root.Rchild = Tree_Node(15)
root.Lchild.Lchild = Tree_Node(3)
root.Lchild.Rchild = Tree_Node(7)
root.Rchild.Rchild = Tree_Node(20)

print("پیمایش پیش‌سفارش:")
pre(root)

print("\n\nتعداد برگ‌ها:", Count_leaves(root))
print("تعداد گره‌های درجه یک:", Count_1Deg(root))
print("تعداد گره‌های درجه دو:", Count_2Deg(root))
print("مجموع داده‌ها:", sum_Tree(root))
print("تعداد کل گره‌ها:", Count(root))
print("جستجوی 7:", search(root, 7))
print("جستجوی 100:", search(root, 100))
print("حداکثر مقدار در درخت:", max_t(root))