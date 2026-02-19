# -------------------------------
# گره لیست دوطرفه
# -------------------------------
class DNode:
    def __init__(self, data):
        self.Data = data
        self.next = None
        self.back = None

# -------------------------------
# کلاس لیست دوطرفه
# -------------------------------
class DLinkedList:
    def __init__(self):
        self.head = None

    # درج در ابتدا
    def insert_first(self, x):
        if self.head is None:
            self.head = DNode(x)
            return
        a = DNode(x)
        a.next = self.head
        self.head.back = a
        self.head = a

    # درج در انتها
    def insert_last(self, x):
        if self.head is None:
            self.insert_first(x)
            return
        c = self.head
        while c.next:
            c = c.next
        a = DNode(x)
        c.next = a
        a.back = c

    # درج بعد از گره دارای مقدار x
    def insert_after(self, x, y):
        if self.head is None:
            print("List is empty")
            return
        c = self.head
        while c:
            if c.Data == x:
                if c.next is None:
                    self.insert_last(y)
                else:
                    a = DNode(y)
                    a.next = c.next
                    c.next.back = a
                    a.back = c
                    c.next = a
                return
            c = c.next
        print("Not found")

    # درج قبل از گره دارای مقدار x
    def insert_before(self, x, y):
        if self.head is None:
            print("List is empty")
            return
        c = self.head
        if c.Data == x:
            self.insert_first(y)
            return
        while c:
            if c.Data == x:
                a = DNode(y)
                a.next = c
                a.back = c.back
                c.back.next = a
                c.back = a
                return
            c = c.next
        print("Not found")

    # حذف اولین گره
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return
        c = self.head
        self.head = c.next
        if self.head:
            self.head.back = None
        del c

    # حذف آخرین گره
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return
        c = self.head
        while c.next:
            c = c.next
        if c.back is None:
            self.delete_first()
            return
        c.back.next = None
        del c

    # حذف گره قبل از گره دارای مقدار x
    def delete_before(self, x):
        if self.head is None or self.head.Data == x:
            print("Error: nothing to delete before")
            return
        c = self.head
        while c:
            if c.Data == x:
                a = c.back
                if a.back:
                    a.back.next = c
                    c.back = a.back
                else:
                    c.back = None
                    self.head = c
                del a
                return
            c = c.next
        print("Not found")

    # نمایش لیست از ابتدا
    def display_forward(self):
        c = self.head
        while c:
            print(c.Data, end=" <-> ")
            c = c.next
        print("None")

    # نمایش لیست از انتها
    def display_backward(self):
        c = self.head
        if c is None:
            print("None")
            return
        while c.next:
            c = c.next
        while c:
            print(c.Data, end=" <-> ")
            c = c.back
        print("None")

# -------------------------------
# نمونه استفاده
# -------------------------------
dll = DLinkedList()
dll.insert_first(10)
dll.insert_last(20)
dll.insert_last(30)
dll.insert_after(20, 25)
dll.insert_before(10, 5)

print("لیست از ابتدا:")
dll.display_forward()

print("لیست از انتها:")
dll.display_backward()

dll.delete_before(25)
print("بعد از حذف قبل از 25:")
dll.display_forward()