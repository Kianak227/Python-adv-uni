# -------------------------------
# کلاس Stack با قابلیت‌های پایه و جستجو
# -------------------------------

class Stack:
    def __init__(self, limit=1000):
        self.st = []          # لیست برای ذخیره عناصر پشته
        self.lim = limit      # حداکثر ظرفیت پشته

    # اضافه کردن عنصر به پشته
    def push(self, x):
        if len(self.st) >= self.lim:
            print("stack is full")
            return -1
        self.st.append(x)

    # حذف و برگرداندن عنصر بالای پشته
    def pop(self):
        if len(self.st) == 0:
            print("stack is empty")
            return -1
        return self.st.pop()

    # مشاهده عنصر بالای پشته بدون حذف
    def peek(self):
        if len(self.st) == 0:
            print("stack is empty")
            return -1
        return self.st[-1]

    # برگرداندن همه ایندکس‌هایی که شامل x هستند
    def find(self, x):
        indexes = []
        for i in range(len(self.st)):
            if self.st[i] == x:
                indexes.append(i)
        print(indexes)

    # برگرداندن اولین ایندکس شامل x
    def find_first(self, x):
        for i in range(len(self.st)):
            if self.st[i] == x:
                print(i)
                return
        print("not found")

    # برگرداندن آخرین ایندکس شامل x
    def find_last(self, x):
        for i in range(len(self.st)-1, -1, -1):
            if self.st[i] == x:
                print(i)
                return
        print("not found")

    # جایگزینی همه x با y
    def replace(self, x, y):
        for i in range(len(self.st)):
            if self.st[i] == x:
                self.st[i] = y

# -------------------------------
# نمونه استفاده
# -------------------------------

test = Stack(10)
test.push(57)
test.push(126)
test.push(-10)
test.push(57)
test.push(126)
test.push(57)

print("Peek:", test.peek())  # مشاهده بالای پشته

# پیدا کردن ایندکس‌ها
print("همه ایندکس‌ها شامل 57:")
test.find(57)

print("اولین ایندکس شامل 126:")
test.find_first(126)

print("آخرین ایندکس شامل 57:")
test.find_last(57)

# جایگزینی عناصر
print("جایگزینی 57 با 999")
test.replace(57, 999)
print("پشته بعد از جایگزینی:", test.st)