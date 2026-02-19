# -------------------------------
# صف خطی (Linear Queue)
# -------------------------------

class Queue:
    def __init__(self, max_size=100):
        self.list = [None] * max_size
        self.front = -1
        self.rear = -1

    # اضافه کردن عنصر به صف
    def insert(self, x):
        if self.rear >= len(self.list) - 1:
            print("Queue is Full")
            return
        if self.front == -1:  # صف خالی
            self.front = 0
        self.rear += 1
        self.list[self.rear] = x

    # حذف عنصر از صف
    def delete(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        k = self.list[self.front]
        if self.front == self.rear:  # آخرین عنصر حذف شد
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
        return k

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.rear >= len(self.list) - 1


# -------------------------------
# نمونه استفاده از صف خطی
# -------------------------------
print("=== Linear Queue ===")
q = Queue(3)
q.insert(57)
q.insert(32)
q.insert(44)
q.insert(39)  # Queue is Full
print("حذف:", q.delete())
q.insert(39)  # حالا جای خالی هست
print("صف:", q.list[q.front:q.rear+1])


# -------------------------------
# صف حلقوی (Circular Queue)
# -------------------------------

class C_Queue:
    def __init__(self, max_size):
        self.list = [None] * max_size
        self.front = -1
        self.rear = -1

    # اضافه کردن عنصر به صف حلقوی
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

    # حذف عنصر از صف حلقوی
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

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (