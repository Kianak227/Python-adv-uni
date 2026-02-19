class DNode:
    def __init__(self, x):
        self.Data = x
        self.next = None
        self.back = None

class DLinkedList:
    def __init__(self):
        self.head = None

    # حذف گره بعد از گره دارای مقدار x
    def del_after(self, x):
        if self.head is None:
            print("Error: list is empty")
            return

        c = self.head
        while c:
            if c.Data == x:
                if c.next:
                    a = c.next
                    c.next = a.next
                    if a.next:
                        a.next.back = c
                    del a
                    return
                else:
                    print("Error: no node after", x)
                    return
            c = c.next
        print("Not found:", x)

    # حذف گره دارای مقدار x
    def del_x(self, x):
        if self.head is None:
            print("Error: list is empty")
            return

        c = self.head
        while c:
            if c.Data == x:
                # اگر گره اول است
                if c.back is None:
                    self.head = c.next
                    if self.head:
                        self.head.back = None
                    del c
                    return
                # اگر گره آخر است
                if c.next is None:
                    c.back.next = None
                    del c
                    return
                # اگر گره وسط است
                c.back.next = c.next
                c.next.back = c.back
                del c
                return
            c = c.next
        print("Not found:", x)

    # متد نمایش لیست از ابتدا
    def display_forward(self):
        c = self.head
        while c:
            print(c.Data, end=" <-> ")
            c = c.next
        print("None")

# -------------------------------
# نمونه استفاده
# -------------------------------
dll = DLinkedList()
dll.head = DNode(10)
dll.head.next = DNode(20)
dll.head.next.back = dll.head
dll.head.next.next = DNode(30)
dll.head.next.next.back = dll.head.next

print("لیست قبل از حذف:")
dll.display_forward()

dll.del_after(20)
print("بعد از حذف بعد از 20:")
dll.display_forward()

dll.del_x(10)
print("بعد از حذف 10:")
dll.display_forward()