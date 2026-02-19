class C_Queue:
    def __init__(self, max_size=100):
        self.list = [None] * max_size  # اصلاح آرایه
        self.front = -1
        self.rear = -1

    # درج عنصر
    def insert(self, x):
        if self.is_full():
            print("Queue is full")
            return
        if self.front == -1:  # صف خالی
            self.front = 0
            self.rear = 0
            self.list[self.rear] = x
            return
        self.rear = (self.rear + 1) % len(self.list)
        self.list[self.rear] = x

    # حذف عنصر
    def delete(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        k = self.list[self.front]
        if self.front == self.rear:  # آخرین عنصر حذف شد
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % len(self.list)
        return k

    # بررسی خالی بودن صف
    def is_empty(self):
        return self.front == -1

    # بررسی پر بودن صف
    def is_full(self):
        return (self.rear + 1) % len(self.list) == self.front

    # نمایش عناصر معتبر (موجود در صف)
    def show_valid(self):
        if self.is_empty():
            print("Queue is empty")
            return
        i = self.front
        while True:
            print(self.list[i])
            if i == self.rear:
                break
            i = (i + 1) % len(self.list)

    # پیدا کردن اولین ایندکس شامل x
    def find(self, x):
        if self.is_empty():
            return None
        i = self.front
        while True:
            if self.list[i] == x:
                return i
            if i == self.rear:
                break
            i = (i + 1) % len(self.list)
        return None

    # جایگزینی همه x با y
    def replace(self, x, y):
        if self.is_empty():
            return
        i = self.front
        while True:
            if self.list[i] == x:
                self.list[i] = y
            if i == self.rear:
                break
            i = (i + 1) % len(self.list)


# -------------------------------
# نمونه استفاده
# -------------------------------
cq = C_Queue(5)
cq.insert(10)
cq.insert(20)
cq.insert(30)
cq.insert(20)

print("صف قبل از جایگزینی:")
cq.show_valid()

print("\nایندکس 20:", cq.find(20))
cq.replace(20, 99)

print("\nصف بعد از جایگزینی 20 با 99:")
cq.show_valid()